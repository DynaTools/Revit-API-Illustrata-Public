using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;

// Estrattore Revit API -> schede Markdown (frontmatter YAML).
// Legge i METADATI di RevitAPI.dll con MetadataLoadContext: nessun caricamento
// runtime, nessuna dipendenza da Revit in esecuzione.
// Uso: revitapi-extractor <revitVersion> <outDir> [filtroNome]
class Program
{
    static readonly string[] SkipMethods = { "Equals", "GetHashCode", "ToString", "GetType", "Finalize", "MemberwiseClone" };

    static int Main(string[] args)
    {
        string ver    = args.Length > 0 ? args[0] : "2025";
        string outDir = args.Length > 1 ? args[1] : "docs/classi";
        string filter = args.Length > 2 ? args[2] : null;

        string revitDir = $@"C:\Program Files\Autodesk\Revit {ver}";
        string dll = Path.Combine(revitDir, "RevitAPI.dll");
        if (!File.Exists(dll)) { Console.Error.WriteLine($"Non trovo {dll}"); return 1; }

        var paths = new List<string>();
        paths.AddRange(Directory.GetFiles(revitDir, "*.dll"));
        paths.AddRange(Directory.GetFiles(System.Runtime.InteropServices.RuntimeEnvironment.GetRuntimeDirectory(), "*.dll"));
        var resolver = new PathAssemblyResolver(paths.GroupBy(Path.GetFileName).Select(g => g.First()));

        using var mlc = new MetadataLoadContext(resolver);
        var asm = mlc.LoadFromAssemblyPath(dll);
        string apiver = asm.GetName().Version.ToString();

        Type[] types;
        try { types = asm.GetExportedTypes(); }
        catch (ReflectionTypeLoadException ex) { types = ex.Types.Where(t => t != null).ToArray(); }

        Directory.CreateDirectory(outDir);
        int n = 0, fail = 0;
        foreach (var t in types.Where(t => t.IsClass && !t.IsSpecialName))
        {
            if (filter != null && (t.FullName == null || !t.FullName.Contains(filter))) continue;
            try {
                string ns = string.IsNullOrEmpty(t.Namespace) ? "_global" : Safe(t.Namespace);
                string dir = Path.Combine(outDir, ns);
                Directory.CreateDirectory(dir);
                File.WriteAllText(Path.Combine(dir, Safe(t.Name) + ".md"), Render(t, ver, apiver), new UTF8Encoding(false));
                n++;
            } catch { fail++; }
        }
        Console.WriteLine($"RevitAPI {apiver} (Revit {ver}): scritte {n} schede in {outDir} ({fail} saltate)");
        return 0;
    }

    static string Render(Type t, string ver, string apiver)
    {
        string recv = char.ToLowerInvariant(t.Name[0]) + t.Name.Substring(1);
        var flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static | BindingFlags.DeclaredOnly;

        var rows = new List<(string kind, string cs, string py, string tipo)>();
        foreach (var p in t.GetProperties(flags).OrderBy(p => p.Name))
        {
            try {
                string acc = p.CanWrite ? "{ get; set; }" : "{ get; }";
                bool stat = (p.GetMethod ?? p.SetMethod)?.IsStatic ?? false;
                rows.Add(("property", $"{Friendly(p.PropertyType)} {p.Name} {acc}",
                          (stat ? t.Name : recv) + "." + p.Name, Friendly(p.PropertyType)));
            } catch { }
        }
        foreach (var m in t.GetMethods(flags).OrderBy(m => m.Name))
        {
            if (m.IsSpecialName || SkipMethods.Contains(m.Name)) continue;
            try {
                var pars = m.GetParameters();
                string ps = string.Join(", ", pars.Select(pp => Friendly(pp.ParameterType)));
                string args = string.Join(", ", pars.Select(pp => pp.Name));
                rows.Add(("method", $"{Friendly(m.ReturnType)} {m.Name}({ps})",
                          (m.IsStatic ? t.Name : recv) + "." + m.Name + "(" + args + ")", Friendly(m.ReturnType)));
            } catch { }
        }

        var sb = new StringBuilder();
        sb.Append("---\n");
        sb.Append($"title: {t.Name}\n");
        sb.Append($"classe: {t.FullName}\n");
        sb.Append($"namespace: {t.Namespace}\n");
        sb.Append($"eredita: {(t.BaseType != null ? t.BaseType.FullName : "")}\n");
        sb.Append($"revit: \"{ver}\"\n");
        sb.Append($"revitapi: \"{apiver}\"\n");
        sb.Append("stato: auto\n");
        sb.Append("verbo: leggere\n");
        sb.Append($"membri_n: {rows.Count}\n");
        sb.Append("---\n\n");
        sb.Append($"# {t.Name}\n\n");
        sb.Append("!!! note \"Scheda automatica\"\n");
        sb.Append("    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).\n\n");
        sb.Append("## La classe\n\n_(una frase: cos'è e a cosa serve)_\n\n");
        sb.Append("## La corrispondenza\n\n");
        sb.Append("| nella doc (C#) | in python | tipo |\n");
        sb.Append("|---|---|---|\n");
        foreach (var r in rows)
            sb.Append($"| `{r.cs}` | `{r.py}` | {r.tipo} |\n");
        sb.Append("\n## Il tranello\n\n_(ciò che la pagina non dice e ti farebbe sbagliare)_\n\n");
        sb.Append("## Lo script\n\n```python\n# esempio da completare\n```\n");
        return sb.ToString();
    }

    static string Friendly(Type t)
    {
        if (t.IsByRef) return Friendly(t.GetElementType()) + "&";
        if (t.IsArray) return Friendly(t.GetElementType()) + "[]";
        if (t.IsGenericType)
        {
            string nm = t.Name; int i = nm.IndexOf('`'); if (i > 0) nm = nm.Substring(0, i);
            return nm + "<" + string.Join(", ", t.GetGenericArguments().Select(Friendly)) + ">";
        }
        return t.Name;
    }

    static string Q(string s) => "\"" + s.Replace("\"", "'") + "\"";
    static string Safe(string s)
    {
        var sb = new StringBuilder();
        foreach (char c in s.Replace('+', '.'))
            sb.Append(char.IsLetterOrDigit(c) || c == '.' || c == '-' || c == '_' ? c : '_');
        return sb.ToString();
    }
}

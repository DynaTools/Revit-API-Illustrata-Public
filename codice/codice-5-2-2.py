# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 5.2.2  |  Capitolo 5.2 - Il cammino verso il C#
# Sezione: Lo stesso script nelle due lingue

// C# (lo stesso Livello 4)
var walls = new FilteredElementCollector(doc)
                  .OfClass(typeof(Wall));

using (Transaction t = new Transaction(doc, "Riempire Commenti"))
{
    t.Start();
    foreach (Wall w in walls)
    {
        Parameter p = w.LookupParameter("Commenti");
        if (p != null && !p.IsReadOnly)
            p.Set("Verificato");
    }
    t.Commit();
}

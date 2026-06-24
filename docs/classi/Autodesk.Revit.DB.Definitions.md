---
title: Definitions
classe: Autodesk.Revit.DB.Definitions
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# Definitions

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `definitions.IsEmpty` | Boolean |
| `Definition Item { get; }` | `definitions.Item` | Definition |
| `Int32 Size { get; }` | `definitions.Size` | Int32 |
| `Boolean Contains(Definition)` | `definitions.Contains(definition)` | Boolean |
| `Definition Create(ExternalDefinitionCreationOptions)` | `definitions.Create(option)` | Definition |
| `Void Dispose()` | `definitions.Dispose()` | Void |
| `IEnumerator<Definition> GetEnumerator()` | `definitions.GetEnumerator()` | IEnumerator<Definition> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

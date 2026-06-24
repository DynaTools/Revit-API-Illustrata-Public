---
title: DirectShapeLibrary
classe: Autodesk.Revit.DB.DirectShapeLibrary
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# DirectShapeLibrary

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `directShapeLibrary.IsValidObject` | Boolean |
| `Void AddDefinition(String, IList<GeometryObject>)` | `directShapeLibrary.AddDefinition(id, GNodes)` | Void |
| `Void AddDefinition(String, GeometryObject)` | `directShapeLibrary.AddDefinition(id, GNode)` | Void |
| `Void AddDefinitionType(String, ElementId)` | `directShapeLibrary.AddDefinitionType(id, typeId)` | Void |
| `Boolean Contains(String)` | `directShapeLibrary.Contains(id)` | Boolean |
| `Boolean ContainsType(String)` | `directShapeLibrary.ContainsType(name)` | Boolean |
| `Void Dispose()` | `directShapeLibrary.Dispose()` | Void |
| `IList<GeometryObject> FindDefinition(String)` | `directShapeLibrary.FindDefinition(id)` | IList<GeometryObject> |
| `ElementId FindDefinitionType(String)` | `directShapeLibrary.FindDefinitionType(id)` | ElementId |
| `DirectShapeLibrary GetDirectShapeLibrary(Document)` | `DirectShapeLibrary.GetDirectShapeLibrary(ADoc)` | DirectShapeLibrary |
| `Void Reset()` | `directShapeLibrary.Reset()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

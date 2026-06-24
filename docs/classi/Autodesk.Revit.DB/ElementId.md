---
title: ElementId
classe: Autodesk.Revit.DB.ElementId
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# ElementId

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 IntegerValue { get; }` | `elementId.IntegerValue` | Int32 |
| `ElementId InvalidElementId { get; }` | `ElementId.InvalidElementId` | ElementId |
| `Int64 Value { get; }` | `elementId.Value` | Int64 |
| `Int32 Compare(ElementId)` | `elementId.Compare(id)` | Int32 |
| `ElementId Parse(String)` | `ElementId.Parse(idStr)` | ElementId |
| `Boolean TryParse(String, ElementId&)` | `ElementId.TryParse(idStr, id)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

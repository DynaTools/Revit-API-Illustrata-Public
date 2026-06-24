---
title: Segment
classe: Autodesk.Revit.DB.Segment
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# Segment

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String Description { get; set; }` | `segment.Description` | String |
| `ElementId MaterialId { get; }` | `segment.MaterialId` | ElementId |
| `Double Roughness { get; set; }` | `segment.Roughness` | Double |
| `Int32 SizeCount { get; }` | `segment.SizeCount` | Int32 |
| `Void AddSize(MEPSize)` | `segment.AddSize(size)` | Void |
| `ICollection<MEPSize> GetSizes()` | `segment.GetSizes()` | ICollection<MEPSize> |
| `Void RemoveSize(Double)` | `segment.RemoveSize(nominalDiameter)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

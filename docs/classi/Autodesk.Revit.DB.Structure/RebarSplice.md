---
title: RebarSplice
classe: Autodesk.Revit.DB.Structure.RebarSplice
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# RebarSplice

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 ConnectedRebarEnd { get; }` | `rebarSplice.ConnectedRebarEnd` | Int32 |
| `ElementId ConnectedRebarId { get; }` | `rebarSplice.ConnectedRebarId` | ElementId |
| `Boolean IsValidObject { get; }` | `rebarSplice.IsValidObject` | Boolean |
| `Int32 SourceRebarEnd { get; }` | `rebarSplice.SourceRebarEnd` | Int32 |
| `ElementId SourceRebarId { get; }` | `rebarSplice.SourceRebarId` | ElementId |
| `RebarSplicePosition SplicePosition { get; set; }` | `rebarSplice.SplicePosition` | RebarSplicePosition |
| `ElementId SpliceTypeId { get; set; }` | `rebarSplice.SpliceTypeId` | ElementId |
| `Void Dispose()` | `rebarSplice.Dispose()` | Void |
| `RebarSpliceGeometry GetRebarSpliceGeometry()` | `rebarSplice.GetRebarSpliceGeometry()` | RebarSpliceGeometry |
| `Void MoveRebarSpliceGeometry(XYZ)` | `rebarSplice.MoveRebarSpliceGeometry(translation)` | Void |
| `Void RotateRebarSpliceGeometry(Line, Double)` | `rebarSplice.RotateRebarSpliceGeometry(axis, angle)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

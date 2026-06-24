---
title: PointCloudFilter
classe: Autodesk.Revit.DB.PointClouds.PointCloudFilter
namespace: Autodesk.Revit.DB.PointClouds
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# PointCloudFilter

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `pointCloudFilter.IsValidObject` | Boolean |
| `PointCloudFilter Clone()` | `pointCloudFilter.Clone()` | PointCloudFilter |
| `Void Dispose()` | `pointCloudFilter.Dispose()` | Void |
| `Void PrepareForCell(XYZ, XYZ, Int32)` | `pointCloudFilter.PrepareForCell(min, max, numTests)` | Void |
| `Int32 TestCell(XYZ, XYZ)` | `pointCloudFilter.TestCell(min, max)` | Int32 |
| `Boolean TestPoint(CloudPoint)` | `pointCloudFilter.TestPoint(point)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

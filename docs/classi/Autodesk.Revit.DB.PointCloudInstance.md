---
title: PointCloudInstance
classe: Autodesk.Revit.DB.PointCloudInstance
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Instance
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# PointCloudInstance

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `SelectionFilterAction FilterAction { get; set; }` | `pointCloudInstance.FilterAction` | SelectionFilterAction |
| `Boolean SupportsOverrides { get; }` | `pointCloudInstance.SupportsOverrides` | Boolean |
| `Boolean ContainsScan(String)` | `pointCloudInstance.ContainsScan(scanName)` | Boolean |
| `PointCloudInstance Create(Document, ElementId, Transform)` | `PointCloudInstance.Create(document, typeId, transform)` | PointCloudInstance |
| `PointCollection GetPoints(PointCloudFilter, Double, Int32)` | `pointCloudInstance.GetPoints(filter, averageDistance, numPoints)` | PointCollection |
| `IList<String> GetRegions()` | `pointCloudInstance.GetRegions()` | IList<String> |
| `XYZ GetScanOrigin(String)` | `pointCloudInstance.GetScanOrigin(scanName)` | XYZ |
| `IList<String> GetScans()` | `pointCloudInstance.GetScans()` | IList<String> |
| `PointCloudFilter GetSelectionFilter()` | `pointCloudInstance.GetSelectionFilter()` | PointCloudFilter |
| `Boolean HasColor()` | `pointCloudInstance.HasColor()` | Boolean |
| `Void SetSelectionFilter(PointCloudFilter)` | `pointCloudInstance.SetSelectionFilter(pFilter)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

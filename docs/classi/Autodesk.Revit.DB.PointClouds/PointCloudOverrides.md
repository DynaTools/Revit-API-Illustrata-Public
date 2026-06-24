---
title: PointCloudOverrides
classe: Autodesk.Revit.DB.PointClouds.PointCloudOverrides
namespace: Autodesk.Revit.DB.PointClouds
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# PointCloudOverrides

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `pointCloudOverrides.IsValidObject` | Boolean |
| `Boolean ArePointCloudOverrideSettingsValid(String, PointCloudOverrideSettings)` | `PointCloudOverrides.ArePointCloudOverrideSettingsValid(tag, settings)` | Boolean |
| `Void Assign(PointCloudOverrides)` | `pointCloudOverrides.Assign(other)` | Void |
| `Void Dispose()` | `pointCloudOverrides.Dispose()` | Void |
| `PointCloudOverrideSettings GetPointCloudRegionOverrideSettings(ElementId, String, Document)` | `pointCloudOverrides.GetPointCloudRegionOverrideSettings(elementId, regionTag, doc)` | PointCloudOverrideSettings |
| `PointCloudOverrideSettings GetPointCloudRegionOverrideSettings(ElementId)` | `pointCloudOverrides.GetPointCloudRegionOverrideSettings(elementId)` | PointCloudOverrideSettings |
| `PointCloudOverrideSettings GetPointCloudScanOverrideSettings(ElementId, String, Document)` | `pointCloudOverrides.GetPointCloudScanOverrideSettings(elementId, scanTag, doc)` | PointCloudOverrideSettings |
| `PointCloudOverrideSettings GetPointCloudScanOverrideSettings(ElementId)` | `pointCloudOverrides.GetPointCloudScanOverrideSettings(elementId)` | PointCloudOverrideSettings |
| `Boolean IsEqual(PointCloudOverrides)` | `pointCloudOverrides.IsEqual(other)` | Boolean |
| `Void SetPointCloudRegionOverrideSettings(ElementId, PointCloudOverrideSettings, String, Document)` | `pointCloudOverrides.SetPointCloudRegionOverrideSettings(elementId, newSettings, regionTag, doc)` | Void |
| `Void SetPointCloudRegionOverrideSettings(ElementId, PointCloudOverrideSettings)` | `pointCloudOverrides.SetPointCloudRegionOverrideSettings(elementId, newSettings)` | Void |
| `Void SetPointCloudScanOverrideSettings(ElementId, PointCloudOverrideSettings, String, Document)` | `pointCloudOverrides.SetPointCloudScanOverrideSettings(elementId, newSettings, scanTag, doc)` | Void |
| `Void SetPointCloudScanOverrideSettings(ElementId, PointCloudOverrideSettings)` | `pointCloudOverrides.SetPointCloudScanOverrideSettings(elementId, newSettings)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

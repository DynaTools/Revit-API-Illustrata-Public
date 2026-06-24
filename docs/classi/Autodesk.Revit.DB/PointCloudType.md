---
title: PointCloudType
classe: Autodesk.Revit.DB.PointCloudType
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# PointCloudType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `PointCloudColorEncoding ColorEncoding { get; }` | `pointCloudType.ColorEncoding` | PointCloudColorEncoding |
| `String EngineIdentifier { get; }` | `pointCloudType.EngineIdentifier` | String |
| `PointCloudFoundStatus FoundStatus { get; }` | `pointCloudType.FoundStatus` | PointCloudFoundStatus |
| `XYZ Offset { get; }` | `pointCloudType.Offset` | XYZ |
| `Double Scale { get; set; }` | `pointCloudType.Scale` | Double |
| `PointCloudType Create(Document, String, String)` | `PointCloudType.Create(document, engineIdentifier, typeIdentifier)` | PointCloudType |
| `ModelPath GetPath()` | `pointCloudType.GetPath()` | ModelPath |
| `RCProject GetReCapProject()` | `pointCloudType.GetReCapProject()` | RCProject |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

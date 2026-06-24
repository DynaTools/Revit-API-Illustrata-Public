---
title: StairsPath
classe: Autodesk.Revit.DB.Architecture.StairsPath
namespace: Autodesk.Revit.DB.Architecture
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# StairsPath

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String DownText { get; set; }` | `stairsPath.DownText` | String |
| `XYZ DownTextOffset { get; set; }` | `stairsPath.DownTextOffset` | XYZ |
| `Boolean ShowDownText { get; set; }` | `stairsPath.ShowDownText` | Boolean |
| `Boolean ShowUpText { get; set; }` | `stairsPath.ShowUpText` | Boolean |
| `LinkElementId StairsId { get; }` | `stairsPath.StairsId` | LinkElementId |
| `Double StairsPathOffset { get; set; }` | `stairsPath.StairsPathOffset` | Double |
| `StairsTextOrientation TextOrientation { get; set; }` | `stairsPath.TextOrientation` | StairsTextOrientation |
| `String UpText { get; set; }` | `stairsPath.UpText` | String |
| `XYZ UpTextOffset { get; set; }` | `stairsPath.UpTextOffset` | XYZ |
| `Boolean CanCreateOnMultistoryStairs(Document, LinkElementId)` | `StairsPath.CanCreateOnMultistoryStairs(document, multistoryStairsId)` | Boolean |
| `StairsPath Create(Document, LinkElementId, ElementId, ElementId)` | `StairsPath.Create(document, stairsId, typeId, planViewId)` | StairsPath |
| `IList<StairsPath> CreateOnMultistoryStairs(Document, LinkElementId, ElementId)` | `StairsPath.CreateOnMultistoryStairs(document, multistoryStairsId, typeId)` | IList<StairsPath> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

---
title: FilledRegionType
classe: Autodesk.Revit.DB.FilledRegionType
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.LineAndTextAttrSymbol
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# FilledRegionType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Color BackgroundPatternColor { get; set; }` | `filledRegionType.BackgroundPatternColor` | Color |
| `ElementId BackgroundPatternId { get; set; }` | `filledRegionType.BackgroundPatternId` | ElementId |
| `Color ForegroundPatternColor { get; set; }` | `filledRegionType.ForegroundPatternColor` | Color |
| `ElementId ForegroundPatternId { get; set; }` | `filledRegionType.ForegroundPatternId` | ElementId |
| `Boolean IsMasking { get; set; }` | `filledRegionType.IsMasking` | Boolean |
| `Int32 LineWeight { get; set; }` | `filledRegionType.LineWeight` | Int32 |
| `Boolean IsValidBackgroundPatternId(ElementId)` | `filledRegionType.IsValidBackgroundPatternId(patternId)` | Boolean |
| `Boolean IsValidFillPatternId(ElementId)` | `filledRegionType.IsValidFillPatternId(patternId)` | Boolean |
| `Boolean IsValidForegroundPatternId(ElementId)` | `filledRegionType.IsValidForegroundPatternId(patternId)` | Boolean |
| `Boolean IsValidLineWeight(Int32)` | `FilledRegionType.IsValidLineWeight(lineWeight)` | Boolean |
| `Boolean IsValidMasking(Boolean)` | `filledRegionType.IsValidMasking(isMasking)` | Boolean |
| `Boolean IsValidSolidFillPatternId(ElementId)` | `filledRegionType.IsValidSolidFillPatternId(patternId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

---
title: RebarHookType
classe: Autodesk.Revit.DB.Structure.RebarHookType
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# RebarHookType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double HookAngle { get; set; }` | `rebarHookType.HookAngle` | Double |
| `Double StraightLineMultiplier { get; set; }` | `rebarHookType.StraightLineMultiplier` | Double |
| `RebarStyle Style { get; set; }` | `rebarHookType.Style` | RebarStyle |
| `RebarHookType Create(Document, Double, Double)` | `RebarHookType.Create(doc, angle, multiplier)` | RebarHookType |
| `ElementId CreateDefaultRebarHookType(Document)` | `RebarHookType.CreateDefaultRebarHookType(ADoc)` | ElementId |
| `Double GetDefaultHookExtension(Double)` | `rebarHookType.GetDefaultHookExtension(barDiameter)` | Double |
| `Double GetHookExtensionLength(RebarBarType)` | `rebarHookType.GetHookExtensionLength(barType)` | Double |
| `Boolean IsOffsetLengthRequired()` | `rebarHookType.IsOffsetLengthRequired()` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

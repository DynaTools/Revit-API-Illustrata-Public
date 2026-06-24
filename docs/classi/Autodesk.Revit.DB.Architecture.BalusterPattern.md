---
title: BalusterPattern
classe: Autodesk.Revit.DB.Architecture.BalusterPattern
namespace: Autodesk.Revit.DB.Architecture
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# BalusterPattern

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `BreakPatternCondition BreakPattern { get; set; }` | `balusterPattern.BreakPattern` | BreakPatternCondition |
| `PatternJustification DistributionJustification { get; set; }` | `balusterPattern.DistributionJustification` | PatternJustification |
| `Double EndSpace { get; set; }` | `balusterPattern.EndSpace` | Double |
| `ElementId ExcessLengthFillBalusterId { get; set; }` | `balusterPattern.ExcessLengthFillBalusterId` | ElementId |
| `Double ExcessLengthFillSpacing { get; set; }` | `balusterPattern.ExcessLengthFillSpacing` | Double |
| `Boolean IsValidObject { get; }` | `balusterPattern.IsValidObject` | Boolean |
| `Double Length { get; }` | `balusterPattern.Length` | Double |
| `Double PatternAngle { get; set; }` | `balusterPattern.PatternAngle` | Double |
| `Void Dispose()` | `balusterPattern.Dispose()` | Void |
| `BalusterInfo DuplicateBaluster(Int32)` | `balusterPattern.DuplicateBaluster(index)` | BalusterInfo |
| `BalusterInfo GetBaluster(Int32)` | `balusterPattern.GetBaluster(index)` | BalusterInfo |
| `Int32 GetBalusterCount()` | `balusterPattern.GetBalusterCount()` | Int32 |
| `Void RemoveBaluster(Int32)` | `balusterPattern.RemoveBaluster(index)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

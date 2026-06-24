---
title: StructuralFramingUtils
classe: Autodesk.Revit.DB.Structure.StructuralFramingUtils
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# StructuralFramingUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Void AllowJoinAtEnd(FamilyInstance, Int32)` | `StructuralFramingUtils.AllowJoinAtEnd(familyInstance, end)` | Void |
| `Boolean CanFlipEnds(FamilyInstance)` | `StructuralFramingUtils.CanFlipEnds(familyInstance)` | Boolean |
| `Boolean CanSetEndReference(FamilyInstance, Int32)` | `StructuralFramingUtils.CanSetEndReference(familyInstance, end)` | Boolean |
| `Void DisallowJoinAtEnd(FamilyInstance, Int32)` | `StructuralFramingUtils.DisallowJoinAtEnd(familyInstance, end)` | Void |
| `Void FlipEnds(FamilyInstance)` | `StructuralFramingUtils.FlipEnds(familyInstance)` | Void |
| `Reference GetEndReference(FamilyInstance, Int32)` | `StructuralFramingUtils.GetEndReference(familyInstance, end)` | Reference |
| `Boolean IsEndReferenceValid(FamilyInstance, Int32, Reference)` | `StructuralFramingUtils.IsEndReferenceValid(familyInstance, end, pick)` | Boolean |
| `Boolean IsJoinAllowedAtEnd(FamilyInstance, Int32)` | `StructuralFramingUtils.IsJoinAllowedAtEnd(familyInstance, end)` | Boolean |
| `Void RemoveEndReference(FamilyInstance, Int32)` | `StructuralFramingUtils.RemoveEndReference(familyInstance, end)` | Void |
| `Void SetEndReference(FamilyInstance, Int32, Reference)` | `StructuralFramingUtils.SetEndReference(familyInstance, end, pick)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

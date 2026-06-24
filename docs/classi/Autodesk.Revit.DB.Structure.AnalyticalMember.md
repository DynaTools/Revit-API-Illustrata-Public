---
title: AnalyticalMember
classe: Autodesk.Revit.DB.Structure.AnalyticalMember
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Structure.AnalyticalElement
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# AnalyticalMember

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double CrossSectionRotation { get; set; }` | `analyticalMember.CrossSectionRotation` | Double |
| `ElementId SectionTypeId { get; set; }` | `analyticalMember.SectionTypeId` | ElementId |
| `StructuralSectionShape StructuralSectionShape { get; }` | `analyticalMember.StructuralSectionShape` | StructuralSectionShape |
| `Boolean CanSplit()` | `analyticalMember.CanSplit()` | Boolean |
| `AnalyticalMember Create(Document, Curve)` | `AnalyticalMember.Create(aDoc, curve)` | AnalyticalMember |
| `Void FlipCurve()` | `analyticalMember.FlipCurve()` | Void |
| `IList<MemberForces> GetMemberForces()` | `analyticalMember.GetMemberForces()` | IList<MemberForces> |
| `IList<ReleaseConditions> GetReleaseConditions()` | `analyticalMember.GetReleaseConditions()` | IList<ReleaseConditions> |
| `ReleaseType GetReleaseType(Boolean)` | `analyticalMember.GetReleaseType(start)` | ReleaseType |
| `Boolean IsValidCurve(Curve)` | `AnalyticalMember.IsValidCurve(curve)` | Boolean |
| `Boolean IsValidSectionTypeId(ElementId)` | `analyticalMember.IsValidSectionTypeId(familySymbolId)` | Boolean |
| `Void SetCurve(Curve)` | `analyticalMember.SetCurve(curve)` | Void |
| `Void SetMemberForces(MemberForces)` | `analyticalMember.SetMemberForces(memberForces)` | Void |
| `Void SetMemberForces(Boolean, XYZ, XYZ)` | `analyticalMember.SetMemberForces(start, force, moment)` | Void |
| `Void SetReleaseConditions(ReleaseConditions)` | `analyticalMember.SetReleaseConditions(releaseConditions)` | Void |
| `Void SetReleaseType(Boolean, ReleaseType)` | `analyticalMember.SetReleaseType(start, releaseType)` | Void |
| `ElementId Split(Double)` | `analyticalMember.Split(parameter)` | ElementId |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

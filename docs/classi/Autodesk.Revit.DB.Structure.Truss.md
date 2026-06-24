---
title: Truss
classe: Autodesk.Revit.DB.Structure.Truss
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# Truss

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `CurveArray Curves { get; }` | `truss.Curves` | CurveArray |
| `ICollection<ElementId> Members { get; }` | `truss.Members` | ICollection<ElementId> |
| `TrussType TrussType { get; set; }` | `truss.TrussType` | TrussType |
| `Void AttachChord(Element, TrussChordLocation, Boolean)` | `truss.AttachChord(attachToElement, location, forceRemoveSketch)` | Void |
| `Truss Create(Document, ElementId, ElementId, Curve)` | `Truss.Create(document, trussTypeId, sketchPlaneId, curve)` | Truss |
| `Void DetachChord(TrussChordLocation)` | `truss.DetachChord(location)` | Void |
| `Void DropTruss(Truss)` | `Truss.DropTruss(truss)` | Void |
| `TrussMemberInfo GetTrussMemberInfo(ElementId)` | `truss.GetTrussMemberInfo(elemId)` | TrussMemberInfo |
| `Void RemoveProfile()` | `truss.RemoveProfile()` | Void |
| `Void SetProfile(CurveArray, CurveArray)` | `truss.SetProfile(topChords, bottomChords)` | Void |
| `Void TogglePinMember(ElementId)` | `truss.TogglePinMember(elemId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

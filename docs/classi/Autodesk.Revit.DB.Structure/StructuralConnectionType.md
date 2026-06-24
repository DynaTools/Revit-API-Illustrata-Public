---
title: StructuralConnectionType
classe: Autodesk.Revit.DB.Structure.StructuralConnectionType
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# StructuralConnectionType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `StructuralConnectionApplyTo ApplyTo { get; }` | `structuralConnectionType.ApplyTo` | StructuralConnectionApplyTo |
| `StructuralConnectionType Create(Document, StructuralConnectionApplyTo, String, ElementId)` | `StructuralConnectionType.Create(doc, applyTo, name, familySymbolId)` | StructuralConnectionType |
| `Void GetAllStructuralConnectionTypeIds(Document, ICollection<ElementId>&)` | `StructuralConnectionType.GetAllStructuralConnectionTypeIds(cda, ids)` | Void |
| `ElementId GetFamilySymbolId()` | `structuralConnectionType.GetFamilySymbolId()` | ElementId |
| `Void SetFamilySymbolId(ElementId)` | `structuralConnectionType.SetFamilySymbolId(familySymbolId)` | Void |
| `Boolean ValidFamilySymbolId(Document, StructuralConnectionApplyTo, ElementId)` | `StructuralConnectionType.ValidFamilySymbolId(doc, applyTo, familySymbolId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

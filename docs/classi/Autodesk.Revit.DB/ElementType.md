---
title: ElementType
classe: Autodesk.Revit.DB.ElementType
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# ElementType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean CanBeCopied { get; }` | `elementType.CanBeCopied` | Boolean |
| `Boolean CanBeDeleted { get; }` | `elementType.CanBeDeleted` | Boolean |
| `Boolean CanBeRenamed { get; }` | `elementType.CanBeRenamed` | Boolean |
| `String FamilyName { get; }` | `elementType.FamilyName` | String |
| `String Name { get; set; }` | `elementType.Name` | String |
| `ElementType Duplicate(String)` | `elementType.Duplicate(name)` | ElementType |
| `ICollection<ElementId> GetSimilarTypes()` | `elementType.GetSimilarTypes()` | ICollection<ElementId> |
| `Boolean IsSimilarType(ElementId)` | `elementType.IsSimilarType(typeId)` | Boolean |
| `Boolean IsValidDefaultFamilyType(ElementId)` | `elementType.IsValidDefaultFamilyType(familyCategoryId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

---
title: Group
classe: Autodesk.Revit.DB.Group
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# Group

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId AttachedParentId { get; }` | `group.AttachedParentId` | ElementId |
| `GroupType GroupType { get; set; }` | `group.GroupType` | GroupType |
| `Boolean IsAttached { get; }` | `group.IsAttached` | Boolean |
| `Location Location { get; }` | `group.Location` | Location |
| `ISet<ElementId> GetAvailableAttachedDetailGroupTypeIds()` | `group.GetAvailableAttachedDetailGroupTypeIds()` | ISet<ElementId> |
| `IList<ElementId> GetMemberIds()` | `group.GetMemberIds()` | IList<ElementId> |
| `ISet<ElementId> GetShownAttachedDetailGroupTypeIds(View)` | `group.GetShownAttachedDetailGroupTypeIds(view)` | ISet<ElementId> |
| `Void HideAllAttachedDetailGroups(View)` | `group.HideAllAttachedDetailGroups(view)` | Void |
| `Void HideAttachedDetailGroups(View, ElementId)` | `group.HideAttachedDetailGroups(view, detailGroupTypeId)` | Void |
| `Boolean IsCompatibleAttachedDetailGroupType(View, ElementId)` | `group.IsCompatibleAttachedDetailGroupType(view, detailGroupTypeId)` | Boolean |
| `Void ShowAllAttachedDetailGroups(View)` | `group.ShowAllAttachedDetailGroups(view)` | Void |
| `Void ShowAttachedDetailGroups(View, ElementId)` | `group.ShowAttachedDetailGroups(view, detailGroupTypeId)` | Void |
| `ICollection<ElementId> UngroupMembers()` | `group.UngroupMembers()` | ICollection<ElementId> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

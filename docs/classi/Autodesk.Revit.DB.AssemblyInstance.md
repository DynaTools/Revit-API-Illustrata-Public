---
title: AssemblyInstance
classe: Autodesk.Revit.DB.AssemblyInstance
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 19
---

# AssemblyInstance

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `String AssemblyTypeName { get; set; }` | `assemblyInstance.AssemblyTypeName` | String |
| `Location Location { get; }` | `assemblyInstance.Location` | Location |
| `ElementId NamingCategoryId { get; set; }` | `assemblyInstance.NamingCategoryId` | ElementId |
| `Void AddMemberIds(ICollection<ElementId>)` | `assemblyInstance.AddMemberIds(memberIds)` | Void |
| `Boolean AllowsAssemblyViewCreation()` | `assemblyInstance.AllowsAssemblyViewCreation()` | Boolean |
| `Boolean AreElementsValidForAssembly(Document, ICollection<ElementId>, ElementId)` | `AssemblyInstance.AreElementsValidForAssembly(document, assemblyMemberIds, assemblyId)` | Boolean |
| `Boolean CanRemoveElementsFromAssembly(AssemblyInstance, ICollection<ElementId>)` | `AssemblyInstance.CanRemoveElementsFromAssembly(assemblyInstance, memberIds)` | Boolean |
| `AssemblyDifference CompareAssemblyInstances(AssemblyInstance, AssemblyInstance)` | `AssemblyInstance.CompareAssemblyInstances(instance1, instance2)` | AssemblyDifference |
| `AssemblyInstance Create(Document, ICollection<ElementId>, ElementId)` | `AssemblyInstance.Create(document, assemblyMemberIds, namingCategoryId)` | AssemblyInstance |
| `ICollection<ElementId> Disassemble()` | `assemblyInstance.Disassemble()` | ICollection<ElementId> |
| `XYZ GetCenter()` | `assemblyInstance.GetCenter()` | XYZ |
| `ICollection<ElementId> GetMemberIds()` | `assemblyInstance.GetMemberIds()` | ICollection<ElementId> |
| `Transform GetTransform()` | `assemblyInstance.GetTransform()` | Transform |
| `Boolean IsMember(ElementId)` | `assemblyInstance.IsMember(id)` | Boolean |
| `Boolean IsValidNamingCategory(Document, ElementId, ICollection<ElementId>)` | `AssemblyInstance.IsValidNamingCategory(document, namingCategoryId, assemblyMemberIds)` | Boolean |
| `AssemblyInstance PlaceInstance(Document, ElementId, XYZ)` | `AssemblyInstance.PlaceInstance(document, assemblyTypeId, location)` | AssemblyInstance |
| `Void RemoveMemberIds(ICollection<ElementId>)` | `assemblyInstance.RemoveMemberIds(memberIds)` | Void |
| `Void SetMemberIds(ICollection<ElementId>)` | `assemblyInstance.SetMemberIds(memberIds)` | Void |
| `Void SetTransform(Transform)` | `assemblyInstance.SetTransform(trf)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

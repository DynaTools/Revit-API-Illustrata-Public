---
title: MEPSystem
classe: Autodesk.Revit.DB.MEPSystem
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 21
---

# MEPSystem

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `FamilyInstance BaseEquipment { get; }` | `mEPSystem.BaseEquipment` | FamilyInstance |
| `Connector BaseEquipmentConnector { get; }` | `mEPSystem.BaseEquipmentConnector` | Connector |
| `ConnectorManager ConnectorManager { get; }` | `mEPSystem.ConnectorManager` | ConnectorManager |
| `ElementSet Elements { get; }` | `mEPSystem.Elements` | ElementSet |
| `Boolean HasDesignParts { get; }` | `mEPSystem.HasDesignParts` | Boolean |
| `Boolean HasFabricationParts { get; }` | `mEPSystem.HasFabricationParts` | Boolean |
| `Boolean HasPlaceholders { get; }` | `mEPSystem.HasPlaceholders` | Boolean |
| `Boolean IsEmpty { get; }` | `mEPSystem.IsEmpty` | Boolean |
| `Boolean IsMultipleNetwork { get; }` | `mEPSystem.IsMultipleNetwork` | Boolean |
| `Boolean IsValid { get; }` | `mEPSystem.IsValid` | Boolean |
| `Double PressureLossOfCriticalPath { get; }` | `mEPSystem.PressureLossOfCriticalPath` | Double |
| `Int32 SectionsCount { get; }` | `mEPSystem.SectionsCount` | Int32 |
| `Void Add(ConnectorSet)` | `mEPSystem.Add(connectors)` | Void |
| `ICollection<ElementId> DivideSystem(Document)` | `mEPSystem.DivideSystem(ADoc)` | ICollection<ElementId> |
| `IList<Int32> GetCriticalPathSectionNumbers()` | `mEPSystem.GetCriticalPathSectionNumbers()` | IList<Int32> |
| `Int32 GetPhysicalNetworksNumber()` | `mEPSystem.GetPhysicalNetworksNumber()` | Int32 |
| `MEPSection GetSectionByIndex(Int32)` | `mEPSystem.GetSectionByIndex(index)` | MEPSection |
| `MEPSection GetSectionByNumber(Int32)` | `mEPSystem.GetSectionByNumber(sectionNumber)` | MEPSection |
| `Boolean IsSystemDividable()` | `mEPSystem.IsSystemDividable()` | Boolean |
| `Void Remove(ICollection<ElementId>)` | `mEPSystem.Remove(elementIds)` | Void |
| `Void Remove(ConnectorSet)` | `mEPSystem.Remove(connectors)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

---
title: ElectricalSystem
classe: Autodesk.Revit.DB.Electrical.ElectricalSystem
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.MEPSystem
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 59
---

# ElectricalSystem

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double ApparentCurrent { get; }` | `electricalSystem.ApparentCurrent` | Double |
| `Double ApparentCurrentPhaseA { get; }` | `electricalSystem.ApparentCurrentPhaseA` | Double |
| `Double ApparentCurrentPhaseB { get; }` | `electricalSystem.ApparentCurrentPhaseB` | Double |
| `Double ApparentCurrentPhaseC { get; }` | `electricalSystem.ApparentCurrentPhaseC` | Double |
| `Double ApparentLoad { get; }` | `electricalSystem.ApparentLoad` | Double |
| `Double ApparentLoadPhaseA { get; }` | `electricalSystem.ApparentLoadPhaseA` | Double |
| `Double ApparentLoadPhaseB { get; }` | `electricalSystem.ApparentLoadPhaseB` | Double |
| `Double ApparentLoadPhaseC { get; }` | `electricalSystem.ApparentLoadPhaseC` | Double |
| `Boolean BalancedLoad { get; }` | `electricalSystem.BalancedLoad` | Boolean |
| `CircuitConnectionType CircuitConnectionType { get; set; }` | `electricalSystem.CircuitConnectionType` | CircuitConnectionType |
| `Int32 CircuitNamingIndex { get; }` | `electricalSystem.CircuitNamingIndex` | Int32 |
| `String CircuitNumber { get; }` | `electricalSystem.CircuitNumber` | String |
| `ElectricalCircuitPathMode CircuitPathMode { get; set; }` | `electricalSystem.CircuitPathMode` | ElectricalCircuitPathMode |
| `CircuitType CircuitType { get; }` | `electricalSystem.CircuitType` | CircuitType |
| `Double Frame { get; set; }` | `electricalSystem.Frame` | Double |
| `Int32 GroundConductorsNumber { get; }` | `electricalSystem.GroundConductorsNumber` | Int32 |
| `Boolean HasCustomCircuitPath { get; }` | `electricalSystem.HasCustomCircuitPath` | Boolean |
| `Boolean HasPathOffset { get; }` | `electricalSystem.HasPathOffset` | Boolean |
| `Int32 HotConductorsNumber { get; }` | `electricalSystem.HotConductorsNumber` | Int32 |
| `Boolean IsBasePanelFeedThroughLugsOccupied { get; }` | `electricalSystem.IsBasePanelFeedThroughLugsOccupied` | Boolean |
| `Double Length { get; }` | `electricalSystem.Length` | Double |
| `String LoadClassificationAbbreviations { get; }` | `electricalSystem.LoadClassificationAbbreviations` | String |
| `String LoadClassifications { get; }` | `electricalSystem.LoadClassifications` | String |
| `String LoadName { get; set; }` | `electricalSystem.LoadName` | String |
| `Int32 NeutralConductorsNumber { get; set; }` | `electricalSystem.NeutralConductorsNumber` | Int32 |
| `String PanelName { get; }` | `electricalSystem.PanelName` | String |
| `Double PathOffset { get; set; }` | `electricalSystem.PathOffset` | Double |
| `String PhaseLabel { get; }` | `electricalSystem.PhaseLabel` | String |
| `Int32 PolesNumber { get; }` | `electricalSystem.PolesNumber` | Int32 |
| `Double PowerFactor { get; }` | `electricalSystem.PowerFactor` | Double |
| `PowerFactorStateType PowerFactorState { get; }` | `electricalSystem.PowerFactorState` | PowerFactorStateType |
| `Double Rating { get; set; }` | `electricalSystem.Rating` | Double |
| `Int32 RunsNumber { get; }` | `electricalSystem.RunsNumber` | Int32 |
| `String SlotIndex { get; }` | `electricalSystem.SlotIndex` | String |
| `Int32 StartSlot { get; }` | `electricalSystem.StartSlot` | Int32 |
| `ElectricalSystemType SystemType { get; }` | `electricalSystem.SystemType` | ElectricalSystemType |
| `Double TrueCurrent { get; }` | `electricalSystem.TrueCurrent` | Double |
| `Double TrueCurrentPhaseA { get; }` | `electricalSystem.TrueCurrentPhaseA` | Double |
| `Double TrueCurrentPhaseB { get; }` | `electricalSystem.TrueCurrentPhaseB` | Double |
| `Double TrueCurrentPhaseC { get; }` | `electricalSystem.TrueCurrentPhaseC` | Double |
| `Double TrueLoad { get; set; }` | `electricalSystem.TrueLoad` | Double |
| `Double TrueLoadPhaseA { get; }` | `electricalSystem.TrueLoadPhaseA` | Double |
| `Double TrueLoadPhaseB { get; }` | `electricalSystem.TrueLoadPhaseB` | Double |
| `Double TrueLoadPhaseC { get; }` | `electricalSystem.TrueLoadPhaseC` | Double |
| `Double Voltage { get; }` | `electricalSystem.Voltage` | Double |
| `Double VoltageDrop { get; }` | `electricalSystem.VoltageDrop` | Double |
| `Int32 Ways { get; }` | `electricalSystem.Ways` | Int32 |
| `String WireSizeString { get; }` | `electricalSystem.WireSizeString` | String |
| `WireType WireType { get; set; }` | `electricalSystem.WireType` | WireType |
| `Boolean AddToCircuit(ElementSet)` | `electricalSystem.AddToCircuit(components)` | Boolean |
| `ElectricalSystem Create(Connector, ElectricalSystemType)` | `ElectricalSystem.Create(connector, elecSysType)` | ElectricalSystem |
| `ElectricalSystem Create(Document, IList<ElementId>, ElectricalSystemType)` | `ElectricalSystem.Create(document, electComponents, elecSysType)` | ElectricalSystem |
| `Void DisconnectPanel()` | `electricalSystem.DisconnectPanel()` | Void |
| `IList<XYZ> GetCircuitPath()` | `electricalSystem.GetCircuitPath()` | IList<XYZ> |
| `Boolean IsCircuitPathValid(IList<XYZ>)` | `electricalSystem.IsCircuitPathValid(nodes)` | Boolean |
| `WireSet NewWires(View, WiringType)` | `electricalSystem.NewWires(view, wiringType)` | WireSet |
| `Void RemoveFromCircuit(ElementSet)` | `electricalSystem.RemoveFromCircuit(components)` | Void |
| `Void SelectPanel(FamilyInstance)` | `electricalSystem.SelectPanel(panel)` | Void |
| `Void SetCircuitPath(IList<XYZ>)` | `electricalSystem.SetCircuitPath(nodes)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

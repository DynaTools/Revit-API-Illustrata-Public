---
title: PanelScheduleView
classe: Autodesk.Revit.DB.Electrical.PanelScheduleView
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.TableView
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 44
---

# PanelScheduleView

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Void AddSpace(Int32, Int32)` | `panelScheduleView.AddSpace(nRow, nCol)` | Void |
| `Void AddSpare(Int32, Int32)` | `panelScheduleView.AddSpare(nRow, nCol)` | Void |
| `Boolean CanMoveSlotTo(Int32, Int32, Int32, Int32)` | `panelScheduleView.CanMoveSlotTo(nMovingRow, nMovingCol, nToRow, nToCol)` | Boolean |
| `PanelScheduleView CreateInstanceView(Document, ElementId, ElementId)` | `PanelScheduleView.CreateInstanceView(ADoc, templateId, panelId)` | PanelScheduleView |
| `PanelScheduleView CreateInstanceView(Document, ElementId)` | `PanelScheduleView.CreateInstanceView(ADoc, panelId)` | PanelScheduleView |
| `Void GenerateInstanceFromTemplate(ElementId)` | `panelScheduleView.GenerateInstanceFromTemplate(templateId)` | Void |
| `Double GetApparentPhaseValue(ElementId, ElementId)` | `panelScheduleView.GetApparentPhaseValue(circuitId, apparentLoadParam)` | Double |
| `Void GetCellsBySlotNumber(Int32, IList<Int32>&, IList<Int32>&)` | `panelScheduleView.GetCellsBySlotNumber(nSlotNumber, RowArr, ColArr)` | Void |
| `ElectricalSystem GetCircuitByCell(Int32, Int32)` | `panelScheduleView.GetCircuitByCell(nRow, nCol)` | ElectricalSystem |
| `ElementId GetCircuitIdByCell(Int32, Int32)` | `panelScheduleView.GetCircuitIdByCell(nRow, nCol)` | ElementId |
| `String GetCombinedParamValue(SectionType, Int32, Int32)` | `panelScheduleView.GetCombinedParamValue(sectionType, nRow, nCol)` | String |
| `String GetLoadClassificationConnectedCurrent(Int32, Int32)` | `panelScheduleView.GetLoadClassificationConnectedCurrent(nRow, nCol)` | String |
| `String GetLoadClassificationConnectedLoad(Int32, Int32)` | `panelScheduleView.GetLoadClassificationConnectedLoad(nRow, nCol)` | String |
| `String GetLoadClassificationDemandCurrent(Int32, Int32)` | `panelScheduleView.GetLoadClassificationDemandCurrent(nRow, nCol)` | String |
| `String GetLoadClassificationDemandFactor(Int32, Int32)` | `panelScheduleView.GetLoadClassificationDemandFactor(nRow, nCol)` | String |
| `String GetLoadClassificationDemandLoad(Int32, Int32)` | `panelScheduleView.GetLoadClassificationDemandLoad(nRow, nCol)` | String |
| `ElementId GetLoadClassificationId(Int32)` | `panelScheduleView.GetLoadClassificationId(nRow)` | ElementId |
| `String GetLoadClassificationName(Int32, Int32)` | `panelScheduleView.GetLoadClassificationName(nRow, nCol)` | String |
| `String GetLoadClassificationParamValue(ElementId, Int32, Int32)` | `panelScheduleView.GetLoadClassificationParamValue(parameterId, nRow, nCol)` | String |
| `ElementId GetPanel()` | `panelScheduleView.GetPanel()` | ElementId |
| `String GetParamValue(SectionType, Int32, Int32)` | `panelScheduleView.GetParamValue(sectionType, nRow, nCol)` | String |
| `TableSectionData GetSectionData(SectionType)` | `panelScheduleView.GetSectionData(sectionType)` | TableSectionData |
| `Int32 GetSlotNumberByCell(Int32, Int32)` | `panelScheduleView.GetSlotNumberByCell(nRow, nCol)` | Int32 |
| `Double GetSpareCurrentValue(Int32, Int32, ElementId)` | `panelScheduleView.GetSpareCurrentValue(row, column, idCurrentParameter)` | Double |
| `Double GetSpareLoadValue(Int32, Int32, ElementId)` | `panelScheduleView.GetSpareLoadValue(row, column, idLoadParameter)` | Double |
| `PanelScheduleData GetTableData()` | `panelScheduleView.GetTableData()` | PanelScheduleData |
| `ElementId GetTemplate()` | `panelScheduleView.GetTemplate()` | ElementId |
| `Boolean IsCellInPhaseLoads(Int32, Int32)` | `panelScheduleView.IsCellInPhaseLoads(nRow, nCol)` | Boolean |
| `Boolean IsColumnInLoadSummary(Int32)` | `panelScheduleView.IsColumnInLoadSummary(nCol)` | Boolean |
| `Boolean IsPanelScheduleTemplate()` | `panelScheduleView.IsPanelScheduleTemplate()` | Boolean |
| `Boolean IsRowInCircuitTable(Int32)` | `panelScheduleView.IsRowInCircuitTable(nRow)` | Boolean |
| `Int32 IsSlotGrouped(Int32, Int32)` | `panelScheduleView.IsSlotGrouped(nRow, nCol)` | Int32 |
| `Boolean IsSlotLocked(Int32, Int32)` | `panelScheduleView.IsSlotLocked(nRow, nCol)` | Boolean |
| `Boolean IsSpace(Int32, Int32)` | `panelScheduleView.IsSpace(nRow, nCol)` | Boolean |
| `Boolean IsSpare(Int32, Int32)` | `panelScheduleView.IsSpare(nRow, nCol)` | Boolean |
| `Void MoveSlotTo(Int32, Int32, Int32, Int32)` | `panelScheduleView.MoveSlotTo(nMovingRow, nMovingCol, nToRow, nToCol)` | Void |
| `Void RemoveSpace(Int32, Int32)` | `panelScheduleView.RemoveSpace(nRow, nCol)` | Void |
| `Void RemoveSpare(Int32, Int32)` | `panelScheduleView.RemoveSpare(nRow, nCol)` | Void |
| `Void RenumberIndexes()` | `panelScheduleView.RenumberIndexes()` | Void |
| `Void SetLockSlot(Int32, Int32, Boolean)` | `panelScheduleView.SetLockSlot(nRow, nCol, bLock)` | Void |
| `Boolean SetParamValue(SectionType, Int32, Int32, String)` | `panelScheduleView.SetParamValue(sectionType, nRow, nCol, sValue)` | Boolean |
| `Void SetSpareCurrentValue(Int32, Int32, ElementId, Double)` | `panelScheduleView.SetSpareCurrentValue(row, column, idCurrentParameter, value)` | Void |
| `Void SetSpareLoadValue(Int32, Int32, ElementId, Double)` | `panelScheduleView.SetSpareLoadValue(row, column, idLoadParameter, value)` | Void |
| `Void SwitchPhases(Int32, Int32)` | `panelScheduleView.SwitchPhases(nRow, nCol)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

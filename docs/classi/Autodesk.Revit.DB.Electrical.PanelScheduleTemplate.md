---
title: PanelScheduleTemplate
classe: Autodesk.Revit.DB.Electrical.PanelScheduleTemplate
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# PanelScheduleTemplate

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsBranchPanelSchedule { get; }` | `panelScheduleTemplate.IsBranchPanelSchedule` | Boolean |
| `Boolean IsDataPanelSchedule { get; }` | `panelScheduleTemplate.IsDataPanelSchedule` | Boolean |
| `Boolean IsDefault { get; }` | `panelScheduleTemplate.IsDefault` | Boolean |
| `Boolean IsSwitchboardSchedule { get; }` | `panelScheduleTemplate.IsSwitchboardSchedule` | Boolean |
| `Void CopyFrom(Document, PanelScheduleTemplate)` | `panelScheduleTemplate.CopyFrom(OtherADoc, otherElem)` | Void |
| `PanelScheduleTemplate Create(Document, PanelScheduleType, PanelConfiguration, String)` | `PanelScheduleTemplate.Create(document, type, config, strName)` | PanelScheduleTemplate |
| `PanelScheduleType GetPanelScheduleType()` | `panelScheduleTemplate.GetPanelScheduleType()` | PanelScheduleType |
| `TableSectionData GetSectionData(SectionType)` | `panelScheduleTemplate.GetSectionData(sectionType)` | TableSectionData |
| `PanelScheduleData GetTableData()` | `panelScheduleTemplate.GetTableData()` | PanelScheduleData |
| `Boolean HasSameType(PanelScheduleTemplate)` | `panelScheduleTemplate.HasSameType(otherTemplate)` | Boolean |
| `Boolean IsValidPanelConfiguration(PanelScheduleType, PanelConfiguration)` | `PanelScheduleTemplate.IsValidPanelConfiguration(scheduleType, configuration)` | Boolean |
| `Boolean IsValidType(PanelScheduleType)` | `PanelScheduleTemplate.IsValidType(panelScheduleType)` | Boolean |
| `Void SetTableData(PanelScheduleData)` | `panelScheduleTemplate.SetTableData(Data)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

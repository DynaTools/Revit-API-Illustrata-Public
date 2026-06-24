---
title: PanelScheduleData
classe: Autodesk.Revit.DB.Electrical.PanelScheduleData
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.TableData
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 33
---

# PanelScheduleData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean BodyShowsVerticalHeaders { get; }` | `panelScheduleData.BodyShowsVerticalHeaders` | Boolean |
| `ElementId BorderAroundSchedule { get; }` | `panelScheduleData.BorderAroundSchedule` | ElementId |
| `ElementId BorderAroundSections { get; }` | `panelScheduleData.BorderAroundSections` | ElementId |
| `Boolean IsAutoShadingForLoadDisplay { get; set; }` | `panelScheduleData.IsAutoShadingForLoadDisplay` | Boolean |
| `Boolean IsFooterSectionHidden { get; }` | `panelScheduleData.IsFooterSectionHidden` | Boolean |
| `Boolean IsHeaderSectionHidden { get; }` | `panelScheduleData.IsHeaderSectionHidden` | Boolean |
| `Boolean IsPanelSinglePhase { get; set; }` | `panelScheduleData.IsPanelSinglePhase` | Boolean |
| `Boolean IsSummarySectionHidden { get; }` | `panelScheduleData.IsSummarySectionHidden` | Boolean |
| `Boolean IsUnusedPhaseHidden { get; set; }` | `panelScheduleData.IsUnusedPhaseHidden` | Boolean |
| `Int32 NumberOfSlots { get; }` | `panelScheduleData.NumberOfSlots` | Int32 |
| `PanelConfiguration PanelConfiguration { get; }` | `panelScheduleData.PanelConfiguration` | PanelConfiguration |
| `PanelSchedulePhaseLoadType PhaseLoadType { get; }` | `panelScheduleData.PhaseLoadType` | PanelSchedulePhaseLoadType |
| `Boolean PhasesAsCurrents { get; }` | `panelScheduleData.PhasesAsCurrents` | Boolean |
| `PanelScheduleType ScheduleType { get; }` | `panelScheduleData.ScheduleType` | PanelScheduleType |
| `Boolean ShowCircuitNumberOnOneRowForMultiphaseCircuits { get; set; }` | `panelScheduleData.ShowCircuitNumberOnOneRowForMultiphaseCircuits` | Boolean |
| `Boolean ShowMultipleRowsForMultiphaseCircuits { get; set; }` | `panelScheduleData.ShowMultipleRowsForMultiphaseCircuits` | Boolean |
| `Boolean ShowSlotFromDeviceInsteadOfTemplate { get; set; }` | `panelScheduleData.ShowSlotFromDeviceInsteadOfTemplate` | Boolean |
| `Boolean SummaryShowsGroups { get; set; }` | `panelScheduleData.SummaryShowsGroups` | Boolean |
| `Boolean SummaryShowsOnlyConnectedLoads { get; set; }` | `panelScheduleData.SummaryShowsOnlyConnectedLoads` | Boolean |
| `Boolean SummaryShowsVerticalHeaders { get; }` | `panelScheduleData.SummaryShowsVerticalHeaders` | Boolean |
| `Boolean AddLoadClassification(ElementId)` | `panelScheduleData.AddLoadClassification(loadClassficationId)` | Boolean |
| `IList<ElementId> GetLoadClassifications()` | `panelScheduleData.GetLoadClassifications()` | IList<ElementId> |
| `Int32 GetNumberOfCircuitRows()` | `panelScheduleData.GetNumberOfCircuitRows()` | Int32 |
| `Boolean IsSymmetric()` | `panelScheduleData.IsSymmetric()` | Boolean |
| `Void RemoveLoadClassification(Int32)` | `panelScheduleData.RemoveLoadClassification(nIndex)` | Void |
| `Void SetBorderAroundSchedule(ElementId)` | `panelScheduleData.SetBorderAroundSchedule(borderId)` | Void |
| `Void SetBorderAroundSections(ElementId)` | `panelScheduleData.SetBorderAroundSections(borderId)` | Void |
| `Void SetLoadClassifications(IList<ElementId>)` | `panelScheduleData.SetLoadClassifications(loadClassificaions)` | Void |
| `Void UpdateCircuitTableForInstance(FamilyInstance)` | `panelScheduleData.UpdateCircuitTableForInstance(pPanel)` | Void |
| `Void UpdateCircuitTableForTemplate(PanelSchedulePhaseLoadType, Int32, Boolean)` | `panelScheduleData.UpdateCircuitTableForTemplate(newType, nNumSlots, bPhasesAsCurrents)` | Void |
| `Void UpdateIsSectionHidden(SectionType, Boolean)` | `panelScheduleData.UpdateIsSectionHidden(sectionType, bHide)` | Void |
| `Void UpdateLoadSummary()` | `panelScheduleData.UpdateLoadSummary()` | Void |
| `Void UpdateVerticalHeadersInSection(SectionType, Boolean)` | `panelScheduleData.UpdateVerticalHeadersInSection(sectionType, bVertical)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

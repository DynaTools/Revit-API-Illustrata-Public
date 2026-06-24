---
title: CurtainGrid
classe: Autodesk.Revit.DB.CurtainGrid
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 20
---

# CurtainGrid

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double Grid1Angle { get; set; }` | `curtainGrid.Grid1Angle` | Double |
| `CurtainGridAlignType Grid1Justification { get; set; }` | `curtainGrid.Grid1Justification` | CurtainGridAlignType |
| `Double Grid1Offset { get; set; }` | `curtainGrid.Grid1Offset` | Double |
| `Double Grid2Angle { get; set; }` | `curtainGrid.Grid2Angle` | Double |
| `CurtainGridAlignType Grid2Justification { get; set; }` | `curtainGrid.Grid2Justification` | CurtainGridAlignType |
| `Double Grid2Offset { get; set; }` | `curtainGrid.Grid2Offset` | Double |
| `Int32 NumPanels { get; }` | `curtainGrid.NumPanels` | Int32 |
| `Int32 NumULines { get; }` | `curtainGrid.NumULines` | Int32 |
| `Int32 NumVLines { get; }` | `curtainGrid.NumVLines` | Int32 |
| `CurtainGridLine AddGridLine(Boolean, XYZ, Boolean)` | `curtainGrid.AddGridLine(isUGridLine, position, oneSegmentOnly)` | CurtainGridLine |
| `Element ChangePanelType(Element, ElementType)` | `curtainGrid.ChangePanelType(panel, newSymbol)` | Element |
| `CurtainCell GetCell(ElementId, ElementId)` | `curtainGrid.GetCell(uGridLineId, vGridLineId)` | CurtainCell |
| `ICollection<CurtainCell> GetCurtainCells()` | `curtainGrid.GetCurtainCells()` | ICollection<CurtainCell> |
| `ICollection<ElementId> GetMullionIds()` | `curtainGrid.GetMullionIds()` | ICollection<ElementId> |
| `Panel GetPanel(ElementId, ElementId)` | `curtainGrid.GetPanel(uGridLineId, vGridLineId)` | Panel |
| `ICollection<ElementId> GetPanelIds()` | `curtainGrid.GetPanelIds()` | ICollection<ElementId> |
| `ICollection<ElementId> GetUGridLineIds()` | `curtainGrid.GetUGridLineIds()` | ICollection<ElementId> |
| `ICollection<ElementId> GetUnlockedMullionIds()` | `curtainGrid.GetUnlockedMullionIds()` | ICollection<ElementId> |
| `ICollection<ElementId> GetUnlockedPanelIds()` | `curtainGrid.GetUnlockedPanelIds()` | ICollection<ElementId> |
| `ICollection<ElementId> GetVGridLineIds()` | `curtainGrid.GetVGridLineIds()` | ICollection<ElementId> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

---
title: TableView
classe: Autodesk.Revit.DB.TableView
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.View
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# TableView

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 MaximumColumnWidth { get; }` | `tableView.MaximumColumnWidth` | Int32 |
| `Int32 MaximumGridWidth { get; }` | `tableView.MaximumGridWidth` | Int32 |
| `Int32 MaximumRowHeight { get; }` | `tableView.MaximumRowHeight` | Int32 |
| `Int32 MinimumColumnWidth { get; }` | `tableView.MinimumColumnWidth` | Int32 |
| `Int32 MinimumRowHeight { get; }` | `tableView.MinimumRowHeight` | Int32 |
| `ElementId TargetId { get; set; }` | `tableView.TargetId` | ElementId |
| `IList<ElementId> GetAvailableParameterCategories(SectionType, Int32)` | `tableView.GetAvailableParameterCategories(sectionType, row)` | IList<ElementId> |
| `IList<ElementId> GetAvailableParameters(Document, ElementId)` | `TableView.GetAvailableParameters(cda, categoryId)` | IList<ElementId> |
| `String GetCalculatedValueName(SectionType, Int32, Int32)` | `tableView.GetCalculatedValueName(sectionType, row, column)` | String |
| `String GetCalculatedValueText(SectionType, Int32, Int32)` | `tableView.GetCalculatedValueText(sectionType, row, column)` | String |
| `String GetCellText(SectionType, Int32, Int32)` | `tableView.GetCellText(sectionType, row, column)` | String |
| `Boolean IsValidSectionType(SectionType)` | `tableView.IsValidSectionType(sectionType)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

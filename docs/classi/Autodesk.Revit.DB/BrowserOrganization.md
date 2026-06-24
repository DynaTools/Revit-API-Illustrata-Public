---
title: BrowserOrganization
classe: Autodesk.Revit.DB.BrowserOrganization
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# BrowserOrganization

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `SortingOrder SortingOrder { get; }` | `browserOrganization.SortingOrder` | SortingOrder |
| `ElementId SortingParameterId { get; }` | `browserOrganization.SortingParameterId` | ElementId |
| `BrowserOrganizationType Type { get; }` | `browserOrganization.Type` | BrowserOrganizationType |
| `Boolean AreFiltersSatisfied(ElementId)` | `browserOrganization.AreFiltersSatisfied(elementId)` | Boolean |
| `BrowserOrganization GetCurrentBrowserOrganizationForSchedules(Document)` | `BrowserOrganization.GetCurrentBrowserOrganizationForSchedules(document)` | BrowserOrganization |
| `BrowserOrganization GetCurrentBrowserOrganizationForSheets(Document)` | `BrowserOrganization.GetCurrentBrowserOrganizationForSheets(document)` | BrowserOrganization |
| `BrowserOrganization GetCurrentBrowserOrganizationForViews(Document)` | `BrowserOrganization.GetCurrentBrowserOrganizationForViews(document)` | BrowserOrganization |
| `IList<FolderItemInfo> GetFolderItems(ElementId)` | `browserOrganization.GetFolderItems(elementId)` | IList<FolderItemInfo> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

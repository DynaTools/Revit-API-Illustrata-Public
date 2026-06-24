---
title: ProjectLocation
classe: Autodesk.Revit.DB.ProjectLocation
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Instance
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# ProjectLocation

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ProjectLocation Create(Document, ElementId, String)` | `ProjectLocation.Create(document, siteLocationId, name)` | ProjectLocation |
| `ProjectLocation Duplicate(String)` | `projectLocation.Duplicate(name)` | ProjectLocation |
| `ProjectPosition GetProjectPosition(XYZ)` | `projectLocation.GetProjectPosition(point)` | ProjectPosition |
| `SiteLocation GetSiteLocation()` | `projectLocation.GetSiteLocation()` | SiteLocation |
| `Boolean IsProjectLocationNameUnique(Document, String, ElementId)` | `ProjectLocation.IsProjectLocationNameUnique(document, name, siteLocationId)` | Boolean |
| `Void SetProjectPosition(XYZ, ProjectPosition)` | `projectLocation.SetProjectPosition(point, position)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

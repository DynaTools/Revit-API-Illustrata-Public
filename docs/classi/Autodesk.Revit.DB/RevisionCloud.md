---
title: RevisionCloud
classe: Autodesk.Revit.DB.RevisionCloud
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# RevisionCloud

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId RevisionId { get; set; }` | `revisionCloud.RevisionId` | ElementId |
| `RevisionCloud Create(Document, View, ElementId, IList<Curve>)` | `RevisionCloud.Create(document, view, revisionId, curves)` | RevisionCloud |
| `ISet<ElementId> GetSheetIds()` | `revisionCloud.GetSheetIds()` | ISet<ElementId> |
| `IList<Curve> GetSketchCurves()` | `revisionCloud.GetSketchCurves()` | IList<Curve> |
| `Boolean IsRevisionIssued()` | `revisionCloud.IsRevisionIssued()` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

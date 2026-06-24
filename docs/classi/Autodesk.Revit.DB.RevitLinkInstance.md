---
title: RevitLinkInstance
classe: Autodesk.Revit.DB.RevitLinkInstance
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Instance
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# RevitLinkInstance

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `RevitLinkInstance Create(Document, ElementId, ImportPlacement)` | `RevitLinkInstance.Create(document, revitLinkTypeId, placement)` | RevitLinkInstance |
| `RevitLinkInstance Create(Document, ElementId)` | `RevitLinkInstance.Create(document, revitLinkTypeId)` | RevitLinkInstance |
| `Document GetLinkDocument()` | `revitLinkInstance.GetLinkDocument()` | Document |
| `Void MoveBasePointToHostBasePoint(Boolean)` | `revitLinkInstance.MoveBasePointToHostBasePoint(resetToOriginalRotation)` | Void |
| `Void MoveOriginToHostOrigin(Boolean)` | `revitLinkInstance.MoveOriginToHostOrigin(resetToOriginalRotation)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

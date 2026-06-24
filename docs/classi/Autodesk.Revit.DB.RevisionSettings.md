---
title: RevisionSettings
classe: Autodesk.Revit.DB.RevisionSettings
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# RevisionSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double RevisionCloudSpacing { get; set; }` | `revisionSettings.RevisionCloudSpacing` | Double |
| `RevisionNumbering RevisionNumbering { get; set; }` | `revisionSettings.RevisionNumbering` | RevisionNumbering |
| `RevisionSettings GetRevisionSettings(Document)` | `RevisionSettings.GetRevisionSettings(ccda)` | RevisionSettings |
| `Boolean IsAcceptableRevisionCloudSpacing(Double)` | `revisionSettings.IsAcceptableRevisionCloudSpacing(rawValue)` | Boolean |
| `Double RoundRevisionCloudSpacing(Document, Double)` | `RevisionSettings.RoundRevisionCloudSpacing(ccda, rawValue)` | Double |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

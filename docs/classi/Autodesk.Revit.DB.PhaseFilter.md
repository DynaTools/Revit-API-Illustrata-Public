---
title: PhaseFilter
classe: Autodesk.Revit.DB.PhaseFilter
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 4
---

# PhaseFilter

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsDefault { get; }` | `phaseFilter.IsDefault` | Boolean |
| `PhaseFilter Create(Document, String)` | `PhaseFilter.Create(document, name)` | PhaseFilter |
| `PhaseStatusPresentation GetPhaseStatusPresentation(ElementOnPhaseStatus)` | `phaseFilter.GetPhaseStatusPresentation(status)` | PhaseStatusPresentation |
| `Void SetPhaseStatusPresentation(ElementOnPhaseStatus, PhaseStatusPresentation)` | `phaseFilter.SetPhaseStatusPresentation(status, presentation)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

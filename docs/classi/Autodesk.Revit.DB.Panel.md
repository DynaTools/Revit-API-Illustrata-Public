---
title: Panel
classe: Autodesk.Revit.DB.Panel
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.FamilyInstance
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# Panel

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean Lockable { get; }` | `panel.Lockable` | Boolean |
| `PanelType PanelType { get; set; }` | `panel.PanelType` | PanelType |
| `Transform Transform { get; }` | `panel.Transform` | Transform |
| `ElementId FindHostPanel()` | `panel.FindHostPanel()` | ElementId |
| `Void GetRefGridLines(ElementId&, ElementId&)` | `panel.GetRefGridLines(uGridLineId, vGridLineId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

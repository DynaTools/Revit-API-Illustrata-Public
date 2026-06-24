---
title: TemporaryGraphicsManager
classe: Autodesk.Revit.DB.TemporaryGraphicsManager
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# TemporaryGraphicsManager

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `temporaryGraphicsManager.IsValidObject` | Boolean |
| `Int32 AddControl(InCanvasControlData, ElementId)` | `temporaryGraphicsManager.AddControl(data, ownerViewId)` | Int32 |
| `Void Clear()` | `temporaryGraphicsManager.Clear()` | Void |
| `Void Dispose()` | `temporaryGraphicsManager.Dispose()` | Void |
| `ICollection<Int32> GetAll()` | `temporaryGraphicsManager.GetAll()` | ICollection<Int32> |
| `TemporaryGraphicsManager GetTemporaryGraphicsManager(Document)` | `TemporaryGraphicsManager.GetTemporaryGraphicsManager(document)` | TemporaryGraphicsManager |
| `Void RemoveControl(Int32)` | `temporaryGraphicsManager.RemoveControl(index)` | Void |
| `Void SetVisibility(Int32, Boolean)` | `temporaryGraphicsManager.SetVisibility(index, visible)` | Void |
| `Void UpdateControl(Int32, InCanvasControlData)` | `temporaryGraphicsManager.UpdateControl(index, data)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

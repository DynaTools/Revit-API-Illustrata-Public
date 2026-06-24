---
title: ViewSheetSetting
classe: Autodesk.Revit.DB.ViewSheetSetting
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 8
---

# ViewSheetSetting

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ViewSet AvailableViews { get; }` | `viewSheetSetting.AvailableViews` | ViewSet |
| `IViewSheetSet CurrentViewSheetSet { get; set; }` | `viewSheetSetting.CurrentViewSheetSet` | IViewSheetSet |
| `InSessionViewSheetSet InSession { get; }` | `viewSheetSetting.InSession` | InSessionViewSheetSet |
| `Boolean Delete()` | `viewSheetSetting.Delete()` | Boolean |
| `Boolean Rename(String)` | `viewSheetSetting.Rename(newName)` | Boolean |
| `Void Revert()` | `viewSheetSetting.Revert()` | Void |
| `Boolean Save()` | `viewSheetSetting.Save()` | Boolean |
| `Boolean SaveAs(String)` | `viewSheetSetting.SaveAs(newName)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

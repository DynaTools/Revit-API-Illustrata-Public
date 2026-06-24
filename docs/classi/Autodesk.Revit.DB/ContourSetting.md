---
title: ContourSetting
classe: Autodesk.Revit.DB.ContourSetting
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# ContourSetting

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `contourSetting.IsValidObject` | Boolean |
| `ContourSettingItem AddContourRange(Double, Double, Double, ElementId)` | `contourSetting.AddContourRange(start, stop, step, subcategoryId)` | ContourSettingItem |
| `ContourSettingItem AddSingleContour(Double, ElementId)` | `contourSetting.AddSingleContour(elevation, subcategoryId)` | ContourSettingItem |
| `Void DisableItem(ContourSettingItem)` | `contourSetting.DisableItem(item)` | Void |
| `Void Dispose()` | `contourSetting.Dispose()` | Void |
| `Void EnableItem(ContourSettingItem)` | `contourSetting.EnableItem(item)` | Void |
| `IList<ContourSettingItem> GetContourSettingItems()` | `contourSetting.GetContourSettingItems()` | IList<ContourSettingItem> |
| `Int32 GetItemIndex(ContourSettingItem)` | `contourSetting.GetItemIndex(item)` | Int32 |
| `Boolean IsItemEnabled(ContourSettingItem)` | `contourSetting.IsItemEnabled(item)` | Boolean |
| `Void RemoveItem(ContourSettingItem)` | `contourSetting.RemoveItem(item)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

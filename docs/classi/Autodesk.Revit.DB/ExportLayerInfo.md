---
title: ExportLayerInfo
classe: Autodesk.Revit.DB.ExportLayerInfo
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 18
---

# ExportLayerInfo

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `LayerCategoryType CategoryType { get; set; }` | `exportLayerInfo.CategoryType` | LayerCategoryType |
| `String ColorName { get; set; }` | `exportLayerInfo.ColorName` | String |
| `Int32 ColorNumber { get; set; }` | `exportLayerInfo.ColorNumber` | Int32 |
| `Int32 CutColorNumber { get; set; }` | `exportLayerInfo.CutColorNumber` | Int32 |
| `String CutLayerName { get; set; }` | `exportLayerInfo.CutLayerName` | String |
| `Boolean IsValidObject { get; }` | `exportLayerInfo.IsValidObject` | Boolean |
| `String LayerName { get; set; }` | `exportLayerInfo.LayerName` | String |
| `Void AddCutLayerModifier(LayerModifier)` | `exportLayerInfo.AddCutLayerModifier(layerModifier)` | Void |
| `Void AddLayerModifier(LayerModifier)` | `exportLayerInfo.AddLayerModifier(layerModifier)` | Void |
| `Void ClearCutLayerModifiers()` | `exportLayerInfo.ClearCutLayerModifiers()` | Void |
| `Void ClearLayerModifiers()` | `exportLayerInfo.ClearLayerModifiers()` | Void |
| `Void Dispose()` | `exportLayerInfo.Dispose()` | Void |
| `IList<LayerModifier> GetCutLayerModifiers()` | `exportLayerInfo.GetCutLayerModifiers()` | IList<LayerModifier> |
| `IList<LayerModifier> GetLayerModifiers()` | `exportLayerInfo.GetLayerModifiers()` | IList<LayerModifier> |
| `Void RemoveCutLayerModifier(LayerModifier)` | `exportLayerInfo.RemoveCutLayerModifier(layerModifier)` | Void |
| `Void RemoveLayerModifier(LayerModifier)` | `exportLayerInfo.RemoveLayerModifier(layerModifier)` | Void |
| `Void SetCutLayerModifiers(IList<LayerModifier>)` | `exportLayerInfo.SetCutLayerModifiers(cutLayermodifiers)` | Void |
| `Void SetLayerModifiers(IList<LayerModifier>)` | `exportLayerInfo.SetLayerModifiers(layermodifiers)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

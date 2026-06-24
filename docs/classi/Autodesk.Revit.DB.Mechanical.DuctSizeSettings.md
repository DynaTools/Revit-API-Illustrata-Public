---
title: DuctSizeSettings
classe: Autodesk.Revit.DB.Mechanical.DuctSizeSettings
namespace: Autodesk.Revit.DB.Mechanical
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# DuctSizeSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `DuctSizes Item { get; }` | `ductSizeSettings.Item` | DuctSizes |
| `Void AddSize(DuctShape, MEPSize)` | `ductSizeSettings.AddSize(shape, sizeInfo)` | Void |
| `DuctSizeSettingIterator GetDuctSizeSettingIterator()` | `ductSizeSettings.GetDuctSizeSettingIterator()` | DuctSizeSettingIterator |
| `DuctSizeSettings GetDuctSizeSettings(Document)` | `DuctSizeSettings.GetDuctSizeSettings(aDoc)` | DuctSizeSettings |
| `IEnumerator<KeyValuePair<DuctShape, DuctSizes>> GetEnumerator()` | `ductSizeSettings.GetEnumerator()` | IEnumerator<KeyValuePair<DuctShape, DuctSizes>> |
| `Int32 GetSizeCount(DuctShape)` | `ductSizeSettings.GetSizeCount(shape)` | Int32 |
| `Void RemoveSize(DuctShape, Double)` | `ductSizeSettings.RemoveSize(shape, nominalDiameter)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

---
title: ConduitSizeSettings
classe: Autodesk.Revit.DB.Electrical.ConduitSizeSettings
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# ConduitSizeSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Void AddSize(String, ConduitSize)` | `conduitSizeSettings.AddSize(standardName, sizeInfo)` | Void |
| `Boolean CreateConduitStandardTypeFromExisingStandardType(Document, String, String)` | `conduitSizeSettings.CreateConduitStandardTypeFromExisingStandardType(pADoc, newStandardName, existingStandardName)` | Boolean |
| `Boolean DoesConduitStandardTypeExist(String)` | `conduitSizeSettings.DoesConduitStandardTypeExist(standardName)` | Boolean |
| `ConduitSizeSettings GetConduitSizeSettings(Document)` | `ConduitSizeSettings.GetConduitSizeSettings(aDoc)` | ConduitSizeSettings |
| `ConduitSizeSettingIterator GetConduitSizeSettingsIterator()` | `conduitSizeSettings.GetConduitSizeSettingsIterator()` | ConduitSizeSettingIterator |
| `IEnumerator<KeyValuePair<String, ConduitSizes>> GetEnumerator()` | `conduitSizeSettings.GetEnumerator()` | IEnumerator<KeyValuePair<String, ConduitSizes>> |
| `Int32 GetSizeCount(String)` | `conduitSizeSettings.GetSizeCount(standardName)` | Int32 |
| `Boolean RemoveConduitStandardType(Document, String)` | `conduitSizeSettings.RemoveConduitStandardType(pADoc, standardName)` | Boolean |
| `Void RemoveSize(String, Double)` | `conduitSizeSettings.RemoveSize(standardName, nominalDiameter)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

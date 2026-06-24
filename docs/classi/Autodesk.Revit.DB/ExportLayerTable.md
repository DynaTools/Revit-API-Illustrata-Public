---
title: ExportLayerTable
classe: Autodesk.Revit.DB.ExportLayerTable
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 14
---

# ExportLayerTable

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 Count { get; }` | `exportLayerTable.Count` | Int32 |
| `Boolean IsValidObject { get; }` | `exportLayerTable.IsValidObject` | Boolean |
| `ExportLayerInfo Item { get; set; }` | `exportLayerTable.Item` | ExportLayerInfo |
| `Void Add(ExportLayerKey, ExportLayerInfo)` | `exportLayerTable.Add(exportLayerKey, exportLayerInfo)` | Void |
| `Void Clear()` | `exportLayerTable.Clear()` | Void |
| `Boolean ContainsKey(ExportLayerKey)` | `exportLayerTable.ContainsKey(exportlayerKey)` | Boolean |
| `Void Dispose()` | `exportLayerTable.Dispose()` | Void |
| `IList<ModifierType> GetAvaliableLayerModifierTypes(Document, ExportLayerKey)` | `ExportLayerTable.GetAvaliableLayerModifierTypes(document, exportLayerKey)` | IList<ModifierType> |
| `IEnumerator<KeyValuePair<ExportLayerKey, ExportLayerInfo>> GetEnumerator()` | `exportLayerTable.GetEnumerator()` | IEnumerator<KeyValuePair<ExportLayerKey, ExportLayerInfo>> |
| `ExportLayerInfo GetExportLayerInfo(ExportLayerKey)` | `exportLayerTable.GetExportLayerInfo(exportLayerKey)` | ExportLayerInfo |
| `IList<ExportLayerKey> GetKeys()` | `exportLayerTable.GetKeys()` | IList<ExportLayerKey> |
| `ExportLayerTableIterator GetLayerTableIterator()` | `exportLayerTable.GetLayerTableIterator()` | ExportLayerTableIterator |
| `IList<ExportLayerInfo> GetValues()` | `exportLayerTable.GetValues()` | IList<ExportLayerInfo> |
| `Void Remove(ExportLayerKey)` | `exportLayerTable.Remove(exportLayerKey)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

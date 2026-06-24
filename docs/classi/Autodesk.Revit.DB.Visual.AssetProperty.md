---
title: AssetProperty
classe: Autodesk.Revit.DB.Visual.AssetProperty
namespace: Autodesk.Revit.DB.Visual
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# AssetProperty

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsReadOnly { get; }` | `assetProperty.IsReadOnly` | Boolean |
| `Boolean IsValidObject { get; }` | `assetProperty.IsValidObject` | Boolean |
| `String Name { get; }` | `assetProperty.Name` | String |
| `Int32 NumberOfConnectedProperties { get; }` | `assetProperty.NumberOfConnectedProperties` | Int32 |
| `AssetPropertyType Type { get; }` | `assetProperty.Type` | AssetPropertyType |
| `Void AddConnectedAsset(String)` | `assetProperty.AddConnectedAsset(schema)` | Void |
| `Void AddCopyAsConnectedAsset(Asset)` | `assetProperty.AddCopyAsConnectedAsset(pRenderingAsset)` | Void |
| `Void Dispose()` | `assetProperty.Dispose()` | Void |
| `IList<AssetProperty> GetAllConnectedProperties()` | `assetProperty.GetAllConnectedProperties()` | IList<AssetProperty> |
| `AssetProperty GetConnectedProperty(Int32)` | `assetProperty.GetConnectedProperty(index)` | AssetProperty |
| `Asset GetSingleConnectedAsset()` | `assetProperty.GetSingleConnectedAsset()` | Asset |
| `String GetTypeName(AssetPropertyType)` | `AssetProperty.GetTypeName(type)` | String |
| `Boolean IsEditable()` | `assetProperty.IsEditable()` | Boolean |
| `Boolean IsValidSchemaIdentifier(String)` | `assetProperty.IsValidSchemaIdentifier(schemaID)` | Boolean |
| `Void RemoveConnectedAsset()` | `assetProperty.RemoveConnectedAsset()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

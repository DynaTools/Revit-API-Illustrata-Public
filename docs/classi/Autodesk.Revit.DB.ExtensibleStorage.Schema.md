---
title: Schema
classe: Autodesk.Revit.DB.ExtensibleStorage.Schema
namespace: Autodesk.Revit.DB.ExtensibleStorage
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# Schema

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Guid ApplicationGUID { get; }` | `schema.ApplicationGUID` | Guid |
| `String Documentation { get; }` | `schema.Documentation` | String |
| `Guid GUID { get; }` | `schema.GUID` | Guid |
| `Boolean IsValidObject { get; }` | `schema.IsValidObject` | Boolean |
| `AccessLevel ReadAccessLevel { get; }` | `schema.ReadAccessLevel` | AccessLevel |
| `String SchemaName { get; }` | `schema.SchemaName` | String |
| `String VendorId { get; }` | `schema.VendorId` | String |
| `AccessLevel WriteAccessLevel { get; }` | `schema.WriteAccessLevel` | AccessLevel |
| `Void Dispose()` | `schema.Dispose()` | Void |
| `Field GetField(String)` | `schema.GetField(name)` | Field |
| `IList<Field> ListFields()` | `schema.ListFields()` | IList<Field> |
| `IList<Schema> ListSchemas()` | `Schema.ListSchemas()` | IList<Schema> |
| `Schema Lookup(Guid)` | `Schema.Lookup(guid)` | Schema |
| `Boolean ReadAccessGranted()` | `schema.ReadAccessGranted()` | Boolean |
| `Boolean WriteAccessGranted()` | `schema.WriteAccessGranted()` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

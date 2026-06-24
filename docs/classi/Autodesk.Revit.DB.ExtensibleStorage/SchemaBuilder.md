---
title: SchemaBuilder
classe: Autodesk.Revit.DB.ExtensibleStorage.SchemaBuilder
namespace: Autodesk.Revit.DB.ExtensibleStorage
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 16
---

# SchemaBuilder

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `schemaBuilder.IsValidObject` | Boolean |
| `Boolean AcceptableName(String)` | `schemaBuilder.AcceptableName(name)` | Boolean |
| `FieldBuilder AddArrayField(String, Type)` | `schemaBuilder.AddArrayField(fieldName, fieldType)` | FieldBuilder |
| `FieldBuilder AddMapField(String, Type, Type)` | `schemaBuilder.AddMapField(fieldName, keyType, valueType)` | FieldBuilder |
| `FieldBuilder AddSimpleField(String, Type)` | `schemaBuilder.AddSimpleField(fieldName, fieldType)` | FieldBuilder |
| `Void Dispose()` | `schemaBuilder.Dispose()` | Void |
| `Schema Finish()` | `schemaBuilder.Finish()` | Schema |
| `Boolean GUIDIsValid(Guid)` | `SchemaBuilder.GUIDIsValid(guid)` | Boolean |
| `Boolean Ready()` | `schemaBuilder.Ready()` | Boolean |
| `SchemaBuilder SetApplicationGUID(Guid)` | `schemaBuilder.SetApplicationGUID(applicationGUID)` | SchemaBuilder |
| `SchemaBuilder SetDocumentation(String)` | `schemaBuilder.SetDocumentation(documentation)` | SchemaBuilder |
| `SchemaBuilder SetReadAccessLevel(AccessLevel)` | `schemaBuilder.SetReadAccessLevel(readAccessLevel)` | SchemaBuilder |
| `SchemaBuilder SetSchemaName(String)` | `schemaBuilder.SetSchemaName(schemaName)` | SchemaBuilder |
| `SchemaBuilder SetVendorId(String)` | `schemaBuilder.SetVendorId(vendorId)` | SchemaBuilder |
| `SchemaBuilder SetWriteAccessLevel(AccessLevel)` | `schemaBuilder.SetWriteAccessLevel(writeAccessLevel)` | SchemaBuilder |
| `Boolean VendorIdIsValid(String)` | `SchemaBuilder.VendorIdIsValid(vendorId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

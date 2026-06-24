---
title: Entity
classe: Autodesk.Revit.DB.ExtensibleStorage.Entity
namespace: Autodesk.Revit.DB.ExtensibleStorage
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 18
---

# Entity

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `entity.IsValidObject` | Boolean |
| `Schema Schema { get; }` | `entity.Schema` | Schema |
| `Guid SchemaGUID { get; }` | `entity.SchemaGUID` | Guid |
| `Void Clear(String)` | `entity.Clear(fieldName)` | Void |
| `Void Clear(Field)` | `entity.Clear(field)` | Void |
| `Void Dispose()` | `entity.Dispose()` | Void |
| `FieldType Get(String, ForgeTypeId)` | `entity.Get(fieldName, unitTypeId)` | FieldType |
| `FieldType Get(Field, ForgeTypeId)` | `entity.Get(field, unitTypeId)` | FieldType |
| `FieldType Get(String)` | `entity.Get(fieldName)` | FieldType |
| `FieldType Get(Field)` | `entity.Get(field)` | FieldType |
| `Boolean IsValid()` | `entity.IsValid()` | Boolean |
| `Boolean ReadAccessGranted()` | `entity.ReadAccessGranted()` | Boolean |
| `Boolean RecognizedField(Field)` | `entity.RecognizedField(field)` | Boolean |
| `Void Set(String, FieldType, ForgeTypeId)` | `entity.Set(fieldName, value, unitTypeId)` | Void |
| `Void Set(Field, FieldType, ForgeTypeId)` | `entity.Set(field, value, unitTypeId)` | Void |
| `Void Set(String, FieldType)` | `entity.Set(fieldName, value)` | Void |
| `Void Set(Field, FieldType)` | `entity.Set(field, value)` | Void |
| `Boolean WriteAccessGranted()` | `entity.WriteAccessGranted()` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

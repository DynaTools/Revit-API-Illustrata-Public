---
title: NumberingSchema
classe: Autodesk.Revit.DB.NumberingSchema
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# NumberingSchema

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 MaximumStartingNumber { get; }` | `NumberingSchema.MaximumStartingNumber` | Int32 |
| `ElementId NumberingParameterId { get; }` | `numberingSchema.NumberingParameterId` | ElementId |
| `NumberingSchemaType SchemaType { get; }` | `numberingSchema.SchemaType` | NumberingSchemaType |
| `Void AppendSequence(String, String)` | `numberingSchema.AppendSequence(fromPartition, toPartition)` | Void |
| `Void AssignElementsToSequence(ISet<ElementId>, String)` | `numberingSchema.AssignElementsToSequence(elementIds, partitionName)` | Void |
| `IList<ElementId> ChangeNumber(String, Int32, Int32)` | `numberingSchema.ChangeNumber(partition, fromNumber, toNumber)` | IList<ElementId> |
| `Int32 GetMinimumNumberOfDigits(Document)` | `NumberingSchema.GetMinimumNumberOfDigits(document)` | Int32 |
| `NumberingSchema GetNumberingSchema(Document, NumberingSchemaType)` | `NumberingSchema.GetNumberingSchema(document, schemaType)` | NumberingSchema |
| `IList<String> GetNumberingSequences()` | `numberingSchema.GetNumberingSequences()` | IList<String> |
| `IList<IntegerRange> GetNumbers(String)` | `numberingSchema.GetNumbers(partition)` | IList<IntegerRange> |
| `ISet<ElementId> GetSchemasInDocument(Document)` | `NumberingSchema.GetSchemasInDocument(document)` | ISet<ElementId> |
| `Boolean IsValidPartitionName(String, String&)` | `NumberingSchema.IsValidPartitionName(name, message)` | Boolean |
| `Void MergeSequences(IList<String>, String)` | `numberingSchema.MergeSequences(sourcePartitions, newPartition)` | Void |
| `Void MoveSequence(String, String)` | `numberingSchema.MoveSequence(fromPartition, newPartition)` | Void |
| `Void RemoveGaps(String)` | `numberingSchema.RemoveGaps(partition)` | Void |
| `Void SetMinimumNumberOfDigits(Document, Int32)` | `NumberingSchema.SetMinimumNumberOfDigits(document, value)` | Void |
| `Void ShiftNumbers(String, Int32)` | `numberingSchema.ShiftNumbers(partition, firstNumber)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

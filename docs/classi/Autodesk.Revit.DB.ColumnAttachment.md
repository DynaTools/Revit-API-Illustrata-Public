---
title: ColumnAttachment
classe: Autodesk.Revit.DB.ColumnAttachment
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 16
---

# ColumnAttachment

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double AttachOffset { get; set; }` | `columnAttachment.AttachOffset` | Double |
| `Int32 BaseOrTop { get; }` | `columnAttachment.BaseOrTop` | Int32 |
| `ColumnAttachmentCutStyle CutStyle { get; }` | `columnAttachment.CutStyle` | ColumnAttachmentCutStyle |
| `Boolean IsValidObject { get; }` | `columnAttachment.IsValidObject` | Boolean |
| `ColumnAttachmentJustification Justification { get; }` | `columnAttachment.Justification` | ColumnAttachmentJustification |
| `ElementId TargetId { get; }` | `columnAttachment.TargetId` | ElementId |
| `Void AddColumnAttachment(Document, FamilyInstance, Element, Int32, ColumnAttachmentCutStyle, ColumnAttachmentJustification, Double)` | `ColumnAttachment.AddColumnAttachment(doc, column, target, baseOrTop, cutColumnStyle, justification, attachOffset)` | Void |
| `Void Dispose()` | `columnAttachment.Dispose()` | Void |
| `ColumnAttachment GetColumnAttachment(FamilyInstance, ElementId)` | `ColumnAttachment.GetColumnAttachment(column, targetId)` | ColumnAttachment |
| `ColumnAttachment GetColumnAttachment(FamilyInstance, Int32)` | `ColumnAttachment.GetColumnAttachment(column, baseOrTop)` | ColumnAttachment |
| `Boolean IsValidColumn(FamilyInstance)` | `ColumnAttachment.IsValidColumn(familyInstance)` | Boolean |
| `Boolean IsValidTarget(Boolean, Element)` | `ColumnAttachment.IsValidTarget(forSlantedColumn, target)` | Boolean |
| `Boolean IsValidTarget(FamilyInstance, Element)` | `ColumnAttachment.IsValidTarget(column, target)` | Boolean |
| `Void RemoveColumnAttachment(FamilyInstance, ElementId)` | `ColumnAttachment.RemoveColumnAttachment(column, targetId)` | Void |
| `Void RemoveColumnAttachment(FamilyInstance, Int32)` | `ColumnAttachment.RemoveColumnAttachment(column, baseOrTop)` | Void |
| `Void SetJustification(ColumnAttachmentJustification)` | `columnAttachment.SetJustification(justification)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

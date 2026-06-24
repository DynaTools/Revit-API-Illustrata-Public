---
title: TransmissionData
classe: Autodesk.Revit.DB.TransmissionData
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# TransmissionData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsTransmitted { get; set; }` | `transmissionData.IsTransmitted` | Boolean |
| `Boolean IsValidObject { get; }` | `transmissionData.IsValidObject` | Boolean |
| `String UserData { get; set; }` | `transmissionData.UserData` | String |
| `Int32 Version { get; }` | `transmissionData.Version` | Int32 |
| `Void Dispose()` | `transmissionData.Dispose()` | Void |
| `Boolean DocumentIsNotTransmitted(ModelPath)` | `TransmissionData.DocumentIsNotTransmitted(filePath)` | Boolean |
| `ICollection<ElementId> GetAllExternalFileReferenceIds()` | `transmissionData.GetAllExternalFileReferenceIds()` | ICollection<ElementId> |
| `ExternalFileReference GetDesiredReferenceData(ElementId)` | `transmissionData.GetDesiredReferenceData(elemId)` | ExternalFileReference |
| `ExternalFileReference GetLastSavedReferenceData(ElementId)` | `transmissionData.GetLastSavedReferenceData(elemId)` | ExternalFileReference |
| `Boolean IsDocumentTransmitted(ModelPath)` | `TransmissionData.IsDocumentTransmitted(filePath)` | Boolean |
| `TransmissionData ReadTransmissionData(ModelPath)` | `TransmissionData.ReadTransmissionData(path)` | TransmissionData |
| `Void SetDesiredReferenceData(ElementId, ModelPath, PathType, Boolean)` | `transmissionData.SetDesiredReferenceData(elemId, path, pathType, shouldLoad)` | Void |
| `Void WriteTransmissionData(ModelPath, TransmissionData)` | `TransmissionData.WriteTransmissionData(path, data)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

---
title: SteelElementProperties
classe: Autodesk.Revit.DB.Steel.SteelElementProperties
namespace: Autodesk.Revit.DB.Steel
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# SteelElementProperties

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `steelElementProperties.IsValidObject` | Boolean |
| `Guid UniqueID { get; set; }` | `steelElementProperties.UniqueID` | Guid |
| `IList<ElementId> AddFabricationInformationForRevitElements(Document, IList<ElementId>)` | `SteelElementProperties.AddFabricationInformationForRevitElements(aDoc, elementIds)` | IList<ElementId> |
| `Guid GetFabricationUniqueID(Document, Reference)` | `SteelElementProperties.GetFabricationUniqueID(aDoc, reference)` | Guid |
| `Reference GetReference(Document, Guid)` | `SteelElementProperties.GetReference(aDoc, guid)` | Reference |
| `SteelElementProperties GetSteelElementProperties(Element)` | `SteelElementProperties.GetSteelElementProperties(pElement)` | SteelElementProperties |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

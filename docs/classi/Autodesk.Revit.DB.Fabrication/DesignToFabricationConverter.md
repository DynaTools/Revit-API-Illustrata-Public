---
title: DesignToFabricationConverter
classe: Autodesk.Revit.DB.Fabrication.DesignToFabricationConverter
namespace: Autodesk.Revit.DB.Fabrication
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# DesignToFabricationConverter

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `designToFabricationConverter.IsValidObject` | Boolean |
| `DesignToFabricationConverterResult Convert(ISet<ElementId>, Int32)` | `designToFabricationConverter.Convert(selection, serviceId)` | DesignToFabricationConverterResult |
| `Void Dispose()` | `designToFabricationConverter.Dispose()` | Void |
| `ISet<ElementId> GetConvertedFabricationParts()` | `designToFabricationConverter.GetConvertedFabricationParts()` | ISet<ElementId> |
| `IDictionary<ElementId, ElementId> GetConvertedFabricationPartsWithInvalidConnections()` | `designToFabricationConverter.GetConvertedFabricationPartsWithInvalidConnections()` | IDictionary<ElementId, ElementId> |
| `IDictionary<ElementId, ISet<ElementId>> GetDesignElementAndFabricationPartsWithDifferentOffsets()` | `designToFabricationConverter.GetDesignElementAndFabricationPartsWithDifferentOffsets()` | IDictionary<ElementId, ISet<ElementId>> |
| `IDictionary<ElementId, ISet<ElementId>> GetDesignElementAndFabricationPartsWithOpenConnectors()` | `designToFabricationConverter.GetDesignElementAndFabricationPartsWithOpenConnectors()` | IDictionary<ElementId, ISet<ElementId>> |
| `ISet<ElementId> GetElementsWithOpenConnector()` | `designToFabricationConverter.GetElementsWithOpenConnector()` | ISet<ElementId> |
| `IList<PartialFailureResults> GetPartialConvertFailureResults()` | `designToFabricationConverter.GetPartialConvertFailureResults()` | IList<PartialFailureResults> |
| `DesignToFabricationMappingResult SetMapForFamilySymbolToFabricationPartType(IDictionary<ElementId, ElementId>)` | `designToFabricationConverter.SetMapForFamilySymbolToFabricationPartType(typeMappings)` | DesignToFabricationMappingResult |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

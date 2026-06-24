---
title: BaseImportOptions
classe: Autodesk.Revit.DB.BaseImportOptions
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# BaseImportOptions

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean AutoCorrectAlmostVHLines { get; set; }` | `baseImportOptions.AutoCorrectAlmostVHLines` | Boolean |
| `ImportColorMode ColorMode { get; set; }` | `baseImportOptions.ColorMode` | ImportColorMode |
| `Double CustomScale { get; set; }` | `baseImportOptions.CustomScale` | Double |
| `Boolean IsValidObject { get; }` | `baseImportOptions.IsValidObject` | Boolean |
| `Boolean OrientToView { get; set; }` | `baseImportOptions.OrientToView` | Boolean |
| `ImportPlacement Placement { get; set; }` | `baseImportOptions.Placement` | ImportPlacement |
| `XYZ ReferencePoint { get; set; }` | `baseImportOptions.ReferencePoint` | XYZ |
| `Boolean ThisViewOnly { get; set; }` | `baseImportOptions.ThisViewOnly` | Boolean |
| `ImportUnit Unit { get; set; }` | `baseImportOptions.Unit` | ImportUnit |
| `Boolean VisibleLayersOnly { get; set; }` | `baseImportOptions.VisibleLayersOnly` | Boolean |
| `Void Dispose()` | `baseImportOptions.Dispose()` | Void |
| `ForgeTypeId GetDefaultLengthUnit()` | `baseImportOptions.GetDefaultLengthUnit()` | ForgeTypeId |
| `ICollection<String> GetLayerSelection()` | `baseImportOptions.GetLayerSelection()` | ICollection<String> |
| `Void SetDefaultLengthUnit(ForgeTypeId)` | `baseImportOptions.SetDefaultLengthUnit(specTypeId)` | Void |
| `Void SetLayerSelection(ICollection<String>)` | `baseImportOptions.SetLayerSelection(layerSelection)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

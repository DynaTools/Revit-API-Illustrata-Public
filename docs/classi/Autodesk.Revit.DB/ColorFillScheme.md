---
title: ColorFillScheme
classe: Autodesk.Revit.DB.ColorFillScheme
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 24
---

# ColorFillScheme

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId AreaSchemeId { get; }` | `colorFillScheme.AreaSchemeId` | ElementId |
| `ElementId CategoryId { get; }` | `colorFillScheme.CategoryId` | ElementId |
| `Boolean IsByRange { get; set; }` | `colorFillScheme.IsByRange` | Boolean |
| `Boolean IsLinkedFilesIncluded { get; set; }` | `colorFillScheme.IsLinkedFilesIncluded` | Boolean |
| `ElementId ParameterDefinition { get; set; }` | `colorFillScheme.ParameterDefinition` | ElementId |
| `StorageType StorageType { get; }` | `colorFillScheme.StorageType` | StorageType |
| `String Title { get; set; }` | `colorFillScheme.Title` | String |
| `Void AddEntry(ColorFillSchemeEntry)` | `colorFillScheme.AddEntry(entry)` | Void |
| `EntryAndSchemeConsistency AreEntriesConsistentWithScheme(IList<ColorFillSchemeEntry>)` | `colorFillScheme.AreEntriesConsistentWithScheme(entries)` | EntryAndSchemeConsistency |
| `Boolean CanDefineByRange()` | `colorFillScheme.CanDefineByRange()` | Boolean |
| `Boolean CanRemoveEntry(ColorFillSchemeEntry)` | `colorFillScheme.CanRemoveEntry(entry)` | Boolean |
| `Boolean CanUpdateEntry(ColorFillSchemeEntry)` | `colorFillScheme.CanUpdateEntry(entry)` | Boolean |
| `ElementId Duplicate(String)` | `colorFillScheme.Duplicate(name)` | ElementId |
| `IList<ColorFillSchemeEntry> GetEntries()` | `colorFillScheme.GetEntries()` | IList<ColorFillSchemeEntry> |
| `FormatOptions GetFormatOptions()` | `colorFillScheme.GetFormatOptions()` | FormatOptions |
| `IList<ElementId> GetSupportedParameterIds()` | `colorFillScheme.GetSupportedParameterIds()` | IList<ElementId> |
| `EntryAndSchemeConsistency IsEntryConsistentWithScheme(ColorFillSchemeEntry)` | `colorFillScheme.IsEntryConsistentWithScheme(entry)` | EntryAndSchemeConsistency |
| `Boolean IsValidParameterDefinitionId(ElementId)` | `colorFillScheme.IsValidParameterDefinitionId(parameterId)` | Boolean |
| `Boolean IsValidSchemeName(String)` | `colorFillScheme.IsValidSchemeName(name)` | Boolean |
| `Void RemoveEntry(ColorFillSchemeEntry)` | `colorFillScheme.RemoveEntry(entry)` | Void |
| `Void SetEntries(IList<ColorFillSchemeEntry>)` | `colorFillScheme.SetEntries(entries)` | Void |
| `Void SetFormatOptions(FormatOptions)` | `colorFillScheme.SetFormatOptions(formatOptions)` | Void |
| `Void SortEntries()` | `colorFillScheme.SortEntries()` | Void |
| `Void UpdateEntry(ColorFillSchemeEntry)` | `colorFillScheme.UpdateEntry(entry)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

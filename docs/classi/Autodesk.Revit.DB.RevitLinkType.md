---
title: RevitLinkType
classe: Autodesk.Revit.DB.RevitLinkType
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 31
---

# RevitLinkType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `AttachmentType AttachmentType { get; set; }` | `revitLinkType.AttachmentType` | AttachmentType |
| `Boolean IsNestedLink { get; }` | `revitLinkType.IsNestedLink` | Boolean |
| `Boolean LocallyUnloaded { get; }` | `revitLinkType.LocallyUnloaded` | Boolean |
| `PathType PathType { get; set; }` | `revitLinkType.PathType` | PathType |
| `LinkLoadResult Create(Document, ExternalResourceReference, RevitLinkOptions)` | `RevitLinkType.Create(document, resourceReference, options)` | LinkLoadResult |
| `LinkLoadResult Create(Document, ModelPath, RevitLinkOptions)` | `RevitLinkType.Create(document, path, options)` | LinkLoadResult |
| `LinkLoadResult CreateFromIFC(Document, ExternalResourceReference, String, Boolean, RevitLinkOptions)` | `RevitLinkType.CreateFromIFC(document, resourceReference, revitLinkedFilePath, recreateLink, options)` | LinkLoadResult |
| `LinkLoadResult CreateFromIFC(Document, String, String, Boolean, RevitLinkOptions)` | `RevitLinkType.CreateFromIFC(document, ifcFilePath, revitLinkedFilePath, recreateLink, options)` | LinkLoadResult |
| `ICollection<ElementId> GetChildIds()` | `revitLinkType.GetChildIds()` | ICollection<ElementId> |
| `LinkConversionData GetConversionData()` | `revitLinkType.GetConversionData()` | LinkConversionData |
| `LinkedFileStatus GetLinkedFileStatus()` | `revitLinkType.GetLinkedFileStatus()` | LinkedFileStatus |
| `ElementId GetParentId()` | `revitLinkType.GetParentId()` | ElementId |
| `IDictionary<ElementId, ElementId> GetPhaseMap()` | `revitLinkType.GetPhaseMap()` | IDictionary<ElementId, ElementId> |
| `ElementId GetRootId()` | `revitLinkType.GetRootId()` | ElementId |
| `ElementId GetTopLevelLink(Document, ExternalResourceReference)` | `RevitLinkType.GetTopLevelLink(document, reference)` | ElementId |
| `ElementId GetTopLevelLink(Document, ModelPath)` | `RevitLinkType.GetTopLevelLink(document, path)` | ElementId |
| `Boolean HasSaveablePositions()` | `revitLinkType.HasSaveablePositions()` | Boolean |
| `Boolean IsFromLocalPath()` | `revitLinkType.IsFromLocalPath()` | Boolean |
| `Boolean IsFromRevitServer()` | `revitLinkType.IsFromRevitServer()` | Boolean |
| `Boolean IsLoaded(Document, ElementId)` | `RevitLinkType.IsLoaded(document, typeId)` | Boolean |
| `Boolean IsNotLoadedIntoMultipleOpenDocuments()` | `revitLinkType.IsNotLoadedIntoMultipleOpenDocuments()` | Boolean |
| `LinkLoadResult Load()` | `revitLinkType.Load()` | LinkLoadResult |
| `LinkLoadResult LoadFrom(ModelPath, WorksetConfiguration)` | `revitLinkType.LoadFrom(path, config)` | LinkLoadResult |
| `LinkLoadResult LoadFrom(ExternalResourceReference, WorksetConfiguration)` | `revitLinkType.LoadFrom(resourceReference, config)` | LinkLoadResult |
| `LinkLoadResult Reload()` | `revitLinkType.Reload()` | LinkLoadResult |
| `LinkedFileStatus RevertLocalUnloadStatus()` | `revitLinkType.RevertLocalUnloadStatus()` | LinkedFileStatus |
| `Boolean SavePositions(ISaveSharedCoordinatesCallback)` | `revitLinkType.SavePositions(callback)` | Boolean |
| `Void Unload(ISaveSharedCoordinatesCallback)` | `revitLinkType.Unload(callback)` | Void |
| `Boolean UnloadLocally(ISaveSharedCoordinatesCallbackForUnloadLocally)` | `revitLinkType.UnloadLocally(callback)` | Boolean |
| `Boolean UpdateFromIFC(Document, ExternalResourceReference, String, Boolean)` | `revitLinkType.UpdateFromIFC(document, resourceReference, revitLinkedFilePath, recreateLink)` | Boolean |
| `Boolean UpdateFromIFC(Document, String, String, Boolean)` | `revitLinkType.UpdateFromIFC(document, ifcFilePath, revitLinkedFilePath, recreateLink)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

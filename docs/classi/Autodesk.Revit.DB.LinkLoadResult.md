---
title: LinkLoadResult
classe: Autodesk.Revit.DB.LinkLoadResult
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 14
---

# LinkLoadResult

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId ElementId { get; }` | `linkLoadResult.ElementId` | ElementId |
| `Boolean IsCircularLink { get; }` | `linkLoadResult.IsCircularLink` | Boolean |
| `Boolean IsNested { get; }` | `linkLoadResult.IsNested` | Boolean |
| `Boolean IsValidObject { get; }` | `linkLoadResult.IsValidObject` | Boolean |
| `LinkLoadResultType LoadResult { get; }` | `linkLoadResult.LoadResult` | LinkLoadResultType |
| `Void Dispose()` | `linkLoadResult.Dispose()` | Void |
| `ModelPath GetCentralModelName()` | `linkLoadResult.GetCentralModelName()` | ModelPath |
| `ExternalResourceReference GetExternalResourceReference()` | `linkLoadResult.GetExternalResourceReference()` | ExternalResourceReference |
| `IList<ExternalResourceReference> GetExternalResourceReferencesFromFailedLoads()` | `linkLoadResult.GetExternalResourceReferencesFromFailedLoads()` | IList<ExternalResourceReference> |
| `LinkLoadResult GetLinkLoadResult(ExternalResourceReference)` | `linkLoadResult.GetLinkLoadResult(matchExtResRef)` | LinkLoadResult |
| `ModelPath GetModelName()` | `linkLoadResult.GetModelName()` | ModelPath |
| `IDictionary<String, LinkLoadResult> GetNestedLinkLoadResults()` | `linkLoadResult.GetNestedLinkLoadResults()` | IDictionary<String, LinkLoadResult> |
| `ModelPath GetParentModelName()` | `linkLoadResult.GetParentModelName()` | ModelPath |
| `Boolean IsCodeSuccess(LinkLoadResultType)` | `LinkLoadResult.IsCodeSuccess(code)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

---
title: FilteredWorksetCollector
classe: Autodesk.Revit.DB.FilteredWorksetCollector
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# FilteredWorksetCollector

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `filteredWorksetCollector.IsValidObject` | Boolean |
| `Void Dispose()` | `filteredWorksetCollector.Dispose()` | Void |
| `Workset FirstWorkset()` | `filteredWorksetCollector.FirstWorkset()` | Workset |
| `WorksetId FirstWorksetId()` | `filteredWorksetCollector.FirstWorksetId()` | WorksetId |
| `IEnumerator<Workset> GetEnumerator()` | `filteredWorksetCollector.GetEnumerator()` | IEnumerator<Workset> |
| `FilteredWorksetIdIterator GetWorksetIdIterator()` | `filteredWorksetCollector.GetWorksetIdIterator()` | FilteredWorksetIdIterator |
| `FilteredWorksetIterator GetWorksetIterator()` | `filteredWorksetCollector.GetWorksetIterator()` | FilteredWorksetIterator |
| `FilteredWorksetCollector OfKind(WorksetKind)` | `filteredWorksetCollector.OfKind(worksetKind)` | FilteredWorksetCollector |
| `ICollection<WorksetId> ToWorksetIds()` | `filteredWorksetCollector.ToWorksetIds()` | ICollection<WorksetId> |
| `IList<Workset> ToWorksets()` | `filteredWorksetCollector.ToWorksets()` | IList<Workset> |
| `FilteredWorksetCollector WherePasses(WorksetFilter)` | `filteredWorksetCollector.WherePasses(filter)` | FilteredWorksetCollector |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

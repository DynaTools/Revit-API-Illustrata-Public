---
title: FilteredElementCollector
classe: Autodesk.Revit.DB.FilteredElementCollector
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 24
---

# FilteredElementCollector

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `filteredElementCollector.IsValidObject` | Boolean |
| `FilteredElementCollector ContainedInDesignOption(ElementId)` | `filteredElementCollector.ContainedInDesignOption(designOptionId)` | FilteredElementCollector |
| `Void Dispose()` | `filteredElementCollector.Dispose()` | Void |
| `FilteredElementCollector Excluding(ICollection<ElementId>)` | `filteredElementCollector.Excluding(idsToExclude)` | FilteredElementCollector |
| `Element FirstElement()` | `filteredElementCollector.FirstElement()` | Element |
| `ElementId FirstElementId()` | `filteredElementCollector.FirstElementId()` | ElementId |
| `Int32 GetElementCount()` | `filteredElementCollector.GetElementCount()` | Int32 |
| `FilteredElementIdIterator GetElementIdIterator()` | `filteredElementCollector.GetElementIdIterator()` | FilteredElementIdIterator |
| `FilteredElementIterator GetElementIterator()` | `filteredElementCollector.GetElementIterator()` | FilteredElementIterator |
| `IEnumerator<Element> GetEnumerator()` | `filteredElementCollector.GetEnumerator()` | IEnumerator<Element> |
| `FilteredElementCollector IntersectWith(FilteredElementCollector)` | `filteredElementCollector.IntersectWith(other)` | FilteredElementCollector |
| `Boolean IsViewValidForElementIteration(Document, ElementId)` | `FilteredElementCollector.IsViewValidForElementIteration(document, viewId)` | Boolean |
| `FilteredElementCollector OfCategory(BuiltInCategory)` | `filteredElementCollector.OfCategory(category)` | FilteredElementCollector |
| `FilteredElementCollector OfCategoryId(ElementId)` | `filteredElementCollector.OfCategoryId(categoryId)` | FilteredElementCollector |
| `FilteredElementCollector OfClass(Type)` | `filteredElementCollector.OfClass(type)` | FilteredElementCollector |
| `FilteredElementCollector OwnedByView(ElementId)` | `filteredElementCollector.OwnedByView(viewId)` | FilteredElementCollector |
| `ICollection<ElementId> ToElementIds()` | `filteredElementCollector.ToElementIds()` | ICollection<ElementId> |
| `IList<Element> ToElements()` | `filteredElementCollector.ToElements()` | IList<Element> |
| `FilteredElementCollector UnionWith(FilteredElementCollector)` | `filteredElementCollector.UnionWith(other)` | FilteredElementCollector |
| `FilteredElementCollector WhereElementIsCurveDriven()` | `filteredElementCollector.WhereElementIsCurveDriven()` | FilteredElementCollector |
| `FilteredElementCollector WhereElementIsElementType()` | `filteredElementCollector.WhereElementIsElementType()` | FilteredElementCollector |
| `FilteredElementCollector WhereElementIsNotElementType()` | `filteredElementCollector.WhereElementIsNotElementType()` | FilteredElementCollector |
| `FilteredElementCollector WhereElementIsViewIndependent()` | `filteredElementCollector.WhereElementIsViewIndependent()` | FilteredElementCollector |
| `FilteredElementCollector WherePasses(ElementFilter)` | `filteredElementCollector.WherePasses(filter)` | FilteredElementCollector |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

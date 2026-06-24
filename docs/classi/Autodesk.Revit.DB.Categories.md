---
title: Categories
classe: Autodesk.Revit.DB.Categories
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.CategoryNameMap
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 10
---

# Categories

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsEmpty { get; }` | `categories.IsEmpty` | Boolean |
| `Category Item { get; set; }` | `categories.Item` | Category |
| `Category Item { get; }` | `categories.Item` | Category |
| `Int32 Size { get; }` | `categories.Size` | Int32 |
| `Boolean Contains(String)` | `categories.Contains(name)` | Boolean |
| `CategoryNameMapIterator ForwardIterator()` | `categories.ForwardIterator()` | CategoryNameMapIterator |
| `IEnumerator GetEnumerator()` | `categories.GetEnumerator()` | IEnumerator |
| `Boolean Insert(String, Category)` | `categories.Insert(key, item)` | Boolean |
| `Category NewSubcategory(Category, String)` | `categories.NewSubcategory(parentCategory, name)` | Category |
| `CategoryNameMapIterator ReverseIterator()` | `categories.ReverseIterator()` | CategoryNameMapIterator |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

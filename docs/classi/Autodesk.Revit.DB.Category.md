---
title: Category
classe: Autodesk.Revit.DB.Category
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 28
---

# Category

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean AllowsBoundParameters { get; }` | `category.AllowsBoundParameters` | Boolean |
| `Boolean AllowsVisibilityControl { get; }` | `category.AllowsVisibilityControl` | Boolean |
| `BuiltInCategory BuiltInCategory { get; }` | `category.BuiltInCategory` | BuiltInCategory |
| `Boolean CanAddSubcategory { get; }` | `category.CanAddSubcategory` | Boolean |
| `CategoryType CategoryType { get; }` | `category.CategoryType` | CategoryType |
| `Boolean HasMaterialQuantities { get; }` | `category.HasMaterialQuantities` | Boolean |
| `ElementId Id { get; }` | `category.Id` | ElementId |
| `Boolean IsCuttable { get; }` | `category.IsCuttable` | Boolean |
| `Boolean IsTagCategory { get; }` | `category.IsTagCategory` | Boolean |
| `Boolean IsValid { get; }` | `category.IsValid` | Boolean |
| `Boolean IsVisibleInUI { get; }` | `category.IsVisibleInUI` | Boolean |
| `Color LineColor { get; set; }` | `category.LineColor` | Color |
| `Material Material { get; set; }` | `category.Material` | Material |
| `String Name { get; }` | `category.Name` | String |
| `Category Parent { get; }` | `category.Parent` | Category |
| `CategoryNameMap SubCategories { get; }` | `category.SubCategories` | CategoryNameMap |
| `Boolean Visible { get; set; }` | `category.Visible` | Boolean |
| `BuiltInCategory GetBuiltInCategory(ForgeTypeId)` | `Category.GetBuiltInCategory(categoryTypeId)` | BuiltInCategory |
| `ForgeTypeId GetBuiltInCategoryTypeId(BuiltInCategory)` | `Category.GetBuiltInCategoryTypeId(categoryId)` | ForgeTypeId |
| `Category GetCategory(Document, ElementId)` | `Category.GetCategory(document, categoryId)` | Category |
| `Category GetCategory(Document, BuiltInCategory)` | `Category.GetCategory(document, categoryId)` | Category |
| `GraphicsStyle GetGraphicsStyle(GraphicsStyleType)` | `category.GetGraphicsStyle(graphicsStyleType)` | GraphicsStyle |
| `ElementId GetLinePatternId(GraphicsStyleType)` | `category.GetLinePatternId(graphicsStyleType)` | ElementId |
| `Nullable<Int32> GetLineWeight(GraphicsStyleType)` | `category.GetLineWeight(graphicsStyleType)` | Nullable<Int32> |
| `Boolean IsBuiltInCategory(ForgeTypeId)` | `Category.IsBuiltInCategory(categoryTypeId)` | Boolean |
| `Boolean IsBuiltInCategoryValid(BuiltInCategory)` | `Category.IsBuiltInCategoryValid(builtInCategory)` | Boolean |
| `Void SetLinePatternId(ElementId, GraphicsStyleType)` | `category.SetLinePatternId(linePatternId, graphicsStyleType)` | Void |
| `Void SetLineWeight(Int32, GraphicsStyleType)` | `category.SetLineWeight(lineWeight, graphicsStyleType)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

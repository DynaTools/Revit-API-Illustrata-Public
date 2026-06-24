---
title: Material
classe: Autodesk.Revit.DB.Material
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 24
---

# Material

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId AppearanceAssetId { get; set; }` | `material.AppearanceAssetId` | ElementId |
| `Color Color { get; set; }` | `material.Color` | Color |
| `Color CutBackgroundPatternColor { get; set; }` | `material.CutBackgroundPatternColor` | Color |
| `ElementId CutBackgroundPatternId { get; set; }` | `material.CutBackgroundPatternId` | ElementId |
| `Color CutForegroundPatternColor { get; set; }` | `material.CutForegroundPatternColor` | Color |
| `ElementId CutForegroundPatternId { get; set; }` | `material.CutForegroundPatternId` | ElementId |
| `String MaterialCategory { get; set; }` | `material.MaterialCategory` | String |
| `String MaterialClass { get; set; }` | `material.MaterialClass` | String |
| `Int32 Shininess { get; set; }` | `material.Shininess` | Int32 |
| `Int32 Smoothness { get; set; }` | `material.Smoothness` | Int32 |
| `ElementId StructuralAssetId { get; set; }` | `material.StructuralAssetId` | ElementId |
| `Color SurfaceBackgroundPatternColor { get; set; }` | `material.SurfaceBackgroundPatternColor` | Color |
| `ElementId SurfaceBackgroundPatternId { get; set; }` | `material.SurfaceBackgroundPatternId` | ElementId |
| `Color SurfaceForegroundPatternColor { get; set; }` | `material.SurfaceForegroundPatternColor` | Color |
| `ElementId SurfaceForegroundPatternId { get; set; }` | `material.SurfaceForegroundPatternId` | ElementId |
| `ElementId ThermalAssetId { get; set; }` | `material.ThermalAssetId` | ElementId |
| `Int32 Transparency { get; set; }` | `material.Transparency` | Int32 |
| `Boolean UseRenderAppearanceForShading { get; set; }` | `material.UseRenderAppearanceForShading` | Boolean |
| `Void ClearMaterialAspect(MaterialAspect)` | `material.ClearMaterialAspect(aspect)` | Void |
| `ElementId Create(Document, String)` | `Material.Create(document, name)` | ElementId |
| `Material Duplicate(String)` | `material.Duplicate(name)` | Material |
| `Boolean IsMaterialOrValidDefault(Element, ElementId)` | `Material.IsMaterialOrValidDefault(pElem, materialId)` | Boolean |
| `Boolean IsNameUnique(Document, String)` | `Material.IsNameUnique(aDocument, name)` | Boolean |
| `Void SetMaterialAspectByPropertySet(MaterialAspect, ElementId)` | `material.SetMaterialAspectByPropertySet(aspect, propertySetId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

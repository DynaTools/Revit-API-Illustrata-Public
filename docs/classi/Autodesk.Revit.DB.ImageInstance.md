---
title: ImageInstance
classe: Autodesk.Revit.DB.ImageInstance
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# ImageInstance

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean CanHaveSnaps { get; }` | `imageInstance.CanHaveSnaps` | Boolean |
| `DrawLayer DrawLayer { get; set; }` | `imageInstance.DrawLayer` | DrawLayer |
| `Boolean EnableSnaps { get; set; }` | `imageInstance.EnableSnaps` | Boolean |
| `Double Height { get; set; }` | `imageInstance.Height` | Double |
| `Double HeightScale { get; set; }` | `imageInstance.HeightScale` | Double |
| `Boolean LockProportions { get; set; }` | `imageInstance.LockProportions` | Boolean |
| `Double Width { get; set; }` | `imageInstance.Width` | Double |
| `Double WidthScale { get; set; }` | `imageInstance.WidthScale` | Double |
| `ImageInstance Create(Document, View, ElementId, ImagePlacementOptions)` | `ImageInstance.Create(document, view, imageTypeId, placementOptions)` | ImageInstance |
| `XYZ GetLocation(BoxPlacement)` | `imageInstance.GetLocation(placementPoint)` | XYZ |
| `Boolean IsValidView(View)` | `ImageInstance.IsValidView(view)` | Boolean |
| `Void SetLocation(XYZ, BoxPlacement)` | `imageInstance.SetLocation(newLocation, placementPoint)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

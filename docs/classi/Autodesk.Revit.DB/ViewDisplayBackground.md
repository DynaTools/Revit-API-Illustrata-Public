---
title: ViewDisplayBackground
classe: Autodesk.Revit.DB.ViewDisplayBackground
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# ViewDisplayBackground

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Color BackgroundColor { get; }` | `viewDisplayBackground.BackgroundColor` | Color |
| `Color GroundColor { get; }` | `viewDisplayBackground.GroundColor` | Color |
| `Double HorizontalImageOffset { get; }` | `viewDisplayBackground.HorizontalImageOffset` | Double |
| `Double HorizontalImageScale { get; }` | `viewDisplayBackground.HorizontalImageScale` | Double |
| `ViewDisplayBackgroundImageFlags ImageFlags { get; }` | `viewDisplayBackground.ImageFlags` | ViewDisplayBackgroundImageFlags |
| `String ImagePath { get; }` | `viewDisplayBackground.ImagePath` | String |
| `Boolean IsValidObject { get; }` | `viewDisplayBackground.IsValidObject` | Boolean |
| `Color SkyColor { get; }` | `viewDisplayBackground.SkyColor` | Color |
| `ViewDisplayBackgroundType Type { get; }` | `viewDisplayBackground.Type` | ViewDisplayBackgroundType |
| `Double VerticalImageOffset { get; }` | `viewDisplayBackground.VerticalImageOffset` | Double |
| `Double VerticalImageScale { get; }` | `viewDisplayBackground.VerticalImageScale` | Double |
| `ViewDisplayBackground CreateGradient(Color, Color, Color)` | `ViewDisplayBackground.CreateGradient(skyColor, horizonColor, groundColor)` | ViewDisplayBackground |
| `ViewDisplayBackground CreateImage(String, ViewDisplayBackgroundImageFlags, UV, UV)` | `ViewDisplayBackground.CreateImage(imagePath, flags, imageOffsets, imageScales)` | ViewDisplayBackground |
| `ViewDisplayBackground CreateSky()` | `ViewDisplayBackground.CreateSky()` | ViewDisplayBackground |
| `Void Dispose()` | `viewDisplayBackground.Dispose()` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

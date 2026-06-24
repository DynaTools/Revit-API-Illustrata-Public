---
title: TextElement
classe: Autodesk.Revit.DB.TextElement
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# TextElement

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ BaseDirection { get; }` | `textElement.BaseDirection` | XYZ |
| `XYZ Coord { get; set; }` | `textElement.Coord` | XYZ |
| `Double Height { get; }` | `textElement.Height` | Double |
| `HorizontalTextAlignment HorizontalAlignment { get; set; }` | `textElement.HorizontalAlignment` | HorizontalTextAlignment |
| `Boolean IsTextWrappingActive { get; }` | `textElement.IsTextWrappingActive` | Boolean |
| `Boolean KeepRotatedTextReadable { get; set; }` | `textElement.KeepRotatedTextReadable` | Boolean |
| `TextElementType Symbol { get; }` | `textElement.Symbol` | TextElementType |
| `String Text { get; set; }` | `textElement.Text` | String |
| `XYZ UpDirection { get; }` | `textElement.UpDirection` | XYZ |
| `VerticalTextAlignment VerticalAlignment { get; set; }` | `textElement.VerticalAlignment` | VerticalTextAlignment |
| `Double Width { get; set; }` | `textElement.Width` | Double |
| `Double GetMaximumAllowedWidth(Document, ElementId)` | `TextElement.GetMaximumAllowedWidth(cdda, typeId)` | Double |
| `Double GetMaximumAllowedWidth()` | `textElement.GetMaximumAllowedWidth()` | Double |
| `Double GetMinimumAllowedWidth(Document, ElementId)` | `TextElement.GetMinimumAllowedWidth(cdda, typeId)` | Double |
| `Double GetMinimumAllowedWidth()` | `textElement.GetMinimumAllowedWidth()` | Double |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

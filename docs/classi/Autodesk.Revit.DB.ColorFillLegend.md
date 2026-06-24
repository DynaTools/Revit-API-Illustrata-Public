---
title: ColorFillLegend
classe: Autodesk.Revit.DB.ColorFillLegend
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 6
---

# ColorFillLegend

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId ColorFillCategoryId { get; }` | `colorFillLegend.ColorFillCategoryId` | ElementId |
| `Double Height { get; set; }` | `colorFillLegend.Height` | Double |
| `XYZ Origin { get; set; }` | `colorFillLegend.Origin` | XYZ |
| `ColorFillLegend Create(Document, ElementId, ElementId, XYZ)` | `ColorFillLegend.Create(document, viewId, catetoryId, origin)` | ColorFillLegend |
| `IList<Double> GetColumnWidths()` | `colorFillLegend.GetColumnWidths()` | IList<Double> |
| `Void SetColumnWidths(IList<Double>)` | `colorFillLegend.SetColumnWidths(widths)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

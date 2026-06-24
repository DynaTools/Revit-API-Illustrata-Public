---
title: ShapeImporter
classe: Autodesk.Revit.DB.ShapeImporter
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# ShapeImporter

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ImportUnit DefaultLengthUnit { get; }` | `shapeImporter.DefaultLengthUnit` | ImportUnit |
| `ShapeImporterSourceFormat InputFormat { get; set; }` | `shapeImporter.InputFormat` | ShapeImporterSourceFormat |
| `Boolean IsValidObject { get; }` | `shapeImporter.IsValidObject` | Boolean |
| `IList<GeometryObject> Convert(Document, String)` | `shapeImporter.Convert(document, filename)` | IList<GeometryObject> |
| `Void Dispose()` | `shapeImporter.Dispose()` | Void |
| `Boolean IsServiceAvailable()` | `ShapeImporter.IsServiceAvailable()` | Boolean |
| `ShapeImporter SetDefaultLengthUnit(ImportUnit)` | `shapeImporter.SetDefaultLengthUnit(defaultLengthUnit)` | ShapeImporter |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

---
title: Duct
classe: Autodesk.Revit.DB.Mechanical.Duct
namespace: Autodesk.Revit.DB.Mechanical
eredita: Autodesk.Revit.DB.MEPCurve
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 9
---

# Duct

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `DuctType DuctType { get; set; }` | `duct.DuctType` | DuctType |
| `Boolean IsPlaceholder { get; }` | `duct.IsPlaceholder` | Boolean |
| `Duct Create(Document, ElementId, ElementId, Connector, Connector)` | `Duct.Create(document, ductTypeId, levelId, startConnector, endConnector)` | Duct |
| `Duct Create(Document, ElementId, ElementId, Connector, XYZ)` | `Duct.Create(document, ductTypeId, levelId, startConnector, endPoint)` | Duct |
| `Duct Create(Document, ElementId, ElementId, ElementId, XYZ, XYZ)` | `Duct.Create(document, systemTypeId, ductTypeId, levelId, startPoint, endPoint)` | Duct |
| `Duct CreatePlaceholder(Document, ElementId, ElementId, ElementId, XYZ, XYZ)` | `Duct.CreatePlaceholder(document, systemTypeId, ductTypeId, levelId, startPoint, endPoint)` | Duct |
| `Boolean IsDuctTypeId(Document, ElementId)` | `Duct.IsDuctTypeId(document, ductTypeId)` | Boolean |
| `Boolean IsHvacSystemTypeId(Document, ElementId)` | `Duct.IsHvacSystemTypeId(document, systemTypeId)` | Boolean |
| `Void SetSystemType(ElementId)` | `duct.SetSystemType(systemTypeId)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

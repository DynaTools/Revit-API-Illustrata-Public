---
title: Frame
classe: Autodesk.Revit.DB.Frame
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# Frame

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `XYZ BasisX { get; set; }` | `frame.BasisX` | XYZ |
| `XYZ BasisY { get; set; }` | `frame.BasisY` | XYZ |
| `XYZ BasisZ { get; set; }` | `frame.BasisZ` | XYZ |
| `Boolean IsValidObject { get; }` | `frame.IsValidObject` | Boolean |
| `XYZ Origin { get; set; }` | `frame.Origin` | XYZ |
| `Boolean CanDefineRevitGeometry(Frame)` | `Frame.CanDefineRevitGeometry(frameOfReference)` | Boolean |
| `Void Dispose()` | `frame.Dispose()` | Void |
| `Boolean IsOrthogonal()` | `frame.IsOrthogonal()` | Boolean |
| `Boolean IsOrthonormal()` | `frame.IsOrthonormal()` | Boolean |
| `Boolean IsRightHanded()` | `frame.IsRightHanded()` | Boolean |
| `Void Transform(Transform)` | `frame.Transform(trf)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

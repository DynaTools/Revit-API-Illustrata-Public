---
title: Reference
classe: Autodesk.Revit.DB.Reference
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# Reference

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId ElementId { get; }` | `reference.ElementId` | ElementId |
| `ElementReferenceType ElementReferenceType { get; }` | `reference.ElementReferenceType` | ElementReferenceType |
| `XYZ GlobalPoint { get; }` | `reference.GlobalPoint` | XYZ |
| `ElementId LinkedElementId { get; }` | `reference.LinkedElementId` | ElementId |
| `UV UVPoint { get; }` | `reference.UVPoint` | UV |
| `Boolean Contains(Reference)` | `reference.Contains(reference)` | Boolean |
| `String ConvertToStableRepresentation(Document)` | `reference.ConvertToStableRepresentation(document)` | String |
| `Reference CreateLinkReference(RevitLinkInstance)` | `reference.CreateLinkReference(revitLinkInstance)` | Reference |
| `Reference CreateReferenceInLink()` | `reference.CreateReferenceInLink()` | Reference |
| `Boolean EqualTo(Reference)` | `reference.EqualTo(reference)` | Boolean |
| `Reference ParseFromStableRepresentation(Document, String)` | `Reference.ParseFromStableRepresentation(document, representation)` | Reference |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

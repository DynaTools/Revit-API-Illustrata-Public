---
title: RebarPropagation
classe: Autodesk.Revit.DB.Structure.RebarPropagation
namespace: Autodesk.Revit.DB.Structure
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 2
---

# RebarPropagation

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ISet<ElementId> AlignByFace(Document, IList<Rebar>, Reference, Reference)` | `RebarPropagation.AlignByFace(doc, sourceRebars, sourceFaceReference, destinationFaceReference)` | ISet<ElementId> |
| `ISet<ElementId> AlignByHost(Document, IList<Rebar>, Element)` | `RebarPropagation.AlignByHost(doc, sourceRebars, destinationHost)` | ISet<ElementId> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

---
title: SharedParameterElement
classe: Autodesk.Revit.DB.SharedParameterElement
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.ParameterElement
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 4
---

# SharedParameterElement

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Guid GuidValue { get; }` | `sharedParameterElement.GuidValue` | Guid |
| `SharedParameterElement Create(Document, ExternalDefinition)` | `SharedParameterElement.Create(document, sharedParameterDefinition)` | SharedParameterElement |
| `SharedParameterElement Lookup(Document, Guid)` | `SharedParameterElement.Lookup(document, guidValue)` | SharedParameterElement |
| `Boolean ShouldHideWhenNoValue()` | `sharedParameterElement.ShouldHideWhenNoValue()` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

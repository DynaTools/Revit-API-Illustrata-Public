---
title: ElectricalLoadAreaData
classe: Autodesk.Revit.DB.Electrical.ElectricalLoadAreaData
namespace: Autodesk.Revit.DB.Electrical
eredita: Autodesk.Revit.DB.SpatialElementDomainData
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 3
---

# ElectricalLoadAreaData

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ISet<ElementId> CreateElectricalLoadAreas(Document, ElementId, ElementId)` | `ElectricalLoadAreaData.CreateElectricalLoadAreas(doc, levelId, phaseId)` | ISet<ElementId> |
| `ISet<ElementId> GetAreaBasedLoadIds()` | `electricalLoadAreaData.GetAreaBasedLoadIds()` | ISet<ElementId> |
| `Boolean HasCircuitsWithoutElectricalLoadAreas(Document, ElementId, ElementId)` | `ElectricalLoadAreaData.HasCircuitsWithoutElectricalLoadAreas(doc, levelId, phaseId)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

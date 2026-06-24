---
title: MEPSpaceConstruction
classe: Autodesk.Revit.DB.Mechanical.MEPSpaceConstruction
namespace: Autodesk.Revit.DB.Mechanical
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 5
---

# MEPSpaceConstruction

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `MEPBuildingConstruction CurrentConstruction { get; set; }` | `mEPSpaceConstruction.CurrentConstruction` | MEPBuildingConstruction |
| `MEPBuildingConstructionSet SpaceConstructions { get; }` | `mEPSpaceConstruction.SpaceConstructions` | MEPBuildingConstructionSet |
| `Void DeleteConstruction(MEPBuildingConstruction)` | `mEPSpaceConstruction.DeleteConstruction(pCurrentConstruction)` | Void |
| `MEPBuildingConstruction DuplicateConstruction(MEPBuildingConstruction, String)` | `mEPSpaceConstruction.DuplicateConstruction(pCurrentConstruction, pName)` | MEPBuildingConstruction |
| `MEPBuildingConstruction NewConstruction(String)` | `mEPSpaceConstruction.NewConstruction(pName)` | MEPBuildingConstruction |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

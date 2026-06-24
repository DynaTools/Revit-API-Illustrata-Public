---
title: PolymeshTopology
classe: Autodesk.Revit.DB.PolymeshTopology
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 15
---

# PolymeshTopology

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `DistributionOfNormals DistributionOfNormals { get; }` | `polymeshTopology.DistributionOfNormals` | DistributionOfNormals |
| `Boolean IsValidObject { get; }` | `polymeshTopology.IsValidObject` | Boolean |
| `Int32 NumberOfFacets { get; }` | `polymeshTopology.NumberOfFacets` | Int32 |
| `Int32 NumberOfNormals { get; }` | `polymeshTopology.NumberOfNormals` | Int32 |
| `Int32 NumberOfPoints { get; }` | `polymeshTopology.NumberOfPoints` | Int32 |
| `Int32 NumberOfUVs { get; }` | `polymeshTopology.NumberOfUVs` | Int32 |
| `Void Dispose()` | `polymeshTopology.Dispose()` | Void |
| `PolymeshFacet GetFacet(Int32)` | `polymeshTopology.GetFacet(idx)` | PolymeshFacet |
| `IList<PolymeshFacet> GetFacets()` | `polymeshTopology.GetFacets()` | IList<PolymeshFacet> |
| `XYZ GetNormal(Int32)` | `polymeshTopology.GetNormal(idx)` | XYZ |
| `IList<XYZ> GetNormals()` | `polymeshTopology.GetNormals()` | IList<XYZ> |
| `XYZ GetPoint(Int32)` | `polymeshTopology.GetPoint(idx)` | XYZ |
| `IList<XYZ> GetPoints()` | `polymeshTopology.GetPoints()` | IList<XYZ> |
| `UV GetUV(Int32)` | `polymeshTopology.GetUV(idx)` | UV |
| `IList<UV> GetUVs()` | `polymeshTopology.GetUVs()` | IList<UV> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

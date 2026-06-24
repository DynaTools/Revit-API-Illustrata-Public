---
title: Mesh
classe: Autodesk.Revit.DB.Mesh
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.GeometryObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 11
---

# Mesh

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `DistributionOfNormals DistributionOfNormals { get; }` | `mesh.DistributionOfNormals` | DistributionOfNormals |
| `Boolean IsClosed { get; }` | `mesh.IsClosed` | Boolean |
| `ElementId MaterialElementId { get; }` | `mesh.MaterialElementId` | ElementId |
| `Int32 NumberOfNormals { get; }` | `mesh.NumberOfNormals` | Int32 |
| `Int32 NumTriangles { get; }` | `mesh.NumTriangles` | Int32 |
| `Mesh Transformed { get; }` | `mesh.Transformed` | Mesh |
| `MeshTriangle Triangle { get; }` | `mesh.Triangle` | MeshTriangle |
| `IList<XYZ> Vertices { get; }` | `mesh.Vertices` | IList<XYZ> |
| `Double ComputeSurfaceArea()` | `mesh.ComputeSurfaceArea()` | Double |
| `XYZ GetNormal(Int32)` | `mesh.GetNormal(idx)` | XYZ |
| `IList<XYZ> GetNormals()` | `mesh.GetNormals()` | IList<XYZ> |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

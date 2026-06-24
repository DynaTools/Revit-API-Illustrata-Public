---
title: ImportInstance
classe: Autodesk.Revit.DB.ImportInstance
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Instance
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# ImportInstance

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsLinked { get; }` | `importInstance.IsLinked` | Boolean |
| `ImportInstance Create(Document, View, ExternalResourceReference, STEPImportOptions, LinkLoadResult&)` | `ImportInstance.Create(document, DBView, resourceReference, options, linkLoadResult)` | ImportInstance |
| `ImportInstance Create(Document, View, ExternalResourceReference, ImportOptions3DM, LinkLoadResult&)` | `ImportInstance.Create(document, DBView, resourceReference, options, linkLoadResult)` | ImportInstance |
| `ImportInstance Create(Document, View, ExternalResourceReference, STLImportOptions, LinkLoadResult&)` | `ImportInstance.Create(document, DBView, resourceReference, options, linkLoadResult)` | ImportInstance |
| `ImportInstance Create(Document, View, ExternalResourceReference, SKPImportOptions, LinkLoadResult&)` | `ImportInstance.Create(document, DBView, resourceReference, options, linkLoadResult)` | ImportInstance |
| `ImportInstance Create(Document, View, ExternalResourceReference, SATImportOptions, LinkLoadResult&)` | `ImportInstance.Create(document, DBView, resourceReference, options, linkLoadResult)` | ImportInstance |
| `ImportInstance Create(Document, View, ExternalResourceReference, OBJImportOptions, LinkLoadResult&)` | `ImportInstance.Create(document, DBView, resourceReference, options, linkLoadResult)` | ImportInstance |
| `ImportInstance Create(Document, View, ExternalResourceReference, DGNImportOptions, LinkLoadResult&)` | `ImportInstance.Create(document, DBView, resourceReference, options, linkLoadResult)` | ImportInstance |
| `ImportInstance Create(Document, ElementId, View)` | `ImportInstance.Create(document, typeId, DBView)` | ImportInstance |
| `ImportInstance Create(Document, View, ExternalResourceReference, DWGImportOptions, LinkLoadResult&)` | `ImportInstance.Create(document, DBView, resourceReference, options, linkLoadResult)` | ImportInstance |
| `ImportInstance Create(Document, View, String, DWGImportOptions, LinkLoadResult&)` | `ImportInstance.Create(document, DBView, path, options, linkLoadResult)` | ImportInstance |
| `FamilyElementVisibility GetVisibility()` | `importInstance.GetVisibility()` | FamilyElementVisibility |
| `Void SetVisibility(FamilyElementVisibility)` | `importInstance.SetVisibility(visibility)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

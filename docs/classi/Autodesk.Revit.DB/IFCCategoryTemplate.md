---
title: IFCCategoryTemplate
classe: Autodesk.Revit.DB.IFCCategoryTemplate
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# IFCCategoryTemplate

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `IFCCategoryTemplate CopyTemplate(Document, String)` | `iFCCategoryTemplate.CopyTemplate(document, copyTemplateName)` | IFCCategoryTemplate |
| `IFCCategoryTemplate Create(Document, String)` | `IFCCategoryTemplate.Create(document, name)` | IFCCategoryTemplate |
| `Void ExportToFile(Document, String)` | `iFCCategoryTemplate.ExportToFile(document, fileName)` | Void |
| `IFCCategoryTemplate FindByName(Document, String)` | `IFCCategoryTemplate.FindByName(document, name)` | IFCCategoryTemplate |
| `IFCCategoryTemplate GetActiveTemplate(Document)` | `IFCCategoryTemplate.GetActiveTemplate(document)` | IFCCategoryTemplate |
| `IDictionary<ExportIFCCategoryKey, ExportIFCCategoryInfo> GetCategoryMappingTable(Document)` | `iFCCategoryTemplate.GetCategoryMappingTable(document)` | IDictionary<ExportIFCCategoryKey, ExportIFCCategoryInfo> |
| `ExportIFCCategoryInfo GetMappingInfoById(Document, ElementId, CustomSubCategoryId)` | `iFCCategoryTemplate.GetMappingInfoById(document, categoryId, customSubCategoryId)` | ExportIFCCategoryInfo |
| `IFCCategoryTemplate GetOrCreateInSessionTemplate(Document)` | `IFCCategoryTemplate.GetOrCreateInSessionTemplate(document)` | IFCCategoryTemplate |
| `IFCCategoryTemplate ImportFromFile(Document, String, String)` | `IFCCategoryTemplate.ImportFromFile(document, fileName, templateName)` | IFCCategoryTemplate |
| `Boolean IsValidName(Document, String)` | `IFCCategoryTemplate.IsValidName(document, name)` | Boolean |
| `IList<String> ListNames(Document)` | `IFCCategoryTemplate.ListNames(document)` | IList<String> |
| `Void ResetActiveTemplate(Document)` | `IFCCategoryTemplate.ResetActiveTemplate(document)` | Void |
| `ExportIFCCategoryInfo ResetCategoryToDefault(ExportIFCCategoryKey)` | `iFCCategoryTemplate.ResetCategoryToDefault(categoryKey)` | ExportIFCCategoryInfo |
| `Void SetActiveTemplate(Document)` | `iFCCategoryTemplate.SetActiveTemplate(document)` | Void |
| `Void SetMappingInfo(ExportIFCCategoryKey, ExportIFCCategoryInfo)` | `iFCCategoryTemplate.SetMappingInfo(key, info)` | Void |
| `Void SetMappingInfo(IDictionary<ExportIFCCategoryKey, ExportIFCCategoryInfo>)` | `iFCCategoryTemplate.SetMappingInfo(newMap)` | Void |
| `Void UpdateCategoryList(Document)` | `iFCCategoryTemplate.UpdateCategoryList(document)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

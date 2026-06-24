---
title: LabelUtils
classe: Autodesk.Revit.DB.LabelUtils
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# LabelUtils

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `labelUtils.IsValidObject` | Boolean |
| `Void Dispose()` | `labelUtils.Dispose()` | Void |
| `String GetLabelFor(gbXMLBuildingType, Document)` | `LabelUtils.GetLabelFor(buildingType, document)` | String |
| `String GetLabelFor(PipeFlowState, Document)` | `LabelUtils.GetLabelFor(pipeFlowState, doc)` | String |
| `String GetLabelFor(PipeLossMethodType, Document)` | `LabelUtils.GetLabelFor(pipeLossMethodType, doc)` | String |
| `String GetLabelFor(DuctLossMethodType, Document)` | `LabelUtils.GetLabelFor(ductLossMethodType, doc)` | String |
| `String GetLabelFor(BuiltInCategory)` | `LabelUtils.GetLabelFor(builtInCategory)` | String |
| `String GetLabelFor(BuiltInParameter, LanguageType)` | `LabelUtils.GetLabelFor(builtInParam, language)` | String |
| `String GetLabelFor(BuiltInParameter)` | `LabelUtils.GetLabelFor(builtInParam)` | String |
| `String GetLabelForBuiltInParameter(ForgeTypeId, LanguageType)` | `LabelUtils.GetLabelForBuiltInParameter(parameterTypeId, language)` | String |
| `String GetLabelForBuiltInParameter(ForgeTypeId)` | `LabelUtils.GetLabelForBuiltInParameter(parameterTypeId)` | String |
| `String GetLabelForDiscipline(ForgeTypeId)` | `LabelUtils.GetLabelForDiscipline(disciplineTypeId)` | String |
| `String GetLabelForGroup(ForgeTypeId)` | `LabelUtils.GetLabelForGroup(groupTypeId)` | String |
| `String GetLabelForSpec(ForgeTypeId)` | `LabelUtils.GetLabelForSpec(specTypeId)` | String |
| `String GetLabelForSymbol(ForgeTypeId)` | `LabelUtils.GetLabelForSymbol(symbolTypeId)` | String |
| `String GetLabelForUnit(ForgeTypeId)` | `LabelUtils.GetLabelForUnit(unitTypeId)` | String |
| `String GetStructuralSectionShapeName(StructuralSectionShape)` | `LabelUtils.GetStructuralSectionShapeName(shape)` | String |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

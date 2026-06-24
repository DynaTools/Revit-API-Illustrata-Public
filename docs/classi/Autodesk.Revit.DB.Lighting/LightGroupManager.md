---
title: LightGroupManager
classe: Autodesk.Revit.DB.Lighting.LightGroupManager
namespace: Autodesk.Revit.DB.Lighting
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# LightGroupManager

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `lightGroupManager.IsValidObject` | Boolean |
| `LightGroup CreateGroup(String)` | `lightGroupManager.CreateGroup(name)` | LightGroup |
| `Void DeleteGroup(ElementId)` | `lightGroupManager.DeleteGroup(groupId)` | Void |
| `Void Dispose()` | `lightGroupManager.Dispose()` | Void |
| `IList<LightGroup> GetGroups()` | `lightGroupManager.GetGroups()` | IList<LightGroup> |
| `Double GetLightDimmer(ElementId, ElementId)` | `lightGroupManager.GetLightDimmer(viewId, lightId)` | Double |
| `LightGroupManager GetLightGroupManager(Document)` | `LightGroupManager.GetLightGroupManager(document)` | LightGroupManager |
| `Boolean IsLightGroupOn(ElementId, ElementId)` | `lightGroupManager.IsLightGroupOn(viewId, groupId)` | Boolean |
| `Boolean IsLightOn(ElementId, ElementId)` | `lightGroupManager.IsLightOn(viewId, lightId)` | Boolean |
| `Void SetLightDimmer(ElementId, ElementId, Double)` | `lightGroupManager.SetLightDimmer(viewId, lightId, dimmingValue)` | Void |
| `Void SetLightGroupOn(ElementId, ElementId, Boolean)` | `lightGroupManager.SetLightGroupOn(viewId, groupId, turnOn)` | Void |
| `Void SetLightOn(ElementId, ElementId, Boolean)` | `lightGroupManager.SetLightOn(viewId, lightId, turnOn)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

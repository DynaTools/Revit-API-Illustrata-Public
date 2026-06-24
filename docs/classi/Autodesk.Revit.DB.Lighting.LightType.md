---
title: LightType
classe: Autodesk.Revit.DB.Lighting.LightType
namespace: Autodesk.Revit.DB.Lighting
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 16
---

# LightType

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Color ColorFilter { get; set; }` | `lightType.ColorFilter` | Color |
| `LightDimmingColor DimmingColor { get; set; }` | `lightType.DimmingColor` | LightDimmingColor |
| `Boolean IsValidObject { get; }` | `lightType.IsValidObject` | Boolean |
| `Void Dispose()` | `lightType.Dispose()` | Void |
| `InitialColor GetInitialColor()` | `lightType.GetInitialColor()` | InitialColor |
| `InitialIntensity GetInitialIntensity()` | `lightType.GetInitialIntensity()` | InitialIntensity |
| `LightDistribution GetLightDistribution()` | `lightType.GetLightDistribution()` | LightDistribution |
| `LightShape GetLightShape()` | `lightType.GetLightShape()` | LightShape |
| `LightType GetLightType(Document, ElementId)` | `LightType.GetLightType(document, typeId)` | LightType |
| `LightType GetLightTypeFromInstance(Document, ElementId)` | `LightType.GetLightTypeFromInstance(document, instanceId)` | LightType |
| `LossFactor GetLossFactor()` | `lightType.GetLossFactor()` | LossFactor |
| `Void SetInitialColor(InitialColor)` | `lightType.SetInitialColor(initialColor)` | Void |
| `Void SetInitialIntensity(InitialIntensity)` | `lightType.SetInitialIntensity(initialIntensity)` | Void |
| `Void SetLightDistribution(LightDistribution)` | `lightType.SetLightDistribution(lightDistribution)` | Void |
| `Void SetLightShape(LightShape)` | `lightType.SetLightShape(lightShape)` | Void |
| `Void SetLossFactor(LossFactor)` | `lightType.SetLossFactor(lossFactor)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

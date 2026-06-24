---
title: ReinforcementSettings
classe: Autodesk.Revit.DB.Structure.ReinforcementSettings
namespace: Autodesk.Revit.DB.Structure
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 14
---

# ReinforcementSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean HostStructuralRebar { get; set; }` | `reinforcementSettings.HostStructuralRebar` | Boolean |
| `Boolean NumberVaryingLengthRebarsIndividually { get; set; }` | `reinforcementSettings.NumberVaryingLengthRebarsIndividually` | Boolean |
| `RebarPresentationMode RebarPresentationInSection { get; set; }` | `reinforcementSettings.RebarPresentationInSection` | RebarPresentationMode |
| `RebarPresentationMode RebarPresentationInView { get; set; }` | `reinforcementSettings.RebarPresentationInView` | RebarPresentationMode |
| `Boolean RebarShapeDefinesEndTreatments { get; set; }` | `reinforcementSettings.RebarShapeDefinesEndTreatments` | Boolean |
| `Boolean RebarShapeDefinesHooks { get; set; }` | `reinforcementSettings.RebarShapeDefinesHooks` | Boolean |
| `String RebarVaryingLengthNumberSuffix { get; set; }` | `reinforcementSettings.RebarVaryingLengthNumberSuffix` | String |
| `FabricRoundingManager GetFabricRoundingManager()` | `reinforcementSettings.GetFabricRoundingManager()` | FabricRoundingManager |
| `RebarRoundingManager GetRebarRoundingManager()` | `reinforcementSettings.GetRebarRoundingManager()` | RebarRoundingManager |
| `String GetReinforcementAbbreviationTag(ReinforcementAbbreviationTagType)` | `reinforcementSettings.GetReinforcementAbbreviationTag(tagType)` | String |
| `IList<ReinforcementAbbreviationTag> GetReinforcementAbbreviationTags(ReinforcementAbbreviationObjectType)` | `reinforcementSettings.GetReinforcementAbbreviationTags(objectType)` | IList<ReinforcementAbbreviationTag> |
| `ReinforcementSettings GetReinforcementSettings(Document)` | `ReinforcementSettings.GetReinforcementSettings(document)` | ReinforcementSettings |
| `Boolean IsEqual(ReinforcementSettings)` | `reinforcementSettings.IsEqual(other)` | Boolean |
| `Void SetReinforcementAbbreviationTag(ReinforcementAbbreviationTagType, String)` | `reinforcementSettings.SetReinforcementAbbreviationTag(tagType, abbreviationTag)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

---
title: Zone
classe: Autodesk.Revit.DB.Mechanical.Zone
namespace: Autodesk.Revit.DB.Mechanical
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 24
---

# Zone

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double Area { get; }` | `zone.Area` | Double |
| `CurveArray Boundary { get; }` | `zone.Boundary` | CurveArray |
| `Double CalculatedCoolingLoad { get; }` | `zone.CalculatedCoolingLoad` | Double |
| `Double CalculatedHeatingLoad { get; }` | `zone.CalculatedHeatingLoad` | Double |
| `Double CalculatedSupplyAirflow { get; }` | `zone.CalculatedSupplyAirflow` | Double |
| `Double CoolingAirTemperature { get; set; }` | `zone.CoolingAirTemperature` | Double |
| `Double CoolingSetPoint { get; set; }` | `zone.CoolingSetPoint` | Double |
| `Double DehumidificationSetPoint { get; set; }` | `zone.DehumidificationSetPoint` | Double |
| `Double GrossArea { get; }` | `zone.GrossArea` | Double |
| `Double GrossVolume { get; }` | `zone.GrossVolume` | Double |
| `Double HeatingAirTemperature { get; set; }` | `zone.HeatingAirTemperature` | Double |
| `Double HeatingSetPoint { get; set; }` | `zone.HeatingSetPoint` | Double |
| `Double HumidificationSetPoint { get; set; }` | `zone.HumidificationSetPoint` | Double |
| `Boolean IsDefaultZone { get; set; }` | `zone.IsDefaultZone` | Boolean |
| `String Name { get; set; }` | `zone.Name` | String |
| `Double Perimeter { get; }` | `zone.Perimeter` | Double |
| `Phase Phase { get; }` | `zone.Phase` | Phase |
| `ServiceType ServiceType { get; set; }` | `zone.ServiceType` | ServiceType |
| `SpaceSet Spaces { get; }` | `zone.Spaces` | SpaceSet |
| `Double Volume { get; }` | `zone.Volume` | Double |
| `Boolean AddSpaces(SpaceSet)` | `zone.AddSpaces(spaces)` | Boolean |
| `Zone CreateAreaBasedLoad(Document, String, ElementId, ElementId)` | `Zone.CreateAreaBasedLoad(doc, name, levelId, phaseId)` | Zone |
| `ZoneElementDomainData GetDomainData()` | `zone.GetDomainData()` | ZoneElementDomainData |
| `Boolean RemoveSpaces(SpaceSet)` | `zone.RemoveSpaces(spaces)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

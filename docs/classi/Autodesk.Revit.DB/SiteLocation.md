---
title: SiteLocation
classe: Autodesk.Revit.DB.SiteLocation
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.ElementType
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# SiteLocation

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double Elevation { get; }` | `siteLocation.Elevation` | Double |
| `String GeoCoordinateSystemDefinition { get; }` | `siteLocation.GeoCoordinateSystemDefinition` | String |
| `String GeoCoordinateSystemId { get; }` | `siteLocation.GeoCoordinateSystemId` | String |
| `Double Latitude { get; set; }` | `siteLocation.Latitude` | Double |
| `Double Longitude { get; set; }` | `siteLocation.Longitude` | Double |
| `String PlaceName { get; set; }` | `siteLocation.PlaceName` | String |
| `Double TimeZone { get; set; }` | `siteLocation.TimeZone` | Double |
| `String WeatherStationName { get; }` | `siteLocation.WeatherStationName` | String |
| `DateTime ConvertFromProjectTime(DateTime)` | `siteLocation.ConvertFromProjectTime(projectTime)` | DateTime |
| `DateTime ConvertToProjectTime(DateTime)` | `siteLocation.ConvertToProjectTime(inputTime)` | DateTime |
| `Boolean IsCompatibleWith(SiteLocation)` | `siteLocation.IsCompatibleWith(otherSiteLocation)` | Boolean |
| `Void SetGeoCoordinateSystem(String)` | `siteLocation.SetGeoCoordinateSystem(coordSystem)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

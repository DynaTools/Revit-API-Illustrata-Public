---
title: SunAndShadowSettings
classe: Autodesk.Revit.DB.SunAndShadowSettings
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 36
---

# SunAndShadowSettings

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Double ActiveFrame { get; set; }` | `sunAndShadowSettings.ActiveFrame` | Double |
| `DateTime ActiveFrameTime { get; }` | `sunAndShadowSettings.ActiveFrameTime` | DateTime |
| `Double Altitude { get; set; }` | `sunAndShadowSettings.Altitude` | Double |
| `Double Azimuth { get; set; }` | `sunAndShadowSettings.Azimuth` | Double |
| `DateTime EndDateAndTime { get; set; }` | `sunAndShadowSettings.EndDateAndTime` | DateTime |
| `Double GroundPlaneHeight { get; }` | `sunAndShadowSettings.GroundPlaneHeight` | Double |
| `ElementId GroundPlaneLevelId { get; set; }` | `sunAndShadowSettings.GroundPlaneLevelId` | ElementId |
| `Double Latitude { get; }` | `sunAndShadowSettings.Latitude` | Double |
| `Double Longitude { get; }` | `sunAndShadowSettings.Longitude` | Double |
| `Double NumberOfFrames { get; }` | `sunAndShadowSettings.NumberOfFrames` | Double |
| `ElementId ProjectLocationId { get; }` | `sunAndShadowSettings.ProjectLocationId` | ElementId |
| `String ProjectLocationName { get; }` | `sunAndShadowSettings.ProjectLocationName` | String |
| `Boolean RelativeToView { get; set; }` | `sunAndShadowSettings.RelativeToView` | Boolean |
| `Boolean SharesSettings { get; set; }` | `sunAndShadowSettings.SharesSettings` | Boolean |
| `DateTime StartDateAndTime { get; set; }` | `sunAndShadowSettings.StartDateAndTime` | DateTime |
| `SunAndShadowType SunAndShadowType { get; set; }` | `sunAndShadowSettings.SunAndShadowType` | SunAndShadowType |
| `Boolean SunriseToSunset { get; set; }` | `sunAndShadowSettings.SunriseToSunset` | Boolean |
| `SunStudyTimeInterval TimeInterval { get; set; }` | `sunAndShadowSettings.TimeInterval` | SunStudyTimeInterval |
| `Double TimeZone { get; }` | `sunAndShadowSettings.TimeZone` | Double |
| `Boolean UsesDST { get; }` | `sunAndShadowSettings.UsesDST` | Boolean |
| `Boolean UsesGroundPlane { get; set; }` | `sunAndShadowSettings.UsesGroundPlane` | Boolean |
| `Boolean Visible { get; set; }` | `sunAndShadowSettings.Visible` | Boolean |
| `Double CalculateTimeZone(Double, Double)` | `SunAndShadowSettings.CalculateTimeZone(latitude, longitude)` | Double |
| `Void FitToModel()` | `sunAndShadowSettings.FitToModel()` | Void |
| `Element GetActiveSunAndShadowSettings(Document)` | `SunAndShadowSettings.GetActiveSunAndShadowSettings(aDocument)` | Element |
| `Double GetFrameAltitude(Double)` | `sunAndShadowSettings.GetFrameAltitude(frame)` | Double |
| `Double GetFrameAzimuth(Double)` | `sunAndShadowSettings.GetFrameAzimuth(frame)` | Double |
| `DateTime GetFrameTime(Double)` | `sunAndShadowSettings.GetFrameTime(frame)` | DateTime |
| `String GetMatchingPreset()` | `sunAndShadowSettings.GetMatchingPreset()` | String |
| `DateTime GetSunrise(DateTime)` | `sunAndShadowSettings.GetSunrise(date)` | DateTime |
| `DateTime GetSunset(DateTime)` | `sunAndShadowSettings.GetSunset(date)` | DateTime |
| `Boolean IsAfterStartDateAndTime(DateTime)` | `sunAndShadowSettings.IsAfterStartDateAndTime(time)` | Boolean |
| `Boolean IsBeforeEndDateAndTime(DateTime)` | `sunAndShadowSettings.IsBeforeEndDateAndTime(time)` | Boolean |
| `Boolean IsFrameValid(Double)` | `sunAndShadowSettings.IsFrameValid(frame)` | Boolean |
| `Boolean IsGroundPlaneLevelValid(ElementId)` | `sunAndShadowSettings.IsGroundPlaneLevelValid(levelId)` | Boolean |
| `Boolean IsTimeIntervalValid(SunStudyTimeInterval)` | `sunAndShadowSettings.IsTimeIntervalValid(interval)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

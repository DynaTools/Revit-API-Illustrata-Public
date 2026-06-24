---
title: PrintSetup
classe: Autodesk.Revit.DB.PrintSetup
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 7
---

# PrintSetup

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `IPrintSetting CurrentPrintSetting { get; set; }` | `printSetup.CurrentPrintSetting` | IPrintSetting |
| `InSessionPrintSetting InSession { get; }` | `printSetup.InSession` | InSessionPrintSetting |
| `Boolean Delete()` | `printSetup.Delete()` | Boolean |
| `Boolean Rename(String)` | `printSetup.Rename(newName)` | Boolean |
| `Void Revert()` | `printSetup.Revert()` | Void |
| `Boolean Save()` | `printSetup.Save()` | Boolean |
| `Boolean SaveAs(String)` | `printSetup.SaveAs(newName)` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

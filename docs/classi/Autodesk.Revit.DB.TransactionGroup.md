---
title: TransactionGroup
classe: Autodesk.Revit.DB.TransactionGroup
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# TransactionGroup

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsFailureHandlingForcedModal { get; set; }` | `transactionGroup.IsFailureHandlingForcedModal` | Boolean |
| `Boolean IsValidObject { get; }` | `transactionGroup.IsValidObject` | Boolean |
| `TransactionStatus Assimilate()` | `transactionGroup.Assimilate()` | TransactionStatus |
| `TransactionStatus Commit()` | `transactionGroup.Commit()` | TransactionStatus |
| `Void Dispose()` | `transactionGroup.Dispose()` | Void |
| `String GetName()` | `transactionGroup.GetName()` | String |
| `TransactionStatus GetStatus()` | `transactionGroup.GetStatus()` | TransactionStatus |
| `Boolean HasEnded()` | `transactionGroup.HasEnded()` | Boolean |
| `Boolean HasStarted()` | `transactionGroup.HasStarted()` | Boolean |
| `TransactionStatus RollBack()` | `transactionGroup.RollBack()` | TransactionStatus |
| `Void SetName(String)` | `transactionGroup.SetName(name)` | Void |
| `TransactionStatus Start(String)` | `transactionGroup.Start(transGroupName)` | TransactionStatus |
| `TransactionStatus Start()` | `transactionGroup.Start()` | TransactionStatus |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

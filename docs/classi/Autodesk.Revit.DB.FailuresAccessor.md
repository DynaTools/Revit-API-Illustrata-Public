---
title: FailuresAccessor
classe: Autodesk.Revit.DB.FailuresAccessor
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 32
---

# FailuresAccessor

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `failuresAccessor.IsValidObject` | Boolean |
| `Boolean CanCommitPendingTransaction()` | `failuresAccessor.CanCommitPendingTransaction()` | Boolean |
| `Boolean CanRollBackPendingTransaction()` | `failuresAccessor.CanRollBackPendingTransaction()` | Boolean |
| `TransactionStatus CommitPendingTransaction()` | `failuresAccessor.CommitPendingTransaction()` | TransactionStatus |
| `Void DeleteAllWarnings()` | `failuresAccessor.DeleteAllWarnings()` | Void |
| `Void DeleteElements(IList<ElementId>)` | `failuresAccessor.DeleteElements(idsToDelete)` | Void |
| `Void DeleteWarning(FailureMessageAccessor)` | `failuresAccessor.DeleteWarning(failure)` | Void |
| `Void Dispose()` | `failuresAccessor.Dispose()` | Void |
| `IList<FailureResolutionType> GetAttemptedResolutionTypes(FailureMessageAccessor)` | `failuresAccessor.GetAttemptedResolutionTypes(failure)` | IList<FailureResolutionType> |
| `Document GetDocument()` | `failuresAccessor.GetDocument()` | Document |
| `FailureHandlingOptions GetFailureHandlingOptions()` | `failuresAccessor.GetFailureHandlingOptions()` | FailureHandlingOptions |
| `IList<FailureMessageAccessor> GetFailureMessages(FailureSeverity)` | `failuresAccessor.GetFailureMessages(severity)` | IList<FailureMessageAccessor> |
| `IList<FailureMessageAccessor> GetFailureMessages()` | `failuresAccessor.GetFailureMessages()` | IList<FailureMessageAccessor> |
| `FailureSeverity GetSeverity()` | `failuresAccessor.GetSeverity()` | FailureSeverity |
| `String GetTransactionName()` | `failuresAccessor.GetTransactionName()` | String |
| `Boolean IsActive()` | `failuresAccessor.IsActive()` | Boolean |
| `Boolean IsElementsDeletionPermitted(IList<ElementId>, String&)` | `failuresAccessor.IsElementsDeletionPermitted(idsToDelete, reason)` | Boolean |
| `Boolean IsElementsDeletionPermitted(IList<ElementId>)` | `failuresAccessor.IsElementsDeletionPermitted(idsToDelete)` | Boolean |
| `Boolean IsElementsDeletionPermitted()` | `failuresAccessor.IsElementsDeletionPermitted()` | Boolean |
| `Boolean IsFailureResolutionPermitted(FailureMessageAccessor, FailureResolutionType)` | `failuresAccessor.IsFailureResolutionPermitted(failure, resolutionType)` | Boolean |
| `Boolean IsFailureResolutionPermitted(FailureMessageAccessor)` | `failuresAccessor.IsFailureResolutionPermitted(failure)` | Boolean |
| `Boolean IsFailureResolutionPermitted()` | `failuresAccessor.IsFailureResolutionPermitted()` | Boolean |
| `Boolean IsPending()` | `failuresAccessor.IsPending()` | Boolean |
| `Boolean IsTransactionBeingCommitted()` | `failuresAccessor.IsTransactionBeingCommitted()` | Boolean |
| `Void JournalFailures(IList<FailureMessageAccessor>)` | `failuresAccessor.JournalFailures(failures)` | Void |
| `Void PostFailure(FailureMessage)` | `failuresAccessor.PostFailure(failure)` | Void |
| `Void ReplaceFailures(FailureMessage)` | `failuresAccessor.ReplaceFailures(failure)` | Void |
| `Void ResolveFailure(FailureMessageAccessor)` | `failuresAccessor.ResolveFailure(failure)` | Void |
| `Void ResolveFailures(IList<FailureMessageAccessor>)` | `failuresAccessor.ResolveFailures(failures)` | Void |
| `TransactionStatus RollBackPendingTransaction()` | `failuresAccessor.RollBackPendingTransaction()` | TransactionStatus |
| `Void SetFailureHandlingOptions(FailureHandlingOptions)` | `failuresAccessor.SetFailureHandlingOptions(options)` | Void |
| `Void SetTransactionName(String)` | `failuresAccessor.SetTransactionName(transactionName)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

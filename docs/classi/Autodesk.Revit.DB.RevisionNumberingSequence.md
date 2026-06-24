---
title: RevisionNumberingSequence
classe: Autodesk.Revit.DB.RevisionNumberingSequence
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 12
---

# RevisionNumberingSequence

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `RevisionNumberType NumberType { get; }` | `revisionNumberingSequence.NumberType` | RevisionNumberType |
| `String SequenceName { get; set; }` | `revisionNumberingSequence.SequenceName` | String |
| `RevisionNumberingSequence CreateAlphanumericSequence(Document, String, AlphanumericRevisionSettings)` | `RevisionNumberingSequence.CreateAlphanumericSequence(document, name, settings)` | RevisionNumberingSequence |
| `RevisionNumberingSequence CreateNumericSequence(Document, String, NumericRevisionSettings)` | `RevisionNumberingSequence.CreateNumericSequence(document, name, settings)` | RevisionNumberingSequence |
| `ISet<ElementId> GetAllRevisionNumberingSequences(Document)` | `RevisionNumberingSequence.GetAllRevisionNumberingSequences(document)` | ISet<ElementId> |
| `AlphanumericRevisionSettings GetAlphanumericRevisionSettings()` | `revisionNumberingSequence.GetAlphanumericRevisionSettings()` | AlphanumericRevisionSettings |
| `NumericRevisionSettings GetNumericRevisionSettings()` | `revisionNumberingSequence.GetNumericRevisionSettings()` | NumericRevisionSettings |
| `Boolean HasValidAlphanumericRevisionSettings()` | `revisionNumberingSequence.HasValidAlphanumericRevisionSettings()` | Boolean |
| `Boolean HasValidNumericRevisionSettings()` | `revisionNumberingSequence.HasValidNumericRevisionSettings()` | Boolean |
| `Boolean HasValidRevisionSettingsForNumberType()` | `revisionNumberingSequence.HasValidRevisionSettingsForNumberType()` | Boolean |
| `Void SetAlphanumericRevisionSettings(AlphanumericRevisionSettings)` | `revisionNumberingSequence.SetAlphanumericRevisionSettings(settings)` | Void |
| `Void SetNumericRevisionSettings(NumericRevisionSettings)` | `revisionNumberingSequence.SetNumericRevisionSettings(settings)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

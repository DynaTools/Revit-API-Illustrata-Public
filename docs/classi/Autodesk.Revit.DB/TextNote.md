---
title: TextNote
classe: Autodesk.Revit.DB.TextNote
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.TextElement
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 13
---

# TextNote

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Int32 LeaderCount { get; }` | `textNote.LeaderCount` | Int32 |
| `LeaderAtachement LeaderLeftAttachment { get; set; }` | `textNote.LeaderLeftAttachment` | LeaderAtachement |
| `LeaderAtachement LeaderRightAttachment { get; set; }` | `textNote.LeaderRightAttachment` | LeaderAtachement |
| `TextNoteType TextNoteType { get; set; }` | `textNote.TextNoteType` | TextNoteType |
| `Leader AddLeader(TextNoteLeaderTypes)` | `textNote.AddLeader(leaderType)` | Leader |
| `TextNote Create(Document, ElementId, XYZ, Double, String, TextNoteOptions)` | `TextNote.Create(document, viewId, position, width, text, options)` | TextNote |
| `TextNote Create(Document, ElementId, XYZ, Double, String, ElementId)` | `TextNote.Create(document, viewId, position, width, text, typeId)` | TextNote |
| `TextNote Create(Document, ElementId, XYZ, String, TextNoteOptions)` | `TextNote.Create(document, viewId, position, text, options)` | TextNote |
| `TextNote Create(Document, ElementId, XYZ, String, ElementId)` | `TextNote.Create(document, viewId, position, text, typeId)` | TextNote |
| `FormattedText GetFormattedText()` | `textNote.GetFormattedText()` | FormattedText |
| `IList<Leader> GetLeaders()` | `textNote.GetLeaders()` | IList<Leader> |
| `Void RemoveLeaders()` | `textNote.RemoveLeaders()` | Void |
| `Void SetFormattedText(FormattedText)` | `textNote.SetFormattedText(formattedText)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

---
title: FormattedText
classe: Autodesk.Revit.DB.FormattedText
namespace: Autodesk.Revit.DB
eredita: System.Object
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 41
---

# FormattedText

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean IsValidObject { get; }` | `formattedText.IsValidObject` | Boolean |
| `TextRange AsTextRange()` | `formattedText.AsTextRange()` | TextRange |
| `Void Dispose()` | `formattedText.Dispose()` | Void |
| `TextRange Find(String, Int32, Boolean, Boolean)` | `formattedText.Find(searchString, startIndex, matchCase, matchWholeWord)` | TextRange |
| `FormatStatus GetAllCapsStatus()` | `formattedText.GetAllCapsStatus()` | FormatStatus |
| `FormatStatus GetAllCapsStatus(TextRange)` | `formattedText.GetAllCapsStatus(textRange)` | FormatStatus |
| `FormatStatus GetBoldStatus()` | `formattedText.GetBoldStatus()` | FormatStatus |
| `FormatStatus GetBoldStatus(TextRange)` | `formattedText.GetBoldStatus(textRange)` | FormatStatus |
| `Int32 GetIndentLevel(TextRange)` | `formattedText.GetIndentLevel(textRange)` | Int32 |
| `FormatStatus GetItalicStatus()` | `formattedText.GetItalicStatus()` | FormatStatus |
| `FormatStatus GetItalicStatus(TextRange)` | `formattedText.GetItalicStatus(textRange)` | FormatStatus |
| `Int32 GetListStartNumber(TextRange)` | `formattedText.GetListStartNumber(textRange)` | Int32 |
| `ListType GetListType(TextRange)` | `formattedText.GetListType(textRange)` | ListType |
| `Int32 GetMaximumIndentLevel()` | `formattedText.GetMaximumIndentLevel()` | Int32 |
| `Int32 GetMaximumListStartNumber()` | `formattedText.GetMaximumListStartNumber()` | Int32 |
| `Int32 GetMinimumListStartNumber()` | `formattedText.GetMinimumListStartNumber()` | Int32 |
| `String GetPlainText(TextRange)` | `formattedText.GetPlainText(textRange)` | String |
| `String GetPlainText()` | `formattedText.GetPlainText()` | String |
| `FormatStatus GetSubscriptStatus()` | `formattedText.GetSubscriptStatus()` | FormatStatus |
| `FormatStatus GetSubscriptStatus(TextRange)` | `formattedText.GetSubscriptStatus(textRange)` | FormatStatus |
| `FormatStatus GetSuperscriptStatus()` | `formattedText.GetSuperscriptStatus()` | FormatStatus |
| `FormatStatus GetSuperscriptStatus(TextRange)` | `formattedText.GetSuperscriptStatus(textRange)` | FormatStatus |
| `FormatStatus GetUnderlineStatus()` | `formattedText.GetUnderlineStatus()` | FormatStatus |
| `FormatStatus GetUnderlineStatus(TextRange)` | `formattedText.GetUnderlineStatus(textRange)` | FormatStatus |
| `Void SetAllCapsStatus(Boolean)` | `formattedText.SetAllCapsStatus(isAllCaps)` | Void |
| `Void SetAllCapsStatus(TextRange, Boolean)` | `formattedText.SetAllCapsStatus(textRange, isAllCaps)` | Void |
| `Void SetBoldStatus(Boolean)` | `formattedText.SetBoldStatus(isBold)` | Void |
| `Void SetBoldStatus(TextRange, Boolean)` | `formattedText.SetBoldStatus(textRange, isBold)` | Void |
| `Void SetIndentLevel(TextRange, Int32)` | `formattedText.SetIndentLevel(textRange, level)` | Void |
| `Void SetItalicStatus(Boolean)` | `formattedText.SetItalicStatus(isItalic)` | Void |
| `Void SetItalicStatus(TextRange, Boolean)` | `formattedText.SetItalicStatus(textRange, isItalic)` | Void |
| `Void SetListStartNumber(TextRange, Int32)` | `formattedText.SetListStartNumber(textRange, value)` | Void |
| `Void SetListType(TextRange, ListType)` | `formattedText.SetListType(textRange, listType)` | Void |
| `Void SetPlainText(TextRange, String)` | `formattedText.SetPlainText(textRange, plainText)` | Void |
| `Void SetPlainText(String)` | `formattedText.SetPlainText(plainText)` | Void |
| `Void SetSubscriptStatus(Boolean)` | `formattedText.SetSubscriptStatus(isSubscript)` | Void |
| `Void SetSubscriptStatus(TextRange, Boolean)` | `formattedText.SetSubscriptStatus(textRange, isSubscript)` | Void |
| `Void SetSuperscriptStatus(Boolean)` | `formattedText.SetSuperscriptStatus(isSuperscript)` | Void |
| `Void SetSuperscriptStatus(TextRange, Boolean)` | `formattedText.SetSuperscriptStatus(textRange, isSuperscript)` | Void |
| `Void SetUnderlineStatus(Boolean)` | `formattedText.SetUnderlineStatus(isUnderlined)` | Void |
| `Void SetUnderlineStatus(TextRange, Boolean)` | `formattedText.SetUnderlineStatus(textRange, isUnderlined)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

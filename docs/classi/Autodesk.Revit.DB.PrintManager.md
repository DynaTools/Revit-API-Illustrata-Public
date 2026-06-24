---
title: PrintManager
classe: Autodesk.Revit.DB.PrintManager
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.APIObject
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 17
---

# PrintManager

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Boolean Collate { get; set; }` | `printManager.Collate` | Boolean |
| `Boolean CombinedFile { get; set; }` | `printManager.CombinedFile` | Boolean |
| `Int32 CopyNumber { get; set; }` | `printManager.CopyNumber` | Int32 |
| `VirtualPrinterType IsVirtual { get; }` | `printManager.IsVirtual` | VirtualPrinterType |
| `PaperSizeSet PaperSizes { get; }` | `printManager.PaperSizes` | PaperSizeSet |
| `PaperSourceSet PaperSources { get; }` | `printManager.PaperSources` | PaperSourceSet |
| `String PrinterName { get; }` | `printManager.PrinterName` | String |
| `Boolean PrintOrderReverse { get; set; }` | `printManager.PrintOrderReverse` | Boolean |
| `PrintRange PrintRange { get; set; }` | `printManager.PrintRange` | PrintRange |
| `PrintSetup PrintSetup { get; }` | `printManager.PrintSetup` | PrintSetup |
| `Boolean PrintToFile { get; set; }` | `printManager.PrintToFile` | Boolean |
| `String PrintToFileName { get; set; }` | `printManager.PrintToFileName` | String |
| `ViewSheetSetting ViewSheetSetting { get; }` | `printManager.ViewSheetSetting` | ViewSheetSetting |
| `Void Apply()` | `printManager.Apply()` | Void |
| `Void SelectNewPrintDriver(String)` | `printManager.SelectNewPrintDriver(strPrinterName)` | Void |
| `Boolean SubmitPrint(View)` | `printManager.SubmitPrint(view)` | Boolean |
| `Boolean SubmitPrint()` | `printManager.SubmitPrint()` | Boolean |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```

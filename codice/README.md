# Codice - Revit API Illustrata in Python

Tutto il codice del libro, **un file per ogni blocco**, pronto da copiare e
incollare nel **RevitPythonShell**. Estratto dal sorgente: l'indentazione e
esatta (copiare dal PDF la perde).

Autore: **Paulo Giavoni**

## Come funziona

Nel libro, sotto ogni blocco di codice, il selo rosso **</> Codice P.C.n**
porta al file corrispondente qui. Il nome del file e `codice-P-C-n.py`:

- **P** = parte, **C** = capitolo, **n** = numero del codice nel capitolo.
- Esempio: *Codice 6.4.2* -> `codice-6-4-2.py`.

L'`Indice dei codici` in fondo al libro elenca tutti i codici con la pagina.

I file qui sono **sincronizzati** sul repository pubblico
[DynaTools/Revit-API-Illustrata-Public](https://github.com/DynaTools/Revit-API-Illustrata-Public/tree/main/codice)
dal workflow `.github/workflows/sync-codice.yml` a ogni push che tocca questa
cartella. I badge "Codice P.C.n" del PDF scaricano i file da lì.

> **CPython 3.** I blocchi con `openpyxl` girano solo sull'engine CPython 3
> di pyRevit (prima riga `#! python3` e libreria installata).

> **Selezione -> NON-MODALE.** Gli script con `PickObject` / `PickObjects`
> vanno eseguiti con il RevitPythonShell in modalita **non-modale**, altrimenti
> il clic non raggiunge il modello.

Totale: 139 file (un blocco per file).
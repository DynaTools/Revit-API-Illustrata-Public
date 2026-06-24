# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 5.2.3  |  Capitolo 5.2 - Il cammino verso il C#
# Sezione: Visual Studio e il .addin

[Transaction(TransactionMode.Manual)]
public class RiempireCommenti : IExternalCommand
{
    public Result Execute(ExternalCommandData dati,
                          ref string msg, ElementSet elementi)
    {
        Document doc = dati.Application.ActiveUIDocument.Document;
        // ... il Livello 4 in C#, della sezione precedente ...
        return Result.Succeeded;
    }
}

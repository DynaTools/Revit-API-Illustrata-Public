# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 4.1.2  |  Capitolo 4.1 - Transazioni: il contratto prima di mettere mano
# Sezione: Anatomia del contratto: Start, Commit, RollBack

t = Transaction(doc, "Riempire Commenti")   # 1. redigere il contratto
t.Start()                                   # 2. aprire
# ... le modifiche avvengono qui ...
t.Commit()                                  # 3a. firmare (rendere effettivo)
# oppure: t.RollBack()                      # 3b. strappare (disfare tutto)

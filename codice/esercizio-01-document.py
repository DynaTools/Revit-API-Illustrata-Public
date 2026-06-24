print("Titolo    :", doc.Title)
print("Percorso  :", doc.PathName or "(non salvato)")
print("Condiviso :", doc.IsWorkshared)
print("Vista att.:", doc.ActiveView.Name)

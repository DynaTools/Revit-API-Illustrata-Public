# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 6.1.5  |  Capitolo 6.1 - I primitivi geometrici
# Sezione: Il bounding box orientato (OBB) - Transform

from Autodesk.Revit.DB import XYZ

FT_M = 0.3048

# Per una FamilyInstance la Transform descrive il frame locale
fi    = element                           # assumiamo FamilyInstance
tf    = fi.GetTransform()

# Origine e assi locali in coordinate globali
origin = tf.Origin
u_hat  = tf.BasisX                        # asse longitudinale (normalizzato)
v_hat  = tf.BasisY                        # asse trasversale
w_hat  = tf.BasisZ                        # asse verticale

print("Origine: ({:.3f}, {:.3f}, {:.3f}) m".format(
    origin.X*FT_M, origin.Y*FT_M, origin.Z*FT_M))
print("u: ({:.3f}, {:.3f}, {:.3f})".format(u_hat.X, u_hat.Y, u_hat.Z))
print("v: ({:.3f}, {:.3f}, {:.3f})".format(v_hat.X, v_hat.Y, v_hat.Z))
print("w: ({:.3f}, {:.3f}, {:.3f})".format(w_hat.X, w_hat.Y, w_hat.Z))

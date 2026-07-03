# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.13.3  |  Capitolo 7.13 - Il percorso minimo nella rete
# Sezione: Il verdetto - i due itinerari a confronto

# il grafo costruito ai passi 1-2 (qui esplicitato come nella figura)
adj = {
    "A": [("C", 6.0), ("D", 4.0)],
    "C": [("A", 6.0), ("B", 12.0), ("D", 5.0)],
    "B": [("C", 12.0), ("E", 4.0)],
    "D": [("A", 4.0), ("E", 7.0), ("C", 5.0)],
    "E": [("D", 7.0), ("B", 4.0)],
}

# percorso ottimo (Dijkstra esplora tutto)
lung, cammino = dijkstra(adj, "A", "B")

# itinerario "piu' dritto in pianta": A -> C -> B
alt = 6.0 + 12.0                   # A-C (6) + C-B interrato (12)

print("Itinerario ottimo:  {}  =  {:.1f} m".format(
    " -> ".join(cammino), lung))
print("Piu' dritto in pianta: A -> C -> B  =  {:.1f} m".format(alt))
print("---")
print("Risparmio: {:.1f} m ({:.0f}%) di cavo".format(
    alt - lung, 100.0 * (alt - lung) / alt))

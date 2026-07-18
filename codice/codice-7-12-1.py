# -*- coding: utf-8 -*-
# Revit API Illustrata in Python - Paulo Giavoni
# Codice 7.12.1  |  Capitolo 7.12 - Il percorso minimo nella rete
# Sezione: Passo 3 - Dijkstra in Python

import heapq

# Dijkstra su un grafo pesato.
# adj[u] = lista di (v, peso) per ogni arco u->v (qui non orientato).
def dijkstra(adj, sorg, dest):
    dist = dict((n, float("inf")) for n in adj)   # migliore distanza nota
    prev = dict((n, None) for n in adj)            # predecessore nel cammino
    dist[sorg] = 0.0
    pq = [(0.0, sorg)]                             # coda di priorita'
    while pq:
        d, u = heapq.heappop(pq)                   # nodo aperto piu' vicino
        if d > dist[u]:
            continue                               # voce vecchia: scartala
        if u == dest:
            break                                  # ottimo per dest gia' certo
        for v, w in adj[u]:                        # rilassa i vicini di u
            nd = d + w                             # dist(u) + w(u,v)
            if nd < dist[v]:                       # strada migliore per v?
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))
    # ricostruzione del cammino da dest a ritroso fino a sorg
    cammino, n = [], dest
    while n is not None:
        cammino.append(n)
        n = prev[n]
    cammino.reverse()
    return dist[dest], cammino

# la rete della figura (nodo: lista di (vicino, lunghezza in metri))
adj = {
    "A": [("C", 6.0), ("D", 4.0)],
    "C": [("A", 6.0), ("B", 12.0), ("D", 5.0)],
    "B": [("C", 12.0), ("E", 4.0)],
    "D": [("A", 4.0), ("E", 7.0), ("C", 5.0)],
    "E": [("D", 7.0), ("B", 4.0)],
}

lung, cammino = dijkstra(adj, "A", "B")
print("Percorso minimo: {}".format(" -> ".join(cammino)))
print("Lunghezza cavo: {:.1f} m".format(lung))

GRAPH = {
    "1" : { "2": 2, "3": 5, "4": 3, "6":8},
    "2" : {"1": 2, "3": 1},
    "3" : {"1": 5, "2": 1, "6": 4},
    "4" : {"1": 3, "5": 1},
    "5" : {"4": 1, "6": 4},
    "6" : {"1": 8, "3": 4, "5": 5}
    }

D = {k: 20 for k in GRAPH.keys()}
print(D)
P = {k: -1 for k in GRAPH.keys()}
Q = [k for k in GRAPH.keys()]

start = "2"
D[start] = 0

while Q:
    U = Q.pop(0)
    for V in Q:
        if GRAPH[U[0]].get(V):
            A = D[U] + GRAPH[U][V]
            
            if A < D[V]:
                D[V] = A
                P[V] = U

print(D)
print(P)



graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

def heuristic(n):
    h_values = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
    return h_values[n]


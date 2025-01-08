import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

def heuristic(n):
    h_values = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
    return h_values[n]

def aStar(graph, start, goal, h) :
    open_set = []
    heapq.heappush(open_set, (h(start), start))
    
    g_cost = {start : 0}
    parent = {start : None}
    closed_set = set()
    
    while open_set:
        
        current_f , current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current is not None :
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        closed_set.add(current)
        
        for neighbor, cost in graph[current]:
            if neighbor in closed_set:
                continue  

            tentative_g = g_cost[current] + cost

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_score = tentative_g + h(neighbor)  

                heapq.heappush(open_set, (f_score, neighbor))
                parent[neighbor] = current
    
    return None

path = aStar(graph, 'A', 'D', heuristic)

print(path)
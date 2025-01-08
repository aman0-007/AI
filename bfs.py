from q import Queue

city_map = {
    "Delhi": ["Jaipur", "Lucknow", "Chandigarh", "Agra"],
    "Jaipur": ["Delhi", "Ahmedabad", "Indore", "Udaipur"],
    "Lucknow": ["Delhi", "Varanasi", "Kanpur", "Agra"],
    "Ahmedabad": ["Jaipur", "Mumbai", "Surat", "Vadodara"],
    "Varanasi": ["Lucknow", "Kolkata", "Patna", "Raipur"],
    "Mumbai": ["Ahmedabad", "Pune", "Nagpur", "Goa"],
    "Kolkata": ["Varanasi", "Chennai", "Bhubaneshwar", "Ranchi"],
    "Pune": ["Mumbai", "Bangalore", "Hyderabad", "Goa"],
    "Chennai": ["Kolkata", "Bangalore", "Hyderabad", "Coimbatore"],
    "Bangalore": ["Pune", "Chennai", "Hyderabad", "Mysore"],
    "Chandigarh": ["Delhi", "Amritsar", "Shimla"],
    "Agra": ["Delhi", "Lucknow", "Kanpur"],
    "Indore": ["Jaipur", "Udaipur", "Mumbai"],
    "Udaipur": ["Jaipur", "Indore", "Surat"],
    "Surat": ["Ahmedabad", "Indore", "Mumbai"],
    "Vadodara": ["Ahmedabad", "Surat", "Raipur"],
    "Patna": ["Varanasi", "Ranchi", "Raipur"],
    "Raipur": ["Varanasi", "Vadodara", "Patna"],
    "Nagpur": ["Mumbai", "Hyderabad", "Bhopal"],
    "Goa": ["Mumbai", "Pune", "Bangalore"],
    "Hyderabad": ["Pune", "Chennai", "Bangalore", "Nagpur"],
    "Amritsar": ["Chandigarh", "Delhi"],
    "Shimla": ["Chandigarh", "Delhi"],
    "Bhubaneshwar": ["Kolkata", "Ranchi"],
    "Ranchi": ["Kolkata", "Patna", "Bhubaneshwar"]
}


def BFS(graph,src,dst):
    q = Queue()
    
    q.enqueue((src,[src]))
    visited = set()
    
    while not q.isEmpty():
        currentCity, path = q.dequeue()
        
        if currentCity == dst:
            return path
        
        visited.add(currentCity)
        
        for neighbour in graph.get(currentCity, []):
            if neighbour not in visited:
                q.enqueue((neighbour, path + [neighbour]))
    return None


path = BFS(city_map, 'Delhi', 'Patna')

if path:
    print("Shortest Path found:", " -> ".join(path))
else:
    print("No path found")
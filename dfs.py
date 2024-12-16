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


def DFS(graph,src,dst,path=None):
    
    if path is None:
        path = []
        
    path.append(src)
    
    if src == dst :
        return path
    
    for neighbour in graph.get(src, []):
        if neighbour not in path:
            
            result = DFS(graph,neighbour,dst,path)
            if result:
                return result
    path.pop()
    return None

path = DFS(city_map,'Delhi','Patna')

if path : 
    print("Path found : "," -> " .join(path))
else:
    print("No path found")
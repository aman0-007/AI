from q import Queue

class CityGraph :

    def __init__(self):
        #print("Get distance between cities...")
        self.graph = {}

    def addCity(self, city):
        if city not in self.graph:
            self.graph[city] = {}
            print(f"{city} added successfully.")
        else:
            print(f"{city} already exists.")

    def addDistance(self, city1, city2, distance):
        if city1 not in self.graph:
            self.graph[city1] = {}
        if city2 not in self.graph:
            self.graph[city2] = {}
            
        self.graph[city1][city2] = distance
        self.graph[city2][city1] = distance
        print(f"Distance between the {city1} and {city2} is {distance} kms.")

    def getCity(self):
        for city in self.graph:
            print(f"{city}")

    def getLinksWithDistance(self):
        for sourceCity,links in self.graph.items():
            for destinationCity, dist in links.items():
                print(f"Distance between {sourceCity} to {destinationCity} is {dist} kms.")

    def getLinks(self):
        for sourceCity,links in self.graph.items():
            print(links)

    def displayGraph(self):
        print("\n City Graph :\n")
        for city,links in self.graph.items():
            print(f"{city} : {links}")

    def isPathExits(self, source, destination):            
        if (source not in self.graph):
            print(f"No source city exits.")
            return
        if (destination not in self.graph):
            print(f"No destination city exit.")
            return
        
        for sourceCity, dest in self.graph.items():
            if sourceCity == source : 
                for destinationCity, distance in dest.items():
                    if destinationCity == destination:
                        print(f"Distance between {source} and {destinationCity} is {distance} kms")
                        return

    def BFS(self, src, dst):
        if src not in self.graph or dst not in self.graph:
            print("Invalid source or destination.")
            return

        visited = set([src])
        frontier = Queue()
        frontier.enqueue(src)
        parent = {src: None}

        while not frontier.isEmpty():
            current_city = frontier.dequeue()
            
            if current_city == dst:
                path = []
                while current_city:
                    path.append(current_city)
                    current_city = parent[current_city]
                print("Path found:", " -> ".join(path[::-1]))
                return

            for neighbor in self.graph[current_city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    frontier.enqueue(neighbor)
                    parent[neighbor] = current_city

        print(f"No path found between {src} and {dst}.")

cg = CityGraph()
while(True):
    print("==================== City Graph Options : ====================")
    print("1. Add Cities\n2. Add links and distance\n3. Display City Graph\n4. Get Cities\n5. Does Path Exists between ?\n6. Get Links\n7. Get Path")
    opt = int(input("Choose an option : "))
    
    if opt == 1 :
        op = "y"
        print("============= Add Cities =============")
        while op == "y":
            cg.addCity(input("Enter city name :"))
            op = input("Add more y/n ?")
    if opt == 2 :
        print("============= Add links and distance =============")
        op = "y"
        while op == "y" :
            cg.addDistance(input("Enter Source :"), input("Enter Destination :"), input("Enter Distance :"))
            op = input("Add more y/n ?")
    if opt == 3 :
        print("============= City Graph =============\n")
        cg.displayGraph()
    if opt == 4 :
        print("============= All City =============\n")
        cg.getCity()
    if opt == 5:
        print("============= All City =============\n")
        cg.isPathExits(input("Enter source city name"), input("Enter destination city name"))
    if opt == 6:
        print("============= All City Links =============\n")
        cg.getLinksWithDistance()
    if opt == 7:
        print("============= Get Path =============")
        cg.BFS(input("Enter source city : "), input("Enter destination city : "))
    if opt not in [1, 2, 3, 4, 5, 6, 7]:
        print("Please select appropriate options")










#cg = CityGraph()
# cg.addCity("Mumbai")
# cg.addCity("Satara")
# cg.addCity("Pune")
# cg.addCity("Nagpur")
# cg.addCity("Bhusaval")


# cg.getCity()

# cg.addDistance("Mumbai", "Pune", 150)
# cg.addDistance("Mumbai", "Satara", 170)
# cg.addDistance("Mumbai", "Nagpur", 175)
# cg.addDistance("Pune", "Satara", 75)
# cg.addDistance("Pune", "Nagpur", 168)
# cg.addDistance("Bhusaval", "Satara", 50)
# cg.addDistance("Bhusaval", "Nagpur", 180)

# cg.BFS("Mumbai", "Pune")
#cg.displayGraph()

# cg.getLinksWithDistance()

# print("=====================")

# cg.getLinks()
# print("================================")
# cg.isPathExits("Mumbai", "Pune")
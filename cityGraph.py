from q import Queue

class CityGraph :

    def __init__(self):
        print("Get distance between cities...")
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

cg = CityGraph()
cg.addCity("Mumbai")
cg.addCity("Satara")
cg.addCity("Pune")
cg.addCity("Nagpur")
cg.addCity("Bhusaval")


cg.getCity()

cg.addDistance("Mumbai", "Pune", 150)
cg.addDistance("Mumbai", "Satara", 170)
cg.addDistance("Mumbai", "Nagpur", 175)
cg.addDistance("Pune", "Satara", 75)
cg.addDistance("Pune", "Nagpur", 168)
cg.addDistance("Bhusaval", "Satara", 50)
cg.addDistance("Bhusaval", "Nagpur", 180)

cg.displayGraph()

cg.getLinksWithDistance()

print("=====================")

cg.getLinks()
print("================================")
cg.isPathExits("Mumbai", "Pune")

while(True):
    cg = CityGraph()
    print("==================== City Graph Options : ====================")
    print("1. Add Cities\n2. Add links and distance\n3. Display City Graph\n4. Get Cities\n5. Does Path Exists between ?")
    opt = int(input("Choose an option : "))
    
    if opt == 1 :
        op = "y"
        while op == "y":
            print("============= Add Cities =============")
            cg.addCity(input("Enter city name :"))
            op = input("Add more y/n ?")
    if opt == 2 :
        print("============= Add links and distance =============")
        op = "y"
        while op == "y" :
            
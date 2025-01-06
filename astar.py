from myutils import *

infinity = float('inf')


class MyGraph:
    def __init__(self, cmap, lcs, i, g):
        self.citymap = cmap
        self.init = i
        self.goal = g
        self.locs = lcs
        
    def goal_test(self,anode):
        return anode == self.goal
    
        # if anode==self.goal:
        #     return True
        # else:
        #     return False
    
    def getLinks(self, anode):
        return list(self.citymap[anode].keys())

    def h(self, node):        
        if self.locs:
            return int(distance(self.locs[node], self.locs[self.goal]))             
        else:
            return infinity

    def getMin(self,alist):       
        return min(alist.keys())
    
def astar_search(problem): # based on fig 3.24
    node = problem.init
    if problem.goal_test(node):
        return node
    gval = 0 # start to node n
    hval = problem.h(node) # estimated cheapest from n to goal
    #each entry in list represents a dictionary item with key as f-val and value as node with path   
    nodes = {gval+hval:[node]}
    while nodes:
        print("\nNodelist :\n", nodes)        
        minfval= problem.getMin(nodes)
        elist = nodes[minfval]
        minnode = nodes[minfval][-1]#extract last node from path         
        #print("-- minimum distance - ", minfval, ", min node ", minnode)
        if(problem.goal_test(minnode)):            
            return nodes[minfval] , minfval
        nodes.pop(minfval)        
        for child in problem.getLinks(minnode):
            # gvalue of child equals cost of minnode to child + f cost of minnode - h cost of minnode
            gval =  problem.citymap[minnode][child] + minfval - problem.h(minnode)
            hval = problem.h(child)            
            newlist = elist.copy()            
            newlist.append(child)            
            nodes[gval+hval]=  newlist
        input("press any key to continue...")
    return "not found"

romania_map = {'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},     
    'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu': 97, 'Bucharest': 101, 'Craiova': 138},
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Urziceni': {'Vaslui': 142, 'Bucharest': 85, 'Hirsova': 98},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Giurgiu': {'Bucharest': 90}, 'Mehadia': {'Drobeta': 75, 'Lugoj': 70},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},    'Neamt': {'Iasi': 87}}

locations = dict( Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))

'''
print("\nSolving for arad to bucharest...")
romania = MyGraph(romania_map, locations, 'Arad','Bucharest' )
print(romania.goal_test('Bucharest'))
print(romania.getLinks("Arad"))
x  = romania.citymap['Arad']['Zerind']
y = romania.h("Zerind")
print("g cost of going from arad to zerind is ", x)
print("estimated h cost of going from zerind to bucharest is ", y)
print("f cost of going from arad to bucharest via zerind is ", (x+y))'''



print("\nSolving for arad to bucharest...")
romania = MyGraph(romania_map, locations, 'Arad','Bucharest' )
result = astar_search(romania)
print("\n == Path",result[0], ", cost = ", result[1])


print("\nSolving for Drobeta to Vaslui...")
romania = MyGraph(romania_map, locations, 'Drobeta','Vaslui' )
result = astar_search(romania)
print("\n == Pat",result[0], ", cost = ", result[1])

def compute(rods=0):
        if rods==0 or not rods:
            return 0
        
        graph = {}
        
        for x,y in enumerate(rods):
                if y[0] not in graph:
                        graph[y[0]]= [y[1],]
                else:
                  if y[1] not in graph[y[0]]:
                    graph[y[0]].append(y[1])         
                  
                if y[1] not in graph:
                        graph[y[1]] = [y[0],]
                        
                else:
                    if y[0] not in graph[y[1]]:
                      graph[y[1]].append(y[0])    

        num_vertex = len(graph)
        nodes = list(graph.keys())

        
        visited_idx = [0 for i in range(num_vertex)] 
        visited = []
        grouping = [-1 for i in range(num_vertex)]
        #Initialize a queue
        queue = []

        cc = 0
        for idx in range(num_vertex):
                if not visited_idx[idx]:
                        cc +=1
                        bfs(graph, nodes[idx], cc,visited, nodes, visited_idx, grouping)

        unique = set()
        total = 0
        for e in grouping:
                if e not in unique:
                        unique.add(e)
                        total += grouping.count(e)-1

        return len(rods)-total

def bfs(graph, node, cc,visited,nodes,visited_idx,grouping):
  print("new bfs")
  print(grouping)
  queue = []
  visited.append(node)
  node_idx = nodes.index(node)
  visited_idx[node_idx] = 1
  grouping[node_idx] = cc
  queue.append(node)

  while queue:
    s = queue.pop(0)
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)

        nbr_idx = nodes.index(neighbour)
        visited_idx[nbr_idx]=1
        grouping[nbr_idx] = cc
        queue.append(neighbour)
        
###############################################################################
test_rod0 = []

# One repeated Rod, 2 unique vertex
test_rods = [(42,35) , (20,35), (20,35), (42,10)]
# 2 repeated Rod, 3 unique Vertex
test_rods2 =[(42,35),(42,35),(20,35),(20,35)]

# 3 Unique Rods (n unique rods), n unique vertex
test_rods3 = [(1,2),(1,3),(3,2)]

# disconnected graph, repeated edge

test_rods4 = [(42,35),(42,35), (35,10), (15,25), (15,25)]

#disconnected graph, duplicate edges only
test_rod5 = [(42,35),(42,35), (35,10), (15,25), (15,25)]

#remove nothing
test_rod6 = [(42,20),(20,15)]

# 3 graphs
test_rod7 = [(42,15),(20,35),(5,10)]

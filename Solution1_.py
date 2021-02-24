###############################
#########  Test rods  #########
###############################  

# One repeated Rod, 2 unique vertex
test_rods = [(42,35) , (20,35), (20,35), (42,10)]
# 2 repeated Rod, 3 unique Vertex
test_rods2 =[(42,35),(42,35),(20,35),(20,35)]

# 3 Unique Rods (n unique rods), n unique vertex
test_rods3 = [(1,2),(1,3),(3,2)]

def compute(rods=0):

    # corner case
    if not rods:
        return 0

    ###############################
    #####  generate matrix  ######
    ###############################  
    #### generate adjacency matrix
    idx=0
    dic = {}
    for x,y in enumerate(rods):
            if y[0] not in dic:
                    dic[y[0]]= idx
                    idx+=1
            if y[1] not in dic:
                    dic[y[1]] = idx
                    idx+=1

    num_vertex = len(dic)
    
    graph =  [[0 for column in range(num_vertex)]  for row in range(num_vertex)]
    
    for edge in rods:
        row = dic[edge[0]]
        col = dic[edge[1]]
        graph[row][col] = 1
        graph[col][row] = 1

    for i in range(num_vertex):
        print(graph[i])

     
    print("Max number of removed edges")
    return len(rods)-MST(num_vertex, graph)
    


###############################
#########  MST algo  ##########
###############################  
def MST(num_vertex,G):
    INF = 999999999999
    # create a array to track selected num_vertex
    # selected will become true otherwise false
    selected = [0 for i in range(num_vertex)]
    # set number of edge to 0
    num_edge = 0
    # the number of egde in minimum spanning tree will be
    # always less than(num_vertex - 1)
    # choose 0th (1st) num_vertex and make it true
    selected[0] = True

    num_edge_incl = 0 

    while (num_edge < num_vertex - 1):
        # For enum_vertexery num_vertex in the set S, find the all adjacent num_vertexertices
        #, calculate the distance from the num_vertex selected at step 1.
        # if the num_vertex is already in the set S, discard it otherwise
        # choose another num_vertex nearest to selected num_vertex at step 1.
        minimum = INF
        x = 0
        y = 0
        for i in range(num_vertex):
            if selected[i]:
                for j in range(num_vertex):
                    if ((not selected[j]) and G[i][j]):  
                        # not in selected and there is an edge
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
                            num_edge_incl +=1
                           
        selected[y] = True
        num_edge += 1

    
    #print("num_edge_incl: ", num_edge_incl)
    return num_edge_incl

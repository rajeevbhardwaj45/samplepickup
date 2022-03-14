from itertools import permutations

def readFile():
    #portion to read input file and assign content to allLines
    allLines = []
    try:
        inputFile = open('inputPS12.txt', 'r')
        allLines = inputFile.readlines()
        inputFile.close()
    except FileNotFoundError:
        print('Could not open the file')
    #read list of nodes into a list of lists containing start node, end node and distance
    edges = []
    for lines in allLines:
        if lines.startswith('Lab Node:'):
            labNode1 = lines.split(':')
            labNode = labNode1[1].strip()
        elif lines != '\n':
            newLine = lines.rstrip('\n')
            edges.append(newLine.split('/'))
    return(edges, labNode)


'''
Function listVertex takes edges and labNodes as input.
It returns a list consisting of all vertex (houses) from all edges except the labNode node
'''


def listVertex(edges, labNode):
    N = len(edges)
    vertex = []
    for i in range(N):
        if edges[i][0] not in vertex and edges[i][0] != labNode:
            vertex.append(edges[i][0])
        elif edges[i][1] not in vertex and edges[i][1] != labNode:
            vertex.append(edges[i][1])
    return(vertex)


'''
Function costofRoute takes two vertex (houses) as input (x, y) and also list edges
It returns the cost of travelling from x to y
All edges are bidirectional so cost of x to y is same as y to x
'''


def costofRoute(x, y, edges):
    cost = 0
    N = len(edges)
    for i in range(N):
        if (edges[i][0] == x and edges[i][1] == y) or (edges[i][0] == y and edges[i][1] == x):
            cost = edges[i][2]
    return(cost)


'''
Function optimalRoute takes list of vertex, edges and labNode
It returns the route with least cost and also the corresponding cost

'''


def optimalRoute(edges, vertex, labNode):
    # minCostRoute is a variable with a randomly slected very large number to initialize
    # minimum cost for travel
    minCostRoute = 1000000000
    minRoute = []
    # create permutations of all vertex in list vertex to get all possible sequence
    # Note that start and end node for all cases have to be set to labNode
    permRoute = permutations(vertex)
    # loop i calculates cost of each possible permutation after adding labNode
    # as start and end node
    for i in permRoute:
        # print(i)
        route = []
        costRoute = 0
        startNode = labNode
        num = len(i)
        # Loop j runs through each step in a permutaion to get sum of cost for
        # each step
        for j in range(num):
            route.append((startNode, i[j]))
            fromNode = route[j][0]
            toNode = route[j][1]
            costRoute += float(costofRoute(fromNode, toNode, edges))
            startNode = i[j]
        route.append((i[j], labNode))
        fromNode = route[j+1][0]
        toNode = route[j+1][1]
        costRoute += float(costofRoute(fromNode, toNode, edges))
        # print("\ni: ", i)
        # print("route: ", route)
        # print("Cost: ", costRoute)
        # for each permutation of vertex check if the cost of travel is least so far
        if costRoute < minCostRoute:
            minCostRoute = costRoute
            minRoute = route
    return(minRoute, minCostRoute)


'''
This part calls different functions in following order
1. Read file and gets values of edges and labNode
2. Get vertex as list of all nodes (houses). vertex does not contain labNode
3. Call to optimalRoute function to get route with minimum cost and the corresponding costRoute
4. Display results
'''


def generate_report():
    output_path = 'outputsPS12.txt'
    edges, labNode = readFile()
    vertex = listVertex(edges, labNode)
    minRoute, minCostRoute = optimalRoute(edges, vertex, labNode)
    l = len(minRoute)
    routePrint = ''
    for i in range(l):
        routePrint = routePrint + minRoute[i][0] + "->"
    routePrint = routePrint + minRoute[i][1]
    output_file = open(output_path, "w")
    output_file.write("The optimal Route is\n %s" % routePrint)
    output_file.write("\nThe total distance is\n %f" % minCostRoute)


if __name__ == '__main__':
    generate_report()

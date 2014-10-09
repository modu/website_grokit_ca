
import ds.graph as graph

import heapq

def isPathVictory(path, vEnd):
    if path[0][-1] == vEnd:
        return True
    return False

def visitVertex(paths, path, edge, visited):

    path, cost = path
    cost += edge.weight
    path.append(edge.to)

    visited.add(edge.frm)

    paths.append( (path, cost) )

def popLeastCostPathAndEdge(paths, visited):

    fPath, minCost = paths[0]
    minE = next(iter(fPath[-1].edges))
    minCost += minE.weight
    remPath = paths[0] 

    for path, cost in paths:
        path = path[-1]
        for edge in path.edges:
            if edge.to not in visited:
                if cost + edge.weight < minCost:
                    minE = edge
                    minCost = cost + edge.weight 
                    remPath = (path, cost)

    paths.remove(remPath)
    
    return (remPath, minE)

def findShortestPath(G, vStart, vEnd):
    paths = [([vStart], 0)]
    visited = set()

    while len(paths) > 0:

        import pdb; pdb.set_trace()
        for path in paths:
            for v in path[0]:
                print(v)
            print('--x--')
            

        path, edge = popLeastCostPathAndEdge(paths, visited)
        visitVertex(paths, path, edge, visited)

        if isPathVictory(path, vEnd):
            return path[0]

    raise Exception("Shortest path error")

with open('undirected_weighted_graph_simple.dot', 'r') as f:
    dotStr = f.read()

G = graph.graphFromDotString(dotStr)

vStart = G.vertices['a']
vEnd = G.vertices['d']
shortestPath = findShortestPath(G, vStart, vEnd)
print(shortestPath)


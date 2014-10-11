"""
Shortest-path algorithm loosely following Dijkstra's shortest path.

Notes:
    - This is a rag-tag solution that does not use a heap to bring the complexity down (n^2 instead of the possible n log(n)).
    
    - Instead of keeping data by annotating nodes, it keeps a stack of all the possible next steps. This makes this implementation overly complicated.
"""

import ds.graph as graph

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
    minCost = None

    for path, cost in paths:
        pathSoFar = path
        path = path[-1]
        for edge in path.edges:
            if edge.to not in visited:
                if minCost is None or cost + edge.weight < minCost:
                    minE = edge
                    minCost = cost + edge.weight 
                    remPath = (pathSoFar, cost)

    paths.remove(remPath)
    
    return (remPath, minE)

def findShortestPath(G, vStart, vEnd):
    paths = []
    visited = set()

    for edge in vStart.edges:
        paths.append( ([vStart, edge.to], edge.weight) )
        visited.add(vStart)

    while len(paths) > 0:
        path, edge = popLeastCostPathAndEdge(paths, visited)
        visitVertex(paths, path, edge, visited)

        if isPathVictory(path, vEnd):
            return path[0]

    raise Exception("Shortest path error")

def test(filename):
    print('Testing with file: %s.' % filename)

    with open(filename, 'r') as f:
        dotStr = f.read()

    G = graph.graphFromDotString(dotStr)

    vStart = G.vertices['a']
    vEnd = G.vertices['d']
    shortestPath = findShortestPath(G, vStart, vEnd)

    for v in shortestPath:
        print(v)

if __name__ == '__main__':
    test('undirected_weighted_graph_simple.dot')
    test('undirected_weighted_graph_simple2.dot')
    test('undirected_weighted_graph_simple3.dot')

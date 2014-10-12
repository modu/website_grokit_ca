
import ds.graph as graph

import collections


def visit(vertex, edgeT, visited):

    visited.add( vertex )

    for edge in vertex.edges:
        if edge.to not in visited:
            edgeT.append( edge )

def findPopLeastCost(edgeT, visited):

    cand = []

    for edge in edgeT:
        if not edge.to in visited:
            cand.append( (edge, edge.frm.backtrackCost + edge.weight) )

    cand.sort( key = lambda x: x[1] )

    edge = cand[0][0]
    edgeT.remove( edge )

    return edge 


def findShortestPath(vStart, vEnd):

    visited = set()
    edgeT = []

    vStart.backtrackCost = 0
    vStart.backtrackVertex = None
    visit(vStart, edgeT, visited)

    while len(edgeT) > 0:

        edge = findPopLeastCost(edgeT, visited)

        edge.to.backtrackCost = edge.frm.backtrackCost + edge.weight
        edge.to.backtrackVertex = edge.frm 

        visit(edge.to, edgeT, visited)

        if edge.to == vEnd:
            path = collections.deque()
            edge = edge.to
            while edge is not None:
                path.appendleft( edge )
                edge = edge.backtrackVertex
            return path

    raise Exception("Shortest path error")

def test(filename):
    print('Testing with file: %s.' % filename)

    with open(filename, 'r') as f:
        dotStr = f.read()

    G = graph.graphFromDotString(dotStr)

    vStart = G.vertices['a']
    vEnd = G.vertices['d']
    shortestPath = findShortestPath(vStart, vEnd)

    for v in shortestPath:
        print(v)

if __name__ == '__main__':
    test('undirected_weighted_graph_simple.dot')
    test('undirected_weighted_graph_simple2.dot')
    test('undirected_weighted_graph_simple3.dot')


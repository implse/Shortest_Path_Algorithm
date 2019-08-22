from heapq import heappop, heappush
from math import inf

def dijkstras(graph, start):
    # Map vertices to their distance
    distances = {}
    for vertex in graph:
        distances[vertex] = inf
    distances[start] = 0
    # Min Heap
    vertices_to_explore = [(0, start)]
    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)

    for neighbor, edge_weight in graph[current_vertex]:
        new_distance = current_distance + edge_weight
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            heappush(vertices_to_explore, (new_distance, neighbor))
    return distances

distances_from_d = dijkstras(graph, 'D')
print("\n\nShortest Distances: {0}".format(distances_from_d))

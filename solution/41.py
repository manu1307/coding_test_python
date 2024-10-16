def solution(graph, source):
    # 그래프의 노드 수
    num_vertices = len(graph)

    # 거리 배열
    distance = [float("inf")] * num_vertices
    distance[source] = 0

    predecessor = [None] * num_vertices

    # 간선 수 만큼 반복하여 최단 경로 갱신
    for tmp in range(num_vertices - 1):
        for u in range(num_vertices):
            for v, w in graph[u]:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u

    for u in range(num_vertices):
        for v, w in graph[u]:
            if distance[u] + w < distance[v]:
                return [-1]
    return [distance, predecessor]


print(solution([[(1, 4), (2, 3), (4, -6)], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)], [(2, 2)]],
               0))  # 반환갑 : [[0, -2, -4, 3, -6], [None, 2, 4, 1, 0]]
print(solution([[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]], 0))  # 반환값 : [-1]

import heapq


def solution(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    q = []
    heapq.heappush(q, [dist[start], start])
    paths = {start: [start]}

    while q:
        # 현재 가장 거리 값이 가장 작은 노드를 가져옴
        curr_dist, curr_node = heapq.heappop(q)

        # 만약 현재 노드의 거리 값이 큐에서 가져온 거리값보다 크면, 해당 노드는 이미 처리된 것이므로 무시
        if dist[curr_node] < curr_dist:
            continue

        for adjacent_node, w in graph[curr_node].items():
            temp_dist = curr_dist + w
            if temp_dist < dist[adjacent_node]:
                dist[adjacent_node] = temp_dist
                paths[adjacent_node] = paths[curr_node] + [adjacent_node]
                heapq.heappush(q, [temp_dist, adjacent_node])

    sorted_paths = {node: paths[node] for node in sorted(paths)}

    return [dist, sorted_paths]


print(solution({'A': {'B': 9, 'C': 3}, 'B': {'A': 5}, 'C': {'B': 1}},
               'A'))  # 반환값 :[{'A': 0, 'B': 4, 'C': 3}, {'A': ['A'], 'B': ['A', 'C', 'B'], 'C': ['A', 'C']}]
print(solution({'A': {'B': 1}, 'B': {'C': 5}, 'C': {'D': 1}, 'D': {}},
               'A'))  # 반환값 :[{'A': 0, 'B': 1, 'C': 6, 'D': 7}, {'A': ['A'], 'B': ['A', 'B'], 'C': ['A', 'B', 'C'], 'D': ['A', 'B', 'C', 'D']}]

import heapq


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    distance = [float("inf")] * (N + 1)
    distance[1] = 0

    # 그래프 구성
    for a, b, cost in road:
        graph[a].append([b, cost])
        graph[b].append([a, cost])

    heap = []
    heapq.heappush(heap, [0, 1])
    while heap:
        dist, node = heapq.heappop(heap)
        for n_node, n_cost in graph[node]:
            cost = dist + n_cost
            if cost < distance[n_node]:
                distance[n_node] = cost
                heapq.heappush(heap, [cost, n_node])

    answer = 0
    for i in range(N + 1):
        if distance[i] <= K:
            answer += 1

    return answer


# def find_min(N, visited, distance):
#     min_val = float("inf")
#     idx = 0
#     for i in range(N):
#         if distance[i] < min_val and visited[i] == 0:
#             min_val = distance[i]
#             idx = i
#     return idx
#
#
# def solution(N, road, K):
#     # 각 노드의 연결정보를 담은 딕셔너리 생성 노드 : [연결노드, 시간]
#     # 다익스트라로 최소 연결 그래프 만든다
#     # [이전 노드, 거리] 담을 배열
#     road_dict = {}
#     for r in road:
#         if r[0] in road_dict:
#             road_dict[r[0]].append([r[1], r[2]])
#         else:
#             road_dict[r[0]] = [[r[1], r[2]]]
#         if r[1] in road_dict:
#             road_dict[r[1]].append([r[0], r[2]])
#         else:
#             road_dict[r[1]] = [[r[0], r[2]]]
#     visited = [0] * (N + 1)
#     distance = [float('inf') for _ in range(N + 1)]
#     prev = [None] * (N + 1)
#     distance[1] = 0
#     prev[1] = 1
#     for _ in range(N - 1):
#         curr = find_min(N, visited, distance)
#         visited[curr] = 1
#         for j in road_dict[curr]:
#             if distance[curr] + j[1] < distance[j[0]]:
#                 distance[j[0]] = distance[curr] + j[1]
#                 prev[j[0]] = curr
#     answer = 0
#     for i in range(N + 1):
#         if distance[i] <= K:
#             answer += 1
#
#     return answer


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))

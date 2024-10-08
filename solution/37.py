def solution(n, costs):
    # 각 노드별로 [연결 노드, cost]를 값으로 하는 그래프 생성
    # 방문했는지 여부 판단하는 리스트
    # 시작 노드는 0
    # 방문한 노드들의 인접 노드 중
    # 방문하지 않은 노드 중 최단 거리인 노드를 방문
    # 총 거리 계산
    graph = {}
    for cost in costs:
        s, e, c = cost
        if s not in graph:
            graph[s] = [[e, c]]
        else:
            graph[s].append([e, c])

        if e not in graph:
            graph[e] = [[s, c]]
        else:
            graph[e].append([s, c])

    distance = 0
    visited = [False for _ in range(n)]
    visited_nodes = [0]
    visited[0] = True
    while len(visited_nodes) < n:
        min_node = [-1, 9999999]
        for node in visited_nodes:
            for adjacent in graph[node]:
                if not visited[adjacent[0]] and adjacent[1] < min_node[1]:
                    min_node = adjacent
        visited[min_node[0]] = True
        visited_nodes.append(min_node[0])
        distance += min_node[1]

    return distance


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))

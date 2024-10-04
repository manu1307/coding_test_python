from collections import deque


def solution(info, edges):
    # 인접 노드들의 정보를 담은 그래프 리스트 선언
    # bfs로 탐색
    # 현재 위치, 양, 늑대, 인접 노드 집합
    tree = [[] for _ in range(len(info))]
    for edge in edges:
        s, e = edge
        tree[s].append(e)

    q = deque([[0, 1, 0, set()]])
    max_sheep = 0

    while q:
        curr, sheep, wolf, visited = q.popleft()
        max_sheep = max(max_sheep, sheep)
        visited.update(tree[curr])
        for next_node in visited:
            if info[next_node] == 1:
                if sheep > wolf + 1:
                    q.append([next_node, sheep, wolf + 1, visited - {next_node}])
            else:
                q.append([next_node, sheep + 1, wolf, visited - {next_node}])
    return max_sheep


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))

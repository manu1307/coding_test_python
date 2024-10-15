from collections import deque


def solution(graph, start):
    graph_dict = {}
    for g in graph:
        if g[0] not in graph_dict:
            graph_dict[g[0]] = [g[1]]
        else:
            graph_dict[g[0]].append(g[1])

    q = deque()
    q.append(start)
    visited = []
    while q:
        curr = q.popleft()
        if curr in visited:
            continue
        visited.append(curr)
        if curr in graph_dict:
            for a in sorted(graph_dict[curr]):
                q.append(a)

    return visited


print(solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)],
               1))  # 반환값 :[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], 1))  # 반환값 : [1, 2, 3, 4, 5, 0]

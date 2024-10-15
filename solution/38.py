def solution(graph, start):
    # graph를 가지고 방문 노드의 딕셔너리 생성
    # 방문 여부 확인하는 배열 -> 정답 배열로 대체 가능할 듯
    # 스택에 넣어주고
    # 팝해서 이웃노드 넣어주고 (알파벳 역순으로)
    # 계속해서 방문
    graph_dict = {}
    for g in graph:
        if g[0] not in graph_dict:
            graph_dict[g[0]] = [g[1]]
        else:
            graph_dict[g[0]].append(g[1])

    stack = [start]
    visited = []
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.append(curr)

        if curr in graph_dict:
            adjacent = sorted(graph_dict[curr], reverse=True)
            for a in adjacent:
                stack.append(a)

    return visited


print(solution([["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"]], "A"))
print(solution([["A", "B"], ["A", "C"], ["B", "D"], ["B", "E"], ["C", "F"], ["E", "F"]], "A"))

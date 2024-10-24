from collections import defaultdict


def solution(n, wires):
    # 그래프 생성
    # wires 반복문 돌면서 해당하는 전선을 잘라준다 -> 그래프에 내용 반영
    # 1번 노드에 대해서 bfs
    # bfs해서 센 결과값 = count1
    # 나머지 = n - count1
    # 차이 구해서 계속 최솟값으로 업데이트

    answer = 100000

    graph = [[] for _ in range(n + 1)]

    for w in wires:
        s, e = w
        graph[s].append(e)
        graph[e].append(s)

    for w in wires:
        s, e = w
        n_graph = [x[:] for x in graph]
        n_graph[s].remove(e)
        n_graph[e].remove(s)

        v = [0 for _ in range(n + 1)]
        stack = [1]
        cnt = 0
        # 시작 노드 팝
        # 인접노드 미방문이면 스택에 푸시
        while stack:
            curr = stack.pop(0)
            v[curr] = 1
            cnt += 1
            for adj in n_graph[curr]:
                if v[adj] == 0:
                    stack.append(adj)
        cnt2 = n - cnt
        diff = abs(cnt - cnt2)
        answer = min(answer, diff)

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))

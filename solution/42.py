from collections import deque


def solution(maps):
    # BFS 문제
    # 큐 선언
    # 시작점 [0,0], 도착점  [4,4]
    # 큐에서 팝 한 후에
    n = len(maps)
    m = len(maps[0])

    q = deque()
    q.append([0, 0])

    while q:

        cr, cc = q.popleft()
        if (cr, cc) == (n, m):
            break
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = cr + dr, cc + dc
            # 네 방향, 범위내, 미방문
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1:
                maps[nr][nc] = maps[cr][cc] + 1
                q.append([nr, nc])

    return maps[n - 1][m - 1] if maps[n - 1][m - 1] != 1 else -1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution(([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]])))

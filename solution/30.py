from collections import deque


def solution(maps):
    # 출발점 -> 레버 최단 경로 구하고
    # 레버 -> 출구 최단 경로 구한다
    # bfs(출발 좌표, 목표 좌표)
    # 동서남북 방향의 좌표를 큐에 넣어주고
    # 방문했다면 리턴
    # 방문하지 않았다면 카운트 1 증가시키고

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(start, target):
        visit = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
        q = deque([start])
        while q:
            cx, cy = q.popleft()
            for k in range(4):
                nx = cx + dx[k]
                ny = cy + dy[k]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visit[nx][ny] == 0 and maps[nx][ny] != "X":
                    q.append([nx, ny])
                    visit[nx][ny] = visit[cx][cy] + 1
        return visit[target[0]][target[1]]

    s_coord = []
    l_coord = []
    e_coord = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                s_coord.append(i)
                s_coord.append(j)
            if maps[i][j] == "L":
                l_coord.append(i)
                l_coord.append(j)
            if maps[i][j] == "E":
                e_coord.append(i)
                e_coord.append(j)

    d1 = bfs(s_coord, l_coord)
    if d1 == 0:
        return -1
    d2 = bfs(l_coord, e_coord)
    if d2 == 0:
        return -1
    return d1 + d2


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))

# bfs 구현 순서 확실하게 암기할 것!

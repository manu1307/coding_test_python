# 문제 설명서, 보면서 디버깅

R, C, K = map(int, input().split())
unit = [list(map(int, input().split())) for _ in range(K)]
arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]
exit_set = set()
# 상 우 하 좌 (시계 방향)
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(si, sj):
    q = []
    v = [[0] * (C + 2) for _ in range(R + 4)]
    mx_i = 0  # -2 해서 리턴

    q.append((si, sj))
    v[si][sj] = 1
    while q:
        ci, cj = q.pop(0)
        mx_i = max(mx_i, ci)
        # 네 방향, 미방문, 조건 : 같은 값 또는 내가 출구 - 상대방이 골렘
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if v[ni][nj] == 0 and (arr[ci][cj] == arr[ni][nj] or ((ci, cj) in exit_set and arr[ni][nj] > 1)):
                q.append((ni, nj))
                v[ni][nj] = 1
    return mx_i - 2


ans = 0
num = 2
# 골렘 입력 좌표/방향에서 따라서 남쪽 이동 및 정령 최대 좌표 계산
for cj, dr in unit:
    ci = 1
    # 1. 남쪽으로 최대한 이동 ( 남 -> 서 -> 동)
    while True:
        # 남쪽(아래쪽)으로 한칸 이동
        if arr[ci + 1][cj - 1] + arr[ci + 2][cj] + arr[ci + 1][cj + 1] == 0:  # 비어있다
            ci += 1
        # 서족으로 회전하면서 아래로 한칸
        elif arr[ci - 1][cj - 1] + arr[ci][cj - 2] + arr[ci + 1][cj - 1] + arr[ci + 1][cj - 2] + arr[ci + 2][
            cj - 1] == 0:
            ci += 1
            cj -= 1
            dr = (dr - 1) % 4
        # 동쪽(오른쪽) 으로 회전하면서 아래로 한칸
        elif arr[ci - 1][cj + 1] + arr[ci][cj + 2] + arr[ci + 1][cj + 1] + arr[ci + 1][cj + 2] + arr[ci + 2][
            cj + 1] == 0:
            ci += 1
            cj += 1
            dr = (dr + 1) % 4
        else:
            break
    # 2. 골렘을 표시
    if ci < 4:  # 몸이 범위 밖 (새롭게 탐색시작...arr 초기화)
        arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]
        exit_set = set()
        num = 2

    else:
        # 골렘을 표시 + 비상구 위치 추가
        arr[ci + 1][cj] = arr[ci - 1][cj] = arr[ci][cj - 1] = arr[ci][cj] = arr[ci][cj + 1] = num
        num += 1

        exit_set.add((ci + di[dr], cj + dj[dr]))

        ans += bfs(ci, cj)

print(ans)

# from collections import deque
#
# R, C, K = map(int, input().split())
# a_lst = [list(map(int, input().split())) for _ in range(K)]
#
# # 숲을 만들어준다 - 위에 가상의 세 개의 행을 더 추가할 것인가?
# forest = [[0] * C for _ in range(R + 3)]
# ans = 0
#
#
# def move_west(g_lst, forest, d):
#     n_forest = [x[:] for x in forest]
#     ng_lst = [x[:] for x in g_lst]
#     print(g_lst)
#     sr = g_lst[0][0]
#     sc = g_lst[4][1]
#     # 반시계 방향 회전
#     n_forest[g_lst[d][0]][g_lst[d][1]], n_forest[g_lst[(d - 1) % 4][0]][g_lst[(d - 1) % 4][1]] = \
#         n_forest[g_lst[(d - 1) % 4][0]][g_lst[(d - 1) % 4][1]], n_forest[g_lst[d][0]][g_lst[d][1]]
#     # 서쪽으로 한 칸, 남쪽으로 한 칸 이동
#     for i in range(5):
#         if i == 0 or i == 1 or i == 4:
#             n_forest[g_lst[i][0]][g_lst[i][1]] = 0
#         n_forest[ng_lst[i][0] + 1][ng_lst[i][1] - 1] = forest[g_lst[i][0]][g_lst[i][1]]
#     return n_forest, ng_lst
#
#
# def move_east(g_lst, forest, d):
#     n_forest = [x[:] for x in forest]
#     ng_lst = [x[:] for x in g_lst]
#     # 시계 방향 회전
#     n_forest[g_lst[d][0]][g_lst[d][1]], n_forest[g_lst[(d - 1) % 4][0]][g_lst[(d + 1) % 4][1]] = \
#         n_forest[g_lst[(d + 1) % 4][0]][g_lst[(d + 1) % 4][1]], n_forest[g_lst[d][0]][g_lst[d][1]]
#     nn_forest = [x[:] for x in n_forest]
#     print("IN EAST", n_forest, g_lst, ng_lst)
#     # 동쪽으로 한 칸, 남쪽으로 한 칸 이동
#     for i in range(5):
#         print("BEFORE", nn_forest)
#         print(g_lst[i][0], g_lst[i][1], ng_lst[i][0] + 1, ng_lst[i][1] + 1, n_forest[g_lst[i][0]][g_lst[i][1]])
#         if i == 0 or i == 3 or i == 4:
#             nn_forest[g_lst[i][0]][g_lst[i][1]] = 0
#         print("AFTER", nn_forest, n_forest[g_lst[i][0]][g_lst[i][1]])
#         nn_forest[ng_lst[i][0] + 1][ng_lst[i][1] + 1] = n_forest[g_lst[i][0]][g_lst[i][1]]
#         print("AFTER", nn_forest)
#     print("IN EAST", nn_forest)
#     return nn_forest, ng_lst
#
#
# def bfs(forest, sr, sc):
#     # 네방향, 범위 내
#     q = deque([[sr, sc]])
#     v = [[0] * C for _ in range(R + 3)]
#     mx = 0
#     while q:
#         cr, cc = q.popleft()
#         v[cr][cc] = 1
#         if forest[cr][cc] == 0:
#             continue
#         for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#             nr, nc = cr + dr, cc + dc
#             if forest[cr][cc] < 0:
#                 if 0 <= nr < R + 3 and 0 <= nc < C and v[nr][nc] == 0 and forest[nr][nc] != 0:
#                     q.append([nr, nc])
#                     mx = max(mx, nr)
#             elif forest[cr][cc] > 0:
#                 if 0 <= nr < R + 3 and 0 <= nc < C and v[nr][nc] == 0 and forest[nr][nc] != 0 and forest[cr][cc] == \
#                         forest[nr][nc]:
#                     q.append([nr, nc])
#                     mx = max(mx, nr)
#     return mx
#
#
# for i in range(1, len(a_lst) + 1):
#     # 골렘 생성
#     c, d = a_lst[i - 1]
#     g_lst = [[0, c - 1], [1, c], [2, c - 1], [1, c - 2], [1, c - 1]]
#     # 골렘 넣기
#     n_forest = [x[:] for x in forest]
#     for j in range(5):
#         if j == d:
#             n_forest[g_lst[j][0]][g_lst[j][1]] = -i
#
#         else:
#             n_forest[g_lst[j][0]][g_lst[j][1]] = i
#     forest = n_forest
#
#     while True:
#         print([c, d], forest)
#         # 남쪽 1칸 이동 가능한지 확인 후 이동
#         if g_lst[2][0] + 1 < R + 3 and forest[g_lst[2][0] + 1][g_lst[2][1]] == 0:
#             n_forest = [x[:] for x in forest]
#             ng_lst = [x[:] for x in g_lst]
#             for j in range(5):
#                 if j == 0 or j == 1 or j == 3:
#                     n_forest[g_lst[j][0]][g_lst[j][1]] = 0
#                 n_forest[g_lst[j][0] + 1][g_lst[j][1]] = forest[g_lst[j][0]][g_lst[j][1]]
#
#                 ng_lst[j][0] += 1
#             g_lst = ng_lst
#             forest = n_forest
#             continue
#         # 서쪽 회전 가능한지 확인 후 이동
#         if g_lst[2][0] + 1 < R + 3 and (g_lst[3][1] - 1 >= 0 and forest[g_lst[0][0]][g_lst[0][1] - 1] == 0 and
#                                         forest[g_lst[2][0]][g_lst[2][1] - 1] == 0 and forest[g_lst[2][0] + 1][
#                                             g_lst[2][1] - 1] == 0):
#             n_forest, ng_lst = move_west(g_lst, forest, d)
#             g_lst = ng_lst
#             forest = n_forest
#             continue
#         print(g_lst, "IN EAST")
#         # 동쪽 회전 가능한지 확인 후 이동
#         if g_lst[2][0] + 1 < R + 3 and (g_lst[1][1] + 1 < C and forest[g_lst[0][0]][g_lst[0][1] + 1] == 0 and
#                                         forest[g_lst[2][0]][g_lst[2][1] + 1] == 0 and forest[g_lst[2][0] + 1][
#                                             g_lst[2][1] + 1] == 0):
#             n_forest, ng_lst = move_east(g_lst, forest, d)
#             g_lst = ng_lst
#             forest = n_forest
#             continue
#         else:
#             break
#
#     # 골렘 숲에서 넘치는지 확인
#     clear = 0
#     for r in range(3):
#         for c in range(C):
#             if forest[r][c] != 0:
#                 clear = 1
#                 break
#
#     # 넘치면 숲 초기화
#     if clear == 1:
#         forest = [[0] * C for _ in range(R + 3)]
#         continue
#
#     # 정령 남쪽으로 이동
#     r = 0
#     c = 0
#     for g in g_lst:
#         r += g[0]
#         c += g[1]
#     mst_south = bfs(forest, int(r // 5), int(c // 5))
#     print(mst_south - 2)
#     ans += mst_south - 2
#
# print(ans)
#
# # 정령의 열 번호에 따라 골렘을 만들어준다
# # 1) 남쪽으로 1칸 이동가능한지 확인
# #    가능하면 남쪽으로 한 칸 1칸 이동
# # 2) 1이 불가능하면 서쪽으로 1칸씩이랑 서쪽 아래 1칸이 비어있는지 확인
# #    가능하면 서쪽으로 한 칸 이동 + 반시계 방향 회전, 남쪽으로 한 칸 이동
# # 3) 2가 불가능하면 동쪽으로 1칸씩이랑 동쪽 아래 1칸이 비어있는지 확인
# #    가능하면 동쪽으로 한 칸 이동 + 시계 방향 회전, 남쪽으로 한 칸 이동
# # 3도 안되면 스톱
# # 숲에 3행 위에 골렘이 있으면 숲을 초기화 시킨다.
# # 아니면, 현재 정령의 위치에서 최대한 남쪽으로 내려간다 (출구가 내 출구인지 판단 해봐야됨)
# # ans에 정령의 (행 - 2) 값을 더해준다.

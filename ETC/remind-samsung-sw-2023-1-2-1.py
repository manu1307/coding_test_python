N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    cr, cc = map(int, input().split())
    board[cr - 1][cc - 1] -= 1
er, ec = map(lambda x: int(x) - 1, input().split())
board[er][ec] = -11

ans = 0
cnt = M


def find_square(board):
    # 최소 정사각형 길이 구하기
    L = N
    for i in range(N):
        for j in range(N):
            # 사람 찾아서
            if -11 < board[i][j] < 0:
                L = min(L, max(abs(i - er), abs(j - ec)))

    # 모든 가능한 시작 좌표에 대해
    for si in range(N - L):
        for sj in range(N - L):
            if si <= er <= si + L and sj <= ec <= sj + L:
                for i in range(si, si + L + 1):
                    for j in range(sj, sj + L + 1):
                        if -11 < board[i][j] < 0:
                            return si, sj, L + 1


def find_exit(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == -11:
                return i, j


for k in range(K):
    n_board = [x[:] for x in board]
    for i in range(N):
        for j in range(N):
            # 사람일 떄
            if -11 < board[i][j] < 0:
                d = abs(i - er) + abs(j - ec)
                # 네 방향 상하좌우,  조건
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = i + dr, j + dc
                    # 만약 거리가 더 짧다면 이동\
                    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] <= 0 and abs(nr - er) + abs(nc - ec) < d:

                        ans += board[i][j]
                        # 이전 위치 0으로 만들어주고
                        n_board[i][j] -= board[i][j]
                        # 이동할 위치가 출구가 아니라면
                        if board[nr][nc] == -11:
                            cnt += board[i][j]
                        # 해당 위치로 값 이동
                        else:
                            n_board[nr][nc] += board[i][j]
                        break
    # 만약 다 탈출했으면
    if cnt <= 0:
        break

    board = n_board

    si, sj, L = find_square(board)

    n_board = [x[:] for x in board]
    for i in range(L):
        for j in range(L):
            n_board[si + i][sj + j] = board[si + L - 1 - j][sj + i]
            if n_board[si + i][sj + j] > 0:
                n_board[si + i][sj + j] -= 1

    board = n_board
    er, ec = find_exit(board)

for i in range(N):
    for j in range(N):
        if board[i][j] == -11:
            er, ec = i, j

print(ans)
print(er + 1, ec + 1)

# 풀면서 실수했던 점
# 1. 출구 위치 계속 갱신되어야 함
# 2. 정사각형 찾을 때 좌표 값의 차이 != 정사각형의 길이, 정사각형의 길이가 1 커야됨
# 3. nr, nc의 오타 있었음
# 4. 2번 문제에서 파생되는 사각형 탐색 범위의 오류

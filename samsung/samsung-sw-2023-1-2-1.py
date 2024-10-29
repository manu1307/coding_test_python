N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    i, j = map(lambda x: int(x) - 1, input().split())
    arr[i][j] += -1
ei, ej = map(lambda x: int(x) - 1, input().split())
arr[ei][ej] = -11


def find_square(arr):
    # 비상구와 모든 사람간의 가장 짧은 가로 또는 세로 거리 구하기
    mn = N
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0:  # 사람인 경우
                mn = min(mn, max(abs(ei - i), abs(ej - j)))

    # 순회하면서 길이 L인 정사각형에 비상구와 사람 있는지 체크
    for si in range(N - mn):
        for sj in range(N - mn):  # 가능한 모든 시작 위치
            if si <= ei <= si + mn and sj <= ej <= sj + mn:  # 비상구가 포함된 사각형
                for i in range(si, si + mn + 1):
                    for j in range(sj, sj + mn + 1):
                        if -11 < arr[i][j] < 0:
                            return si, sj, mn + 1


def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                return i, j


ans = 0
cnt = M

for _ in range(K):
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0:  # 사람인 경우
                dist = abs(ei - i) + abs(ej - j)
                # 네 방향(상하우선), 범위내, 벽 아니고 <= 0, 거리가 dist 보다 작은면
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] <= 0 and dist > abs(ei - ni) + abs(ej - nj):
                        ans += arr[i][j]  # 현재 인원수가 이동하는 것이니 이동거리에 누적
                        narr[i][j] -= arr[i][j]  # 이동처리
                        if arr[ni][nj] == -11:  # 비상구인 경우
                            cnt += arr[i][j]  # 탈출
                        else:  # 일반빈칸 or 사람
                            narr[ni][nj] += arr[i][j]  # 들어온 인원 추가
                        break
    arr = narr

    if cnt == 0:
        break

    si, sj, L = find_square(arr)  # 비상구 + 사람 포함 최소 정사각형

    narr = [x[:] for x in arr]
    for i in range(L):
        for j in range(L):
            narr[si + i][sj + j] = arr[si + L - 1 - j][sj + i]
            if narr[si + i][sj + j] > 0:  # 벽이면 회전시 1 감소
                narr[si + i][sj + j] -= 1

    arr = narr
    # 회전으로 비상구 위치 저장
    ei, ej = find_exit(arr)

print(-ans)
print(ei + 1, ej + 1)


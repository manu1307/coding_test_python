def rotate(arr, si, sj):  # 90도 회전
    narr = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            narr[si + i][sj + j] = arr[si + 3 - j - 1][sj + i]
    return narr


def bfs(arr, v, si, sj, clr):
    q = []
    sset = set()
    cnt = 0

    q.append((si, sj))
    v[si][sj] = 1
    sset.add((si, sj))
    cnt += 1

    while q:
        ci, cj = q.pop(0)
        # 네 방향, 범위내, 미방문, 조건 : 같은 값이면
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and v[ni][nj] == 0 and arr[ci][cj] == arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = 1
                sset.add((ni, nj))
                cnt += 1
    if cnt >= 3:  # 유물이면: cnt 리턴 + clr == 1이면 0으로 clear
        if clr == 1:  # 0으로 초기화
            for i, j in sset:
                arr[i][j] = 0
        return cnt
    else:  # 3개 미만이면
        return 0


def count_clear(arr, clr):  # clr == 1인 경우 3개 이상값들을 0 으로 만듦
    v = [[0] * 5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5):  # 미방문인 경우 같은 값이면 fill
            if v[i][j] == 0:
                # 같은 값이면, 3개 이상인 경우
                t = bfs(arr, v, i, j, clr)
                cnt += t
    return cnt


K, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(5)]
lst = list(map(int, input().split()))
ans = []

for _ in range(K):  # K 턴을 진행(유물이 없는 경우 즉시 종료)
    # [1] 탐사진행
    mx_cnt = 0
    for rot in range(1, 4):  # 회전수 -> 열 -> 행 (작은순)
        for sj in range(3):
            for si in range(3):
                # rot 횟수만큼 90도 시계 방향 회전 => narr
                narr = [x[:] for x in arr]
                for _ in range(rot):
                    narr = rotate(narr, si, sj)

                # 유물개수 카운트
                t = count_clear(narr, 0)
                if mx_cnt < t:  # 최대 개수
                    mx_cnt = t
                    marr = narr
    # 유물이 없는 경우 턴 즉시종료
    if mx_cnt == 0:
        break

    # [2] 연쇄획득
    cnt = 0
    arr = marr
    while True:
        t = count_clear(arr, 1)
        if t == 0:
            break  # 연쇄 획득 종료 => 다음 턴으로..
        cnt += t  # 획득한 유물 개수 누적

        # arr의 0값인 부분 리스트에서 순서대로 추가
        for j in range(5):
            for i in range(4, -1, -1):
                if arr[i][j] == 0:
                    arr[i][j] = lst.pop(0)

    ans.append(cnt)  # 이번턴 연쇄획득한 개수 추가

print(*ans)

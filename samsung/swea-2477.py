from collections import deque

N, M, K, A, B = map(int, input().split())
init_a = list(map(int, input().split()))
init_b = list(map(int, input().split()))

t_lst = list(map(int, input().split()))
for i in range(len(t_lst)):
    t_lst[i] = [i + 1, t_lst[i]]
t_lst.sort(key=lambda x: x[1])

# 대기열, 창구, 창구별 남은 시간
a_waiting = deque()
N, M, K, A, B = map(int, input().split())
init_a = list(map(int, input().split()))
init_b = list(map(int, input().split()))

t_lst = list(map(int, input().split()))
for i in range(len(t_lst)):
    t_lst[i] = [i + 1, t_lst[i]]
t_lst.sort(key=lambda x: x[1])

# 대기열, 창구, 창구별 남은 시간
a_waiting = deque()
a_lst = [0] * N
a_left = [0] * N
b_waiting = deque()
b_lst = [0] * M
b_left = [0] * M

# 시간, 서비스 완료 고객수, 고객별 창구 결과 값
t = 0
cnt = 0
k_dict = {}
for i in range(K):
    k_dict[i + 1] = [0, 0]

while cnt < K:
    while t_lst and t_lst[0][1] == t:
        a_waiting.append(t_lst.pop(0)[0])

    # 접수 창구
    for i in range(N):
        if a_lst[i] != 0:  # 접수 창구에 이미 사람이 있을 때
            a_left[i] -= 1  # 접수 창구 남은 시간 1 감소
            if a_left[i] == 0:  # 남은 시간이 0이 되었을 때
                b_waiting.append(a_lst[i])  # 정비 대기열로 넘어감
                k_dict[a_lst[i]][0] = i  # 해당 고객 번호 접수 창구 기록
                a_lst[i] = 0  # 접수 창구 비워둠

        # 접수 창구가 비어있을 때
        if a_lst[i] == 0:
            if a_waiting:  # 대기자가 있으면 대기자 창구에 넣어주고 남은 시간 초기화
                a_lst[i] = a_waiting.popleft()
                a_left[i] = init_a[i]

    # 정비 창구
    for j in range(M):
        if b_lst[j] != 0:  # 정비 창구에 이미 사람이 있을 때
            b_left[j] -= 1  # 정비 창구 남은 시간 1 감소
            if b_left[j] == 0:  # 남은 시간이 0이 되면
                k_dict[b_lst[j]][1] = j  # 해당 고객 번호 정비  창구 기록
                b_lst[j] = 0  # 정비 창구 비워둠
                cnt += 1  # 서비스 완료 고객 1 추가

        # 정비 창구가 비어있을 때
        if b_lst[j] == 0:
            if b_waiting:  # 정비 창구 대기자가 있으면 대기자 창구에 넣어주고 남은 시간 초기화
                b_lst[j] = b_waiting.popleft()
                b_left[j] = init_b[j]
    t += 1

ans = 0
for i in k_dict:
    if k_dict[i] == [A - 1, B - 1]:
        ans += i

print(-1 if ans == 0 else ans)
a_lst = [0] * N
a_left = [0] * N
b_waiting = deque()
b_lst = [0] * M
b_left = [0] * M

# 시간, 서비스 완료 고객수, 고객별 창구 결과 값
t = 0
cnt = 0
k_dict = {}
for i in range(K):
    k_dict[i + 1] = [0, 0]

while cnt < K:
    while t_lst and t_lst[0][1] == t:
        a_waiting.append(t_lst.pop(0)[0])

    # 접수 창구
    for i in range(N):
        if a_lst[i] != 0:  # 접수 창구에 이미 사람이 있을 때
            a_left[i] -= 1  # 접수 창구 남은 시간 1 감소
            if a_left[i] == 0:  # 남은 시간이 0이 되었을 때
                b_waiting.append(a_lst[i])  # 정비 대기열로 넘어감
                k_dict[a_lst[i]][0] = i  # 해당 고객 번호 접수 창구 기록
                a_lst[i] = 0  # 접수 창구 비워둠

        # 접수 창구가 비어있을 때
        if a_lst[i] == 0:
            if a_waiting:  # 대기자가 있으면 대기자 창구에 넣어주고 남은 시간 초기화
                a_lst[i] = a_waiting.popleft()
                a_left[i] = init_a[i]

    # 정비 창구
    for j in range(M):
        if b_lst[j] != 0:  # 정비 창구에 이미 사람이 있을 때
            b_left[j] -= 1  # 정비 창구 남은 시간 1 감소
            if b_left[j] == 0:  # 남은 시간이 0이 되면
                k_dict[b_lst[j]][1] = j  # 해당 고객 번호 정비  창구 기록
                b_lst[j] = 0  # 정비 창구 비워둠
                cnt += 1  # 서비스 완료 고객 1 추가

        # 정비 창구가 비어있을 때
        if b_lst[j] == 0:
            if b_waiting:  # 정비 창구 대기자가 있으면 대기자 창구에 넣어주고 남은 시간 초기화
                b_lst[j] = b_waiting.popleft()
                b_left[j] = init_b[j]
    t += 1

ans = 0
for i in k_dict:
    if k_dict[i] == [A - 1, B - 1]:
        ans += i

print(-1 if ans == 0 else ans)

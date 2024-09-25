from collections import deque


def solution(progresses, speeds):
    # 각각의 남은 일수를 먼저 계산하여
    # q 자료구조로 만들어준다.
    # 하나를 popleft한 후
    # 그 값보다 큰 값이 나올 때까지 popleft한다
    # 큰 값이 나오면 그 이전까지의 개수를 세어 정답 배열에 푸쉬한다
    answer = []
    left = [100 - i for i in progresses]
    left_d = deque()
    for i in range(len(left)):
        if left[i] % speeds[i] == 0:
            left_d.append(left[i] // speeds[i])
        else:
            left_d.append(left[i] // speeds[i] + 1)
    mx = 0
    count = 0
    while left_d:
        tmp = left_d.popleft()
        if tmp <= mx:
            count += 1
        else:
            mx = tmp
            if count != 0:
                answer.append(count)
            count = 1
    answer.append(count)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

from collections import deque


def solution(N, K):
    # N명의 사람들이 역순으로 들어가있는 큐 선언
    # K만큼 팝하여 푸쉬한 다음
    # 맨 뒤의 원소 팝
    # 1개만 남을 때까지 반복
    people = deque([N - i for i in range(N)])
    while len(people) > 1:
        for _ in range(K):
            people.appendleft(people.pop())
        people.popleft()
    return people[0]


print(solution(5, 2))

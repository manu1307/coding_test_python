from collections import deque


def solution(cards1, cards2, goal):
    # goal을 큐로 만들고
    # popleft한 원소가 card1이나 card2에 있는지 확인
    # 없으면 No 리턴
    # 있으면 해당 card popleft하고 그 다음 원소 진행
    queue = deque(goal)
    cards1queue = deque(cards1)
    cards2queue = deque(cards2)
    while queue:
        item = queue.popleft()
        if cards1queue and cards1queue[0] == item:
            cards1queue.popleft()
        elif cards2queue and cards2queue[0] == item:
            cards2queue.popleft()
        else:
            queue.appendleft(item)
            break
    return "Yes" if not queue else "No"


print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["list", "length", "important"], ["are", "very"], ["are", "very"]))

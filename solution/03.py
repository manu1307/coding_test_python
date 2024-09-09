def solution(numbers):
    # 왼쪽에 하나 고정하고
    # 고정된 곳 오른쪽 방향으로 끝까지 하나씩 탐색하며 연산
    # 연산값 추가하고
    # 중복 제거하여 정렬
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    answer = list(set(answer))
    answer.sort()
    return answer

# 시간복잡도 : O(N^2log(N^2))
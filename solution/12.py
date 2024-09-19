def solution(prices):
    n = len(prices)
    answer = [0] * n

    # 스택을 사용해 이전 가격과 현재 가격 비교
    stack = [0]  # 스택 초기화
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            # 가격이 떨어졌으니깐 이전 가격의 기간 계산
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # 스택에 남아있는 가격들은 가격이 안 떨어진 경우라 전체 길이에서 기간 세주면 됨
    while stack:
        t = stack.pop()
        answer[t] = n - 1 - t
    return answer


print(solution([1, 2, 3, 2, 3]))

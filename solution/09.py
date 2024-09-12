def solution(decimal):
    stack = []
    # 십진수가 몫이 1이 될 때까지
    while decimal > 0:
        # 십진수를 2로 나눠서
        # 나누어 떨어지면 나머지 0 push
        # 나누어 떨어지지 않으면 나머지 1 push
        stack.append(decimal % 2)
        # 십진수를 몫으로 값을 재설정
        decimal = decimal // 2
    answer = ""
    # 값을 역순으로 넣어서 하나의 수로 만들어준다.
    while stack:
        answer += str(stack.pop())
    return answer


# 시간복잡도 : O((logN)^2)
# join으로 하면 시간 복잡도를 더 낮출 수 있음


print(solution(10))
print(solution(27))
print(solution(12345))

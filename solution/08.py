def solution(s):
    # 스택 선언
    stack = []
    # 괄호를 하나씩 검사
    for i, parenthesis in enumerate(s):
        # 괄호가 ( 라면 append
        if parenthesis == "(":
            stack.append(parenthesis)
        # 괄호가 ) 라면
        if parenthesis == ")":
            # stack이 비어있으면 짝이 맞는 애가 없으므로 False
            if not stack:
                return False
            else:
                stack.pop()

    # stack이 남아있으면 False, 아니면 True
    result = True if len(stack) == 0 else False
    return result


# 시간 복잡도 : O(N)

print(solution("(())()"))
print(solution("((())()"))
print(solution(")("))

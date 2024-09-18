def solution(s):
    # 스택 선언
    # 문자열을 반복문으로 돌면서
    # 스택의 최상단과 현재 문자열을 비교하여
    # 같으면 팝
    # 다르면 푸쉬
    stack = []
    for i, s in enumerate(s):
        if len(stack) == 0:
            stack.append(s)
        else:
            if stack[len(stack) - 1] == s:
                stack.pop()
            else:
                stack.append(s)
    return 1 if len(stack) == 0 else 0


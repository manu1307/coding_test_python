# 올바른 괄호 문자열인지 확인하는 함수
def check_parentheses(s):
    # 스택 선언
    # 스택에서 하나 팝하고
    # 짝이 맞으면 넘어가고
    # 아니면 푸시한다
    stack = []
    for i, p in enumerate(s):
        if len(stack) == 0:
            stack.append(p)
            continue
        t = stack.pop()
        if (t == "(" and p == ")") or (t == "{" and p == "}") or (t == "[" and p == "]"):
            continue
        else:
            stack.append(t)
            stack.append(p)

    return True if len(stack) == 0 else False


def solution(s):
    # 반복문으로 모든 쉬프트 경우 돌면서
    # 올바른 괄호 문자열인지 확인
    # 맞으면 정답 하나 추가
    # 아니면 패스
    answer = 0
    s = list(s)
    for i in range(len(s)):
        if i != 0:
            s.append(s.pop(0))
        if check_parentheses("".join(s)):
            answer += 1

    return answer

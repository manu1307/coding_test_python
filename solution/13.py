def solution(board, moves):
    # 최대 O(N^3)이 될거 같긴 하나 위험하기에 그 미만으로 생각
    # 인형을 담을 스택 선언
    # move에서 인형을 하나 꺼낸다
    # 스택의 top에 넣고
    # top과 top-1을 비교
    # 만약 같으면 pop 2번 하고
    # 터뜨린 인형 2개 추가
    # 터진 후에 계속 top과 top-1을 비교하여 같은 과정 수행
    # 없으면 다음 move 수행
    answer = 0
    size = len(board)
    stack = []
    for move in moves:
        for i in range(size):
            if board[i][move - 1] != 0:
                stack.append(board[i][move - 1])
                board[i][move - 1] = 0
                if len(stack) > 1:
                    while stack[len(stack) - 1] == stack[len(stack) - 2]:
                        stack.pop()
                        stack.pop()
                        answer += 2
                        if len(stack) < 2:
                            break
                break
    return answer

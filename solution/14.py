# def solution(n, k, cmd):
#     # 길이가 n인 리스트 s 선언
#     # 삭제된 원소 담은 배열 deleted 선언
#     # 초기 index = k로 선언
#     # for문으로 cmd를 돈다
#     # D X 면
#     # index를 X 만큼 증가시킨다
#     # U X 면
#     # index를 X 만큼 감소시킨다
#     # C 면
#     # index가 마지막 원소를 가리킬 경우
#     # index 1 감소
#     # 아니라면 해당 인덱스의 원소 pop하여 deleted에 넣음
#     # Z 면
#     # 현재 인덱스 기준으로 배열을 나누고
#     # 복구시킬 값이 s[index]보다 크면
#     # 오른쪽 배열에 값 넣어주고 sort
#     # 작으면
#     # 왼쪽 배열에 값 넣어주고 sort
#     # 그리고 다시 합쳐준다
#     s = [i for i in range(n)]
#     deleted = []
#     index = k
#     for command in cmd:
#         if command.startswith("D"):
#             index += int(command.split(" ")[1])
#         if command.startswith("U"):
#             index -= int(command.split(" ")[1])
#         if command == "C":
#             if index == len(s):
#                 index -= 1
#             else:
#                 deleted.append(s.pop(index))
#         if command == "Z":
#             leftArr = s[:index]
#             rightArr = s[index:]
#             restoreItem = deleted.pop()
#             if restoreItem > s[index]:
#                 rightArr.append(restoreItem)
#                 s = leftArr + sorted(rightArr)
#             else:
#                 leftArr.append(restoreItem)
#                 s = sorted(leftArr) + rightArr
#
#     print(s, deleted)
#     answerList = ["O" for _ in range(n)]
#     for d in deleted:
#         answerList[d] = "X"
#     answer = "".join(answerList)
#     return answer
#
#
# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

def solution(n, k, cmd):
    # 삭제된 행의 인덱스를 저장하는 리스트
    deleted = []

    # 링크드리스트에서 각 행 위아래의 행의 인덱스를 저장하는 리스트
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]

    # 현재 위치를 나타내는 인덱스
    k += 1

    # 주어진 명령어 리스트 하나씩 처리
    for cmd_i in cmd:
        if cmd_i.startswith("C"):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
        elif cmd_i.startswith("Z"):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore

        # U 또는 D를 사용해 현재 위치를 위 아래로 이동
        else:
            action, num = cmd_i.split(" ")
            if action == "U":
                for _ in range(int(num)):
                    k = up[k]
            if action == "D":
                for _ in range(int(num)):
                    k = down[k]
    answer = ["O" for _ in range(n)]
    for i in deleted:
        answer[i - 1] = "X"
    return "".join(answer)


# 상대 인덱스를 활용하여 링크드 리스트를 활용
# 시간 복잡도 O(N)

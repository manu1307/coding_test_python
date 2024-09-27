def solution(record):
    # uid 별로 닉네임을 구별할 딕셔너리 생성
    # record를 돌면서
    # Enter면 [uid, "님이 들어왔습니다"]를 정답 배열에 넣고
    # uid 값을 딕셔너리에 넣어준다
    # Leave면 [uid, "님이 나갔습니다"]를 정답 배열에 넣는다
    # Change면 딕셔너리의 uid를 찾아 값을 수정
    # 정답 배열을 돌면서 해당하는 uid의 값을 딕셔너리에 찾아서 문자열로 조인
    uid_dict = {}
    message_list = []
    for r in record:
        if r.startswith("Enter"):
            cmd, uid, nickname = r.split(" ")
            uid_dict[uid] = nickname
            message_list.append([uid, "님이 들어왔습니다."])
        elif r.startswith("Leave"):
            cmd, uid = r.split(" ")
            message_list.append([uid, "님이 나갔습니다."])
        else:
            cmd, uid, nickname = r.split(" ")
            uid_dict[uid] = nickname
    answer = []
    for m in message_list:
        answer.append(uid_dict[m[0]] + m[1])

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))

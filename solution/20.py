def solution(participant, completion):
    # 빈 딕셔너리 2개를 만들어준다
    # completion을 순회하며
    # 딕셔너리에 완주자 명단을 만든
    # participant에도 같은 작업 수행
    # completion에 키가 존재하지 않거나
    # 값이 다를 경우
    # 바로 리턴한다.
    d_complete = {}
    d_participant = {}
    for complete in completion:
        d_complete[complete] = 1 if complete not in d_complete else d_complete[complete] + 1
    for par in participant:
        d_participant[par] = 1 if par not in d_participant else d_participant[par] + 1

    for key in d_participant.keys():
        if key not in d_complete or d_complete[key] != d_participant[key]:
            return key


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

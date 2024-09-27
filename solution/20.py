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


def solution2(participant, completion):
    # 해시 테이블 생성
    dic = {}

    # 참가자들의 이름을 해시 테이블에 추가
    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1

    # 완주한 선수들의 이름을 키로 하는 값을 1씩 감소
    # 위의 풀이에서는 모든 값을 저장했지만
    # 해당 풀이는 하나의 딕셔너리를 가지고 조작하기에 메모리가 덜 점유됨
    for c in completion:
        dic[c] -= 1

    for key in dic.keys():
        if dic[key] > 0:
            return key


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution2(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

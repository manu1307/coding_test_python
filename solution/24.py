def solution(id_list, report, k):
    # 신고횟수를 측정하기 위한 딕셔너리를 선언
    # 해당 아이디를 신고한 명단을 저장하기 위한 딕셔너리 선언
    # 결과를 담을 리스트 선언
    # 각각의 id의 인덱스를 매핑한 딕셔너리 선언
    # report를 순회하며
    # 신고자 딕셔너리에 넣어주는 대신 겹치지 않도록 set을 사용한다
    # 신고횟수는 set의 길이로 넣어준다
    # 신고횟수 딕셔너리의 items들을 순회하며 k 이상이면
    # 신고자들 명단을 순회하며 리스트에서 해당 인덱스 값을 1씩 추가해준다

    count_dict = {}
    report_dict = {}
    result = [0 for _ in range(len(id_list))]
    id_idx = {}
    for i in range(len(id_list)):
        count_dict[id_list[i]] = 0
        report_dict[id_list[i]] = set([])
        id_idx[id_list[i]] = i

    for r in report:
        reporter, suspect = r.split(" ")
        report_dict[suspect] = set.union(report_dict[suspect], {reporter})
        count_dict[suspect] = len(report_dict[suspect])

    for s, count in count_dict.items():
        if count >= k:
            for reporter in list(report_dict[s]):
                result[id_idx[reporter]] += 1

    return result


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"],
               3))

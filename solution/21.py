def solution(want, number, discount):
    # want와 number를 조합하여 딕셔너리를 하나 만든다
    # discount를 순회할 포인터를 하나 선언
    # 포인터를 기준으로 10개씩 카운트하면서
    # 10개 구성을 담은 딕셔너리를 만든다
    # want 딕셔너리와 조합하여 비교해서
    # 같은 구성이면 1 추가
    answer = 0
    n = 10
    want_dic = {}
    for i in range(len(want)):
        want_dic[want[i]] = number[i]

    for ptr in range(len(discount) - n + 1):
        disc_slice = discount[ptr:ptr + n]
        want_dic_copy = dict.copy(want_dic)
        for t in disc_slice:
            if t not in want_dic_copy:
                break
            else:
                want_dic_copy[t] -= 1

        if list(want_dic_copy.values()) == [0 for _ in range(len(want))]:
            answer += 1

    return answer




print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                "banana", "apple", "banana"]))
print(solution(["apple"], [10],
               ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))

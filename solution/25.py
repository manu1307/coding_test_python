from itertools import combinations
from collections import Counter


def solution(orders, course):
    # 각 단품메뉴들로 만들 수 있는 조합들을 키 값으로 하고 횟수를 담을 딕셔너리 선언
    # 메뉴 길이를 키 값으로 하고 조합들을 밸류로 담을 딕셔너리 선언
    # course를 순회하며 해당하는 길이의 조합들을 순회하여
    # 최소 2번 이상 불렸는지 확인
    # 그리고 횟수가 최대인 키 값을 찾아 result에 넣어준다
    # result를 오름차순으로 정렬
    answer = []
    combos = []
    combo_dict = {}
    len_dict = {}
    for i in orders:
        for j in range(1, len(i) + 1):
            combo_tuple = list(combinations(i, j))
            combo_str = list(map(lambda x: "".join(sorted(x)), combo_tuple))
            combos = combos + combo_str
    for c in combos:
        combo_dict[c] = combo_dict.get(c, 0) + 1
        if len(c) not in len_dict:
            len_dict[len(c)] = [c]
        else:
            len_dict[len(c)].append(c)

    for cnt in course:
        if cnt not in len_dict:
            continue
        mx = []
        mx_cnt = 0
        for menus in len_dict[cnt]:
            if combo_dict[menus] >= 2:
                if combo_dict[menus] == mx_cnt:
                    mx.append("".join(menus))
                elif combo_dict[menus] > mx_cnt:
                    mx_cnt = combo_dict[menus]
                    mx.clear()
                    mx.append("".join(menus))
        answer = answer + list(set(mx))

    return sorted(answer)


def solution2(orders, course):
    answer = []
    for c in course:  # 각 코스 요리 길에 대해
        menu = []
        for order in orders:  # 모든 주문에 대해
            comb = combinations(sorted(order), c)  # 조합을 이용해 가능한 메뉴 구성을 모두 구함
            menu += comb

        counter = Counter(menu)  # 각 메뉴 구성이 몇 번 주문되었는지 세어줌

        if len(counter) != 0 and max(counter.values()) != 1:  # 가장 많이 주문된 구성이 1번 이상 주문된 경우
            for m, cnt in counter.items():
                if cnt == max(counter.values()):  # 가장 많이 주문된 구성을 찾아서
                    answer.append("".join(m))
    return sorted(answer)


print(solution2(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))

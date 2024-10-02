def solution(enroll, referral, seller, amount):
    # 결과를 담고 있을 배열 선언 - 초깃값은 다 0
    # enroll 명단의 index 딕셔너리로 매핑
    # seller와 amount 딕셔너리 매핑
    # 딕셔너리 아이템을 순회하면서
    # "-"가 나올 때까지
    # 값이 한 자리수가 아니면
    # result[enroll[seller]]에 90퍼 추가해주고
    # result[referral[seller]]에 10퍼 추가
    # seller를 referral로 교체
    # 값이 한 자리수면
    # result[enroll[seller]]에 다 추가하고 리턴
    result = [0 for _ in range(len(enroll))]
    enroll_idx = {}
    for i in range(len(enroll)):
        enroll_idx[enroll[i]] = i

    for i in range(len(seller)):
        s = seller[i]
        a = amount[i] * 100
        while a>0 and s != "-":
            result[enroll_idx[s]] += a - a // 10
            s = referral[enroll_idx[s]]
            a //= 10

    return result


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))


# 오답 노트 : seller는 중복해서 나올 수 있다고 했다. 결과를 모두 합산할 경우 분배금 처리가 달라질 수 있어
# 합산한 후 계산하는 방식이 아니라 각각의 판매에 맞춰서 계산되어야함
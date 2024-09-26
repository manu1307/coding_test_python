def solution(arr, target):
    # 빈 dict 선언
    # arr를 반복문으로 돌면서
    # dict에 target을 만들 수 있는 쌍이 있는지 검사
    # 있으면 True
    # 없으면 dict에 숫자가 키, target을 만들 수 있는 쌍을 값으로 하는 애를 넣어준다
    d = {}
    for i in arr:
        if target - i in d:
            return True
        else:
            d[i] = target - i
    return False


print(solution([1, 2, 3, 4, 8], 6))
print(solution([2, 3, 5, 9], 10))

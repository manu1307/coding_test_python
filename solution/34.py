def solution(nums):
    # 뽑을 수 있는 폰켓몬의 수 선언
    # nums를 돌면서 폰켓몬의 종류와 수를 딕셔너리에 담는다
    # 만약 종류 >= 뽑을 수 있는 폰켓몬의 수 라면 최대는 폰켓몬의 수
    # 아니라면 종류 만큼 뽑을 수 있음

    np = len(nums) // 2
    p_dict = {}
    for n in nums:
        p_dict[n] = p_dict.get(n, 0) + 1
    k = len(p_dict.keys())
    answer = np if np < k else k
    return answer


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))

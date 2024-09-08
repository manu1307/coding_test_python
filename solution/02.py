# 테스트 케이스
# print(solution([4, 2, 2, 1, 3, 4])) # 반환값 : [4, 3, 2, 1]
# print(solution([2, 1, 1, 3, 2, 5, 4])) # 반환값 : [5, 4, 3, 2, 1]

def solution(array):
    remove_overlap_array = list(set(array))
    remove_overlap_array.sort(reverse=True)
    return remove_overlap_array

# 집합은 중복값을 허용하지 앉으므로 중복 문제 한 번에 해결 가능
# 파이썬에서는 코테에 유용한 함수가 많다.
# 굳이 직접 작성하려 하지 마라

# set()의 시간 복잡도는 O(N)



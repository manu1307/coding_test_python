# 테스트 케이스
# print(solution([1, -5, 2, 4, 3]))  # 반환값 : [-5, 1, 2, 3, 4]
# print(solution([2, 1, 1, 3, 2, 5, 4]))  # 반환값 : [1, 1, 2, 2, 3, 4, 5]
# print(solution([1, 6, 7]))  # 반환값 : [1, 6, 7]

def solution(array):
    array.sort()
    return array


# sort() 메서드는 원본 자체의 값을 바꿈


# 다른 풀이
def solution2(array):
    sorted_array = sorted(array)
    return sorted_array

# sort 메서드의 시간 복잡도는 O(NlogN)
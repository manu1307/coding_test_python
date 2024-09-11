def solution(arr1, arr2):
    # arr1의 행과 arr2의 열을 곱한다
    # 각각의 원소를 곱해서 더한다
    # i = arr1의 행 개수
    # j = arr2의 열 개수
    # k = arr2의 행 개수
    answer = []
    for i in range(len(arr1)):
        arr = []
        for j in range(len(arr2[0])):
            sum = 0
            for k in range(len(arr2)):
                sum += arr1[i][k] * arr2[k][j]
            arr.append(sum)
        answer.append(arr)

    return answer

# 시간 복잡도 : O(N^3)


def solution2(arr1, arr2):
    # 행렬 arr1과 arr2의 행과 열의 수
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    # 결과를 저장할 2차원 리스트
    ret = [[0] * c2 for _ in range(r1)]

    # arr1의 각 행과 arr2의 가 열에 대하여
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                ret[i][j] += arr1[i][k] * arr2[k][j]

    return ret


print(solution2([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))

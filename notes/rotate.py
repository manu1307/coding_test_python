# 2차원 행렬 회전

# 1 2 3      7 4 1
# 4 5 6  ->  8 5 2
# 7 8 9      9 6 3
# arr1   ->   arr2


def rotate():
    arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arr2 = [x[:] for x in arr1]
    for i in range(3):  # 회전시킬 사각형 크기만큼
        for j in range(3):
            # 회전한 후의 열 = 회전되기 전의 행
            # 회전한 후의 행 = (크기 - 1) - 회전되기 전의 열
            arr2[i][j] = arr1[3 - 1 - j][i]
    arr1 = arr2
    return arr1


print(rotate())

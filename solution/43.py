def solution(n, computers):
    # visited에서 미방문한 컴퓨터면 dfs
    # visited는 컴퓨터의 길이만큼
    answer = 0
    visited = [0 for _ in range(n)]

    def dfs(c):
        visited[c] = 1
        for i in range(n):
            if visited[i] == 0 and computers[c][i] == 1:
                visited[i] = 1
                dfs(i)

    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

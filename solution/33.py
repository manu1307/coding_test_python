# union =  두 집합 합 치기
# find = 루트 노드 찾기

def find(parents, x):
    # 만약 본인이랑 부모가 같은 노드면 루트 노드
    if parents[x] == x:
        return x
    # 그렇지 않으면 x의 부모를 찾아서 parents[x]에 저장
    # 부모 노드의 루트 노드를 찾아서 parents[x]에 저장한 후 리턴
    parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents, x, y):
    # 각 집합의 루트 노드 찾은 후
    root1 = find(parents, x)
    root2 = find(parents, y)
    # 숫자가 큰 놈 아래에 숫자가 작은 놈 넣어준다
    parents[root2] = root1


def solution(k, operations):
    parents = [i for i in range(k)]

    for o in operations:
        if o[0] == "u":
            union(parents, o[1], o[2])
        elif o[0] == "f":
            find(parents, o[1])

    tmp = []
    for i in range(k):
        tmp.append(find(parents, i))

    tmp = set(tmp)

    return len(tmp)


print(solution(3, [["u", 0, 1], ["u", 1, 2], ["f", 2]]))
print(solution(4, [["u", 0, 1], ["u", 2, 3], ["f", 0]]))

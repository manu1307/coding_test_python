def preorder(nodes, idx):
    # 가장 루트에 있는 거 출력하고
    # 트리가 없을 경우 그냥 리턴
    # 왼쪽 트리에 대해서 preorder 한다
    # 오른쪽 트리에 대해서 preorder 한다
    if idx < len(nodes):
        ret = str(nodes[idx]) + " "
        ret += preorder(nodes, idx * 2 + 1)
        ret += preorder(nodes, idx * 2 + 2)
        return ret
    else:
        return ""


def inorder(nodes, idx):
    # 왼쪽 트리 출력
    # 기준 노드 출력
    # 오른쪽 트리 출력
    if idx < len(nodes):
        ret = inorder(nodes, idx * 2 + 1)
        ret += str(nodes[idx]) + " "
        ret += inorder(nodes, idx * 2 + 2)
        return ret
    else:
        return ""


def postorder(nodes, idx):
    # 왼쪽 트리 출력
    # 오른쪽 트리 출력
    # 기준 노드 출력
    if idx < len(nodes):
        ret = postorder(nodes, idx * 2 + 1)
        ret += postorder(nodes, idx * 2 + 2)
        ret += str(nodes[idx]) + " "
        return ret
    else:
        return ""


def solution(nodes):
    return [preorder(nodes, 0)[:-1], inorder(nodes, 0)[:-1], postorder(nodes, 0)[:-1]]


print(solution([1, 2, 3, 4, 5, 6, 7]))

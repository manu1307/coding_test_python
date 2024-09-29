# 노드 클래스 정의
class Node:
    # 노드 클래스 생성자
    def __init__(self, v):
        self.left = None
        self.right = None
        self.value = v


# 이진 탐색 트리 클래스
class BST:
    # 초기에는 아무 노드도 없는 상태
    def __init__(self):
        self.root = None

    # 루트 노브부터 시작해서 이진탐색 트리 규칙에 맞게 새 노드 삽입
    def insert(self, v):
        # 루트 노드가 없는 경우에 새로운 노드를 루트 노드로 추가
        if not self.root:
            self.root = Node(v)
        else:
            curr = self.root
            while True:
                # 삽입하려는 값에 따라 왼쪽 자식 노드로 이동할지 오른쪽 자식 노드로 이동할지 결정
                if v < curr.value:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(v)
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(v)
                        break

    # 이진 탐색 규칙에 따라 특정값이 있는지 확인(루트 노드부터 시작)
    def search(self, v):
        curr = self.root
        # 현재 노드가 존재하고, 찾으려는 값과 현재 노드의 값이 같이 않은 경우 반복
        while curr and curr.value != v:
            if v < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return curr


def solution(lst, search_lst):
    bst = BST()
    for v in lst:
        bst.insert(v)

    result = []
    for s in search_lst:
        if bst.search(s):
            result.append(True)
        else:
            result.append(False)
    return result


print(solution([5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6]))

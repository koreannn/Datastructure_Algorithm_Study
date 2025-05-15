from binary_tree import BinaryTree
"""
ADT: 데이터의 삽입, 삭제, 제거
"""

"""
이진 탐색 트리 구현
"""
class BinarySearchTree:
    def __init__(self, root_node=None):
        self.root = root_node  # 루트 노드
    
    def insert(self, data):
        if self.root is None: 
            self.root = BinaryTree(data) # 루트 노드가 비어있을 경우 새로운 이진 트리 생성
            return
        
        curr_node = self.root 
        parent_node = None # 맨 처음 루트 노드의 부모 노드 (자식 -> 부모 방향의 참조는 안되지만, 부모 -> 자식 방향의 참조는 가능하므로)
        
        # 삽입할 위치 탐색
        while curr_node is not None: # 더이상 자식 노드가 없을때까지
            parent_node = curr_node
            
            if curr_node.getData() > data:
                curr_node = curr_node.getLeftSubTree()  # 현재 노드의 값보다 작으면 왼쪽 서브트리의 값과 비교
            elif curr_node.getData() < data:
                curr_node = curr_node.getRightSubTree() # 현재 노드 값보다 크면 오른쪽 서브트리의 값과 비교
            else:
                return
        
        # 깂(서브트리) 삽입
        new_node = BinaryTree(data)
        
        if parent_node.getData() > data: # (parrent_node == curr_node)
            parent_node.setLeftSubTree(new_node)
        else:
            parent_node.setRightSubTree(new_node)
            
    def search(self, target_data):
        curr_node = self.root
        
        while curr_node is not None:
            if curr_node.getData() == target_data:
                return curr_node
            elif curr_node.getData() > target_data:
                curr_node = curr_node.getLeftSubTree()
            else:
                curr_node = curr_node.getRightSubTree()
        
        return None
    
    
    def remove(self, target):
        fakeParentRootNode = BinaryTree(0)  # 루트 노드가 제거되는 경우 필요
        parentNode = fakeParentRootNode
        curr_node = self.root
        deleted_node = None
        
        fakeParentRootNode.setRightSubTree(self.root)  # setLeftSubTree()로 해도 상관없음
        
        # 삭제할 노드 찾기
        while curr_node is not None and curr_node.getData() != target:
            parentNode = curr_node
            
            if curr_node.getData() > target:
                curr_node = curr_node.getLeftSubTree()
            else:
                curr_node = curr_node.getRightSubTree()
        
        # 삭제할 노드를 찾지 못한 경우
        if curr_node is None:
            return None
            
        # Case 분류
        deleted_node = curr_node
        
        # 1. 제거하는 노드가 터미널 노드인 경우
        if (deleted_node.getLeftSubTree() is None and deleted_node.getRightSubTree() is None):
            if parentNode.getLeftSubTree() == deleted_node:
                parentNode.removeLeftSubTree()
            else:
                parentNode.removeRightSubTree()
                
        # 2. 제거하는 노드의 자식 노드가 한 개인 경우
        elif deleted_node.getLeftSubTree() is None or deleted_node.getRightSubTree() is None:
            deleted_node_child = None
            # 제거할 노드의 자식 노드 찾기
            if deleted_node.getLeftSubTree() is not None:
                deleted_node_child = deleted_node.getLeftSubTree()
            else:
                deleted_node_child = deleted_node.getRightSubTree()
                
            # 제거 후 자식 트리로 대신 연결
            if parentNode.getLeftSubTree() == deleted_node:
                parentNode.setLeftSubTree(deleted_node_child)
            else:
                parentNode.setRightSubTree(deleted_node_child)
                
        # 3. 제거하는 노드의 자식 노드가 두 개인 경우
        else:
            replacingNode = deleted_node.getLeftSubTree()
            replacingNodeParent = deleted_node
            
            # 왼쪽 서브트리에서 가장 큰 값 찾기
            while replacingNode.getRightSubTree() is not None:
                replacingNodeParent = replacingNode
                replacingNode = replacingNode.getRightSubTree()
            
            # 데이터 교환
            deleted_node.setData(replacingNode.getData())
            
            # replacingNode 제거
            if replacingNodeParent.getLeftSubTree() == replacingNode:
                replacingNodeParent.setLeftSubTree(replacingNode.getLeftSubTree())
            else:
                replacingNodeParent.setRightSubTree(replacingNode.getLeftSubTree())
            
            deleted_node = replacingNode
        
        # 루트 노드가 변경된 경우 처리
        if fakeParentRootNode.getRightSubTree() != self.root:
            self.root = fakeParentRootNode.getRightSubTree()
        
        return deleted_node


bst = BinarySearchTree()
bst.insert(18)
bst.insert(15)
bst.insert(10)
bst.insert(6)
bst.insert(3)
bst.insert(8)
bst.insert(12)
bst.insert(11)
bst.insert(31)
bst.insert(27)
bst.insert(24)
bst.insert(20)
bst.insert(33)
bst.insert(35)
bst.insert(37)
bst.root.inOrderTraversal(bst.root) # 중위 순회

print("========== Search 6 ==========")
print(bst.search(6))


print("========== Search 1 ==========")
print(bst.search(1))

# remove메서드 테스트
print("========== Remove Test ==========")
bst.remove(10)
bst.root.inOrderTraversal(bst.root)
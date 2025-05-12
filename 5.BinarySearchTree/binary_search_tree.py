"""
ADT: 데이터의 삽입, 삭제, 제거
"""

"""
이진트리 객체 가져오기(이전 코드와 동일)
"""
class BinaryTree:
    def __init__(self, data, LeftTree=None, RightTree=None):
        self.data = data
        self.LeftTree = LeftTree
        self.RightTree = RightTree
    
    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data
        
    def getLeftSubTree(self):
        return self.LeftTree

    def getRightSubTree(self):
        return self.RightTree
    
    def setLeftSubTree(self, tree):
        self.LeftTree = tree
    
    def setRightSubTree(self, tree):
        self.RightTree = tree
    
    def preOrderTraversal(self, tree):
        if tree == None:
            return
        print(tree.data)
        self.preOrderTraversal(tree.getLeftSubTree())
        self.preOrderTraversal(tree.getRightSubTree())
        
    def inOrderTraversal(self, tree):
        if tree == None:
            return
        self.inOrderTraversal(tree.getLeftSubTree())    # 왼쪽 서브트리 순회
        print(tree.data)                 # 현재 노드 데이터 출력
        self.inOrderTraversal(tree.getRightSubTree())   # 오른쪽 서브트리 순회
        
    def postOrderTraversal(self, tree):
        if tree == None:
            return

        self.postOrderTraversal(tree.getLeftSubTree())
        self.postOrderTraversal(tree.getRightSubTree())
        print(tree.data)
        
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
        
        if parent_node.getData() > data:
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

print("========== Search 6 ==========");
print(bst.search(6));


print("========== Search 1 ==========");
print(bst.search(1));
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
### test

'''
1. 포화 이진 트리 만들기
'''
tree1 = BinaryTree(1)
tree2 = BinaryTree(2)
tree3 = BinaryTree(3)
tree4 = BinaryTree(4)
tree5 = BinaryTree(5)
tree6 = BinaryTree(6)
tree7 = BinaryTree(7)

tree1.setLeftSubTree(tree2)
tree1.setRightSubTree(tree3)
tree2.setLeftSubTree(tree4)
tree2.setRightSubTree(tree5)
tree3.setLeftSubTree(tree6)
tree3.setRightSubTree(tree7)

print("전위 순회")
tree1.preOrderTraversal(tree1)

print("중위 순회")
tree1.inOrderTraversal(tree1)

print("후위 순회")
tree1.postOrderTraversal(tree1)
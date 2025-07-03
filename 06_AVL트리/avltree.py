from binary_tree import BinaryTree

class BinarySearchTree:
    def __init__(self, root_node=None):
        self.root = root_node  # 루트 노드
            
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
    
    def getHeight(self, node):
        if node is None:
            return 0
        else:
            return node.height
    
    def updateHeight(self, node):
        leftChildHeight = self.getHeight(node.getLeftSubTree())
        rightChildHeight = self.getHeight(node.getRightSubTree())
        node.Height = max(leftChildHeight, rightChildHeight) + 1
        return
    
    def getBalanceFactor(self, node):
        return self.getHeight(node.getLeftSubTree()) - self.getHeight(node.getRightSubTree()) # 값이 양수: 왼쪽 노드 높이 > 오른쪽 노드 높이 / 값이 음수: ..
    
    def rotateLeft(self, node):
        childNode = node.getRightSubTree()
        node.setRightSubTree(childNode.getLeftSubTree())
        childNode.setLeftSubTree(node)
        
        self.updateHeight(node)
        self.updateHeight(childNode)
        
    def retateRight(self, node):
    



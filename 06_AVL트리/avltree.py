from binary_tree import BinaryTree

class AVLTree:
    def __init__(self, root=None):
        self.root = root
        
        
    def search(self, key):
        node = self.root
        while node:
            if node.getData() == key:
                return node
            elif key < node.getData():
                node = node.getLeftSubTree()
            else: # key > node.getData()
                node = node.getRightSubTree()
        return None
    
    
    def getHeight(self, node):
        return node.height if node else 0
    
    
    def updateHeight(self, node):
        left_height = self.getHeight(node.getLeftSubTree())
        right_height = self.getHeight(node.getRightSubTree())
        node.height = max(left_height, right_height) + 1
        
        
    def getBalanceFactor(self, node): 
        return self.getHeight(node.getLeftSubTree()) - self.getHeight(node.getRightSubTree())
    
    
    def rotateLeft(self, z): # 왼쪽으로 회전시키는 함수
        y = z.getRightSubTree()
        T2 = y.getLeftSubTree()
        
        y.setLeftSubTree(z)
        z.setRightSubTree(T2)
        
        self.updateHeight(z)
        self.updateHeight(y)
        return y
    
    
    def rotateRight(self, z): # 오른쪽으로 회전시키는 함수
        y = z.getLeftSubTree()
        T3 = y.getRightSubTree()
        
        y.setRightSubTree(z)
        z.setLeftSubTree(T3)
        
        self.updateHeight(z)
        self.updateHeight(y)
        return y
    
    
    def rebalance(self, node, key):
        balance_factor = self.getBalanceFactor(node)
        
        # LL
        if balance_factor > 1 and key < node.getLeftSubTree().getData():
            return self.rotateRight(node)
        
        # RR
        if balance_factor < -1 and key > node.getRightSubTree().getData():
            return self.rotateLeft(node)
        
        # LR
        if balance_factor > 1 and key > node.getLeftSubTree().getData():
            node.setLeftSubTree(self.rotateLeft(node.getLeftSubTree()))
            return self.rotateRight(node)
        
        # RL
        if balance_factor < -1 and key < node.getRightSubTree().getData():
            node.setRightSubTree(self.rotateRight(node.getRightSubTree()))
            return self.rotateLeft(node)
        
        return node
    
    
    def insert(self, node, key):
        if not node:
            return BinaryTree(key)
        
        if key == node.getData():
            return node
        
        elif key < node.getData():
            node.setLeftSubTree(self.insert(node.getLeftSubTree(), key))
            
        else:
            node.setRightSubTree(self.insert(node.getRightSubTree(), key))
        
        self.updateHeight(node)
        return self.rebalance(node, key)
    
    
    def _minValueNode(self, node):
        curr = node
        while curr.getLeftSubTree():
            curr = curr.getLeftSubTree()
        return curr
    
    
    def remove(self, node, key):
        if not node:
            return node
        
        if key < node.getData():
            node.setLeftSubTree(self.remove(node.getLeftSubTree(), key))
        
        elif key > node.getData():
            node.setRightSubTree(self.remove(node.getRightSubTree(), key))
            
        else:
            # 자식 노드가 1개 or 0개인 경우
            if not node.getLeftSubTree():
                tmp = node.getRightSubTree()
                node = None
                return tmp
            elif not node.getRightSubTree():
                tmp = node.getLeftSubTree()
                node = None
                return tmp
            
            # 자식 노드가 2 개일 경우
            tmp = self._minValueNode(node.getRightSubTree())
            node.setData(tmp.getData())
            node.setRightSubTree(self.remove(node.getRightSubTree(), tmp.getData()))
            
        if not node:
            return node
        
        self.updateHeight(node)
        return self.rebalance(node, key)
    
    
if __name__ == "__main__":
    avl_tree = AVLTree()
    
    for x in [1,2,3,4,5,6,7]:
        avl_tree.root = avl_tree.insert(avl_tree.root, x)
    
    print("After inserts(in-order): ")
    avl_tree.root.inOrderTraversal(avl_tree.root)
    print()
    
    for x in [2,3,1]:
        avl_tree.root = avl_tree.remove(avl_tree.root, x)
    print("After deletes(in-order): ")
    avl_tree.root.inOrderTraversal(avl_tree.root)
    print()
    
    print("Search 7: ", avl_tree.search(7).getData() if avl_tree.search(7) else None)

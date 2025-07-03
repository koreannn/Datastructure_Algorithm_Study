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
        self.inOrderTraversal(tree.getLeftSubTree())
        print(tree.data)
        self.inOrderTraversal(tree.getRightSubTree())
        
    def postOrderTraversal(self, tree):
        if tree == None:
            return

        self.postOrderTraversal(tree.getLeftSubTree())
        self.postOrderTraversal(tree.getRightSubTree())
        print(tree.data)
        
    def removeLeftSubTree(self):
        removed_tree = self.getLeftSubTree()
        self.setLeftSubTree(None)
        return removed_tree
        
    def removeRightSubTree(self):
        removed_tree = self.getRightSubTree()
        self.setRightSubTree(None)
        return removed_tree
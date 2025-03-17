class Node:
    def __init__(self, data):
        self.data = 0
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_at(self, index, data): # 연결리스트의 끝단에 데이터 삽입
        new_node = Node()
        if index == 0:
            new_node.next = self.head
            new_node.data = data
        
    def delete_at(self, index): # 값의 삭제(인덱스 기반)
        

class Stack:
    def __init__(self, linked_list):
        self.linkedlist = linked_list
    
    def push(self, data):
        if linked_list.head == None: # 첫 번쨰 데이터일 경우
            new_node = Node()
            new_node.data = data
            self.linkedlist.append(new_node)
        else:
        
        
    def pop(self):
        self.linkedlist.delete_at(-1)
        
    def peek():
    
    def is_empty():
        

if __name__ == "__main__":
    linked_list = Linkedlist()
    stack = Stack(linked_list)
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    
from singledir_linkedlist import singledirlinkedlist
from singledir_linkedlist import Node

class Stack:
    def __init__(self):
        self.linkedlist = singledirlinkedlist()
    
    def push(self, data):
        if self.linkedlist.head == None: # 첫 번쨰 데이터일 경우
            self.linkedlist.append(data)
        else:
            self.linkedlist.insert_at(0, data)
        
    def pop(self):
        self.linkedlist.delete_at(0)
        
    def peek(self):
        return self.linkedlist.read_at(0)
        
    
    def print_all(self):
        self.linkedlist.print_all()
        
    def is_empty(self):
        return not self.linkedlist.head # 없으면 True반환

if __name__ == "__main__":
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_all()
    print(stack.is_empty())
    
    stack.pop()
    stack.print_all()
    stack.pop()
    stack.print_all()
    stack.pop()
    stack.print_all()
    print(stack.is_empty())
    
    stack.push(4)
    print(stack.peek())
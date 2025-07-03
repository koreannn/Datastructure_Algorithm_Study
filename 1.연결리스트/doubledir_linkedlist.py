class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublelinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def print_all(self):
        if self.head == None:    
            print("리스트가 비어있습니다")
            return 
        curr = self.head
        while curr:
            print(curr.data, end=" <-> " if curr.next else "\n")
            curr = curr.next
            
    def print_reverse(self):
        if self.tail == None:
            print("리스트가 비어있습니다")
            return
        curr = self.tail
        while curr:
            print(curr.data, end=" <-> " if curr.prev else "\n")
            curr = curr.prev
    
    def append(self, data):    # 끝에 노드 추가
        new_node = Node(data)
        if self.head == None:    # 처음일 경우
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def prepend(self, data):    # 앞에 노드 추가
        new_node = Node(data)
        if self.head == None:    
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    def clear(self):
        self.head = None
        self.tail = None
        
    def insert_at(self, idx, data):
        if idx < 0:
            return
            
        if idx == 0: 
            self.prepend(data)
            return
            
        new_node = Node(data)
        curr = self.head
        for _ in range(idx-1):    
            if curr == None:   
                return
            curr = curr.next
            
        if curr == None:    
            return
            
        if curr.next == None:    # 맨 끝 삽입
            curr.next = new_node
            new_node.prev = curr
            self.tail = new_node
        else:    # 중간 삽입
            new_node.next = curr.next
            new_node.prev = curr
            curr.next.prev = new_node
            curr.next = new_node
    
    def delete_at(self, idx):   
        if self.head == None or idx < 0:
            return None
        
        if idx == 0:    # 첫 노드 삭제
            removed_data = self.head.data
            self.head = self.head.next
            if self.head:    # 노드가 하나 이상 남아있는 경우
                self.head.prev = None
            else:    # 마지막 노드를 삭제한 경우
                self.tail = None
            return removed_data
            
        curr = self.head
        for _ in range(idx-1):
            if curr == None:
                return None
            curr = curr.next
            
        if curr == None or curr.next == None:    # 인덱스가 범위를 벗어난 경우
            return None
            
        removed_data = curr.next.data
        curr.next = curr.next.next
        if curr.next:    # 중간 노드를 삭제하는 경우
            curr.next.prev = curr
        else:    # 마지막 노드를 삭제하는 경우
            self.tail = curr
            
        return removed_data
        
    def remove_last(self):    # 마지막 노드 삭제
        if self.tail == None:
            return None
            
        removed_data = self.tail.data
        if self.head == self.tail:    # 노드가 하나만 있는 경우
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            
        return removed_data
        
    def read_at(self, idx):
        if idx < 0:
            return None
            
        curr = self.head
        for _ in range(idx):
            if curr == None:
                return None
            curr = curr.next
            
        return curr.data if curr else None
        
    def find(self, data):    # 값으로 인덱스 찾기
        curr = self.head
        idx = 0
        while curr:
            if curr.data == data:
                return idx
            curr = curr.next
            idx += 1
        return -1    # 찾지 못한 경우
        
    def is_empty(self):
        return self.head == None

if __name__ == "__main__":
    doubly_list = doublelinkedlist()
    
    # 데이터 추가 테스트
    doubly_list.append(1)
    doubly_list.append(2)
    doubly_list.append(3)
    print("초기 양방향 연결 리스트:")
    doubly_list.print_all()    # 1 <-> 2 <-> 3
    
    # 중간 삽입 테스트
    doubly_list.insert_at(1, 5)    # 1과 2 사이에 5를 삽입
    print("\n인덱스 1 위치에 5 삽입 후:")
    doubly_list.print_all()    # 1 <-> 5 <-> 2 <-> 3
    
    # 역방향 출력 테스트
    print("\n역방향 출력:")
    doubly_list.print_reverse()    # 3 <-> 2 <-> 5 <-> 1
    
    # 특정 위치의 데이터 읽기 테스트
    value = doubly_list.read_at(2)    # 2
    print(f"\n인덱스 2의 데이터: {value}")    # 2
    
    # 마지막 노드 삭제 테스트
    doubly_list.remove_last()    # 마지막 노드(3) 삭제
    print("\n마지막 데이터 제거 후:")
    doubly_list.print_all()    # 1 <-> 5 <-> 2
    
    # 첫 번째 노드 삭제 테스트
    doubly_list.delete_at(0)    # 첫 번째 노드(1) 삭제
    print("\n인덱스 0의 값 삭제 후:")
    doubly_list.print_all()    # 5 <-> 2
    
    # 앞쪽 삽입 테스트
    doubly_list.prepend(7)    # 리스트의 맨 앞에 7 삽입
    print("\n맨 앞에 7 삽입 후:")
    doubly_list.print_all()    # 7 <-> 5 <-> 2
    
    # 특정 값 검색 테스트
    index = doubly_list.find(5)    # 1
    print(f"\n값 5의 인덱스: {index}")    # 1
    
    # 모든 노드 삭제 테스트
    doubly_list.clear()    # 모든 노드 삭제
    print("\n모든 노드 삭제 후:")
    doubly_list.print_all()    # 리스트가 비어있습니다
    
    # 빈 리스트 확인 테스트
    is_empty = doubly_list.is_empty()    # True
    print(f"\n리스트가 비어있나요? {is_empty}")    # True
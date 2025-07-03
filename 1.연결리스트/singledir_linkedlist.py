class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singledirlinkedlist:
    def __init__(self):
        self.head = None # 첫번째 노드 (첫 번째 노드만 알면 됨)
        self.size = 0 # 노드의 개수
    
    def print_all(self): # 모든 노드의 데이터 출력
        if self.head is None: # 가장 마지막 노드의 next값일 경우
            return
        
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    
    def clear(self): # 모든 데이터 제거
        self.head = None
        self.size = 0
    
    def insert_at(self, index, data):  # 값의 삽입(인덱스 기반)
        if index < 0 or index > self.size:
            return
        
        new_node = Node(data)
        
        if index == 0:  # 맨 앞에 삽입
            curr = self.head
            self.head = new_node
            self.head.next = curr
            return
        
        else:
            current = self.head
            for _ in range(index - 1): 
                current = current.next # 특정 인덱스값으로 한방에 접근할 순 없음. head값을 타고 타고 순차적으로 접근해야함
            # for문 이후 current값: 새로 추가할 노드 이전의 노드 객체
            new_node.next = current.next
            current.next = new_node
        self.size += 1
    
    def delete_at(self, index): # 값의 삭제(인덱스 기반)
        if self.head is None: # 연결리스트에 노드가 아예 없을 경우
            return
        
        if index == 0:  
            removed_data = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            removed_data = current.next.data
            current.next = current.next.next
        
        self.size -= 1
        return removed_data
    
    def append(self, data): # 연결리스트의 끝단에 데이터 삽입
        self.insert_at(self.size, data)
    
    def remove_last(self): # 연결리스트 맨 마지막 노드 제거
            return self.delete_at(self.size - 1)
    
    def read_at(self, index): # 특정 인덱스에 대한 데이터 읽기
        if self.head is None or index < 0 or index >= self.size:
            return None
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.data

# 테스트 코드
if __name__ == "__main__":
    linked_list = singledirlinkedlist()
    
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    
    print("초기 연결 리스트:")
    linked_list.print_all()
    
    linked_list.insert_at(1, 5)
    print("인덱스 1 위치에 5 삽입 후:")
    linked_list.print_all()
    
    print(f"인덱스 2의 데이터: {linked_list.read_at(2)}")
    
    linked_list.remove_last()
    print("마지막 데이터 제거 후:")
    linked_list.print_all()
    
    linked_list.delete_at(0)
    print("인덱스 0의 값 삭제 후:")
    linked_list.print_all()
    
    linked_list.clear()
    linked_list.print_all()
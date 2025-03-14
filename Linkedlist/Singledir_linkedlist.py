class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None # 첫번째 노드 (첫 번째 노드만 알면 됨)
        self.size = 0 # 노드의 개수
    
    # 1. 모든 데이터를 출력
    def print_all(self):
        if self.head is None:
            print("연결 리스트가 비어 있습니다.")
            return
        
        current = self.head 
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    
    # 2. 모든 데이터를 제거
    def clear(self):
        self.head = None
        self.size = 0
        print("모든 데이터가 제거되었습니다.")
    
    # 3. 인덱스 기반으로 값을 삽입한다
    def insert_at(self, index, data):
        if index < 0 or index > self.size:
            print(f"유효하지 않은 인덱스입니다. 현재 크기: {self.size}")
            return
        
        new_node = Node(data)
        
        if index == 0:  # 맨 앞에 삽입
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        
        self.size += 1
        print(f"인덱스 {index}에 {data} 삽입 완료")
    
    # 4. 인덱스 기반으로 값을 삭제
    def delete_at(self, index):
        if self.head is None:
            print("연결 리스트가 비어 있습니다.")
            return
        
        if index < 0 or index >= self.size:
            print(f"유효하지 않은 인덱스입니다. 현재 크기: {self.size}")
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
        print(f"인덱스 {index}의 값 {removed_data} 삭제 완료")
        return removed_data
    
    # 5. 연결리스트 마지막 부분에 값을 삽입
    def append(self, data):
        self.insert_at(self.size, data)
    
    # 6. 연결리스트 마지막 부분에 있는 값을 제거
    def remove_last(self):
        if self.size > 0:
            return self.delete_at(self.size - 1)
        else:
            print("연결 리스트가 비어 있습니다.")
            return None
    
    # 7. 인덱스를 기반으로 특정 인덱스의 데이터를 읽기
    def read_at(self, index):
        if self.head is None:
            print("연결 리스트가 비어 있습니다.")
            return None
        
        if index < 0 or index >= self.size:
            print(f"유효하지 않은 인덱스입니다. 현재 크기: {self.size}")
            return None
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.data

# 테스트 코드
if __name__ == "__main__":
    linked_list = LinkedList()
    
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    
    print("초기 연결 리스트:")
    linked_list.print_all()
    
    linked_list.insert_at(1, 5)
    print("인덱스 1 위치에 5 삽입 후:")
    linked_list.print_all()
    
    print(f"인덱스 2의 데이터: {linked_list.get_at(2)}")
    
    linked_list.remove_last()
    print("마지막 데이터 제거 후:")
    linked_list.print_all()
    
    linked_list.delete_at(0)
    print("인덱스 0의 값 삭제 후:")
    linked_list.print_all()
    
    linked_list.clear()
    linked_list.print_all()
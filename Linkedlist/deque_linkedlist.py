from doubledir_linkedlist import doublelinkedlist

class Deque:
    def __init__(self):
        self.dll = doublelinkedlist()
        
    def push_front(self, data):
        """덱의 앞쪽에 데이터 추가"""
        self.dll.prepend(data)
        
    def push_back(self, data):
        """덱의 뒤쪽에 데이터 추가"""
        self.dll.append(data)
        
    def pop_front(self):
        """덱의 앞쪽에서 데이터 제거 및 반환"""
        if self.is_empty():
            return None
        return self.dll.delete_at(0)
        
    def pop_back(self):
        """덱의 뒤쪽에서 데이터 제거 및 반환"""
        if self.is_empty():
            return None
        return self.dll.remove_last()
        
    def peek_front(self):
        """덱의 앞쪽 데이터 조회"""
        if self.is_empty():
            return None
        return self.dll.read_at(0)
        
    def peek_back(self):
        """덱의 뒤쪽 데이터 조회"""
        if self.is_empty():
            return None
        return self.dll.tail.data
        
    def is_empty(self):
        """덱이 비어있는지 확인"""
        return self.dll.is_empty()
        
    def size(self): # 유일하게 O(n)의 시간복잡도를 가짐
        """덱의 크기 반환"""
        count = 0
        curr = self.dll.head
        while curr:
            count += 1
            curr = curr.next
        return count
    
    def clear(self):
        """덱의 모든 데이터 삭제"""
        self.dll.clear()
        
    def print_deque(self):
        """덱의 모든 데이터 출력"""
        self.dll.print_all()

if __name__ == "__main__":
    # 테스트 코드
    deque = Deque()
    
    # 데이터 추가 테스트
    print("데이터 추가 테스트")
    deque.push_back(1)    # 뒤쪽에 추가
    deque.push_back(2)
    deque.push_front(0)    # 앞쪽에 추가
    deque.print_deque()    # 예상 출력: 0 <-> 1 <-> 2
    
    # 데이터 삭제 테스트
    print("\n데이터 삭제 테스트")
    print(f"앞쪽에서 제거한 데이터: {deque.pop_front()}")    # 0
    print(f"뒤쪽에서 제거한 데이터: {deque.pop_back()}")    # 2
    deque.print_deque()    # 예상 출력: 1
    
    # 데이터 확인 테스트
    print("\n데이터 확인 테스트")
    deque.push_back(3)
    print(f"앞쪽 데이터: {deque.peek_front()}")    # 1
    print(f"뒤쪽 데이터: {deque.peek_back()}")    # 3
    
    # 크기 확인 테스트
    print(f"\n덱의 크기: {deque.size()}")    # 2
    
    # 비우기 테스트
    print("\n덱 비우기 테스트")
    deque.clear()
    print(f"덱이 비어있나요? {deque.is_empty()}")    # True

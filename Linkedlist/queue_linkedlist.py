from doubledir_linkedlist import doublelinkedlist

class Queue:
    def __init__(self):
        self.dll = doublelinkedlist()
        
    def enqueue(self, data):
        """큐의 뒤쪽에 데이터 추가"""
        self.dll.append(data)
        
    def dequeue(self):
        """큐의 앞쪽에서 데이터 제거 및 반환"""
        if self.is_empty():
            return None
        return self.dll.delete_at(0)
        
    def peek(self):
        """큐의 맨 앞 데이터 조회"""
        if self.is_empty():
            return None
        return self.dll.read_at(0)
        
    def is_empty(self):
        """큐가 비어있는지 확인"""
        return self.dll.is_empty()
        
    def size(self):
        """큐의 크기 반환"""
        count = 0
        curr = self.dll.head
        while curr:
            count += 1
            curr = curr.next
        return count
    
    def clear(self):
        """큐의 모든 데이터 삭제"""
        self.dll.clear()
        
    def print_queue(self):
        """큐의 모든 데이터 출력"""
        self.dll.print_all()

if __name__ == "__main__":
    # 테스트 코드
    queue = Queue()
    
    # 데이터 추가 테스트
    print("데이터 추가 테스트")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print_queue()    # 예상 출력: 1 <-> 2 <-> 3
    
    # 데이터 삭제 테스트
    print("\n데이터 삭제 테스트")
    print(f"제거된 데이터: {queue.dequeue()}")    # 1
    queue.print_queue()    # 예상 출력: 2 <-> 3
    
    # 맨 앞 데이터 확인 테스트
    print("\n맨 앞 데이터 확인 테스트")
    print(f"맨 앞 데이터: {queue.peek()}")    # 2
    
    # 크기 확인 테스트
    print(f"\n큐의 크기: {queue.size()}")    # 2
    
    # 비우기 테스트
    print("\n큐 비우기 테스트")
    queue.clear()
    print(f"큐가 비어있나요? {queue.is_empty()}")    # True
    
    # 빈 큐에서 데이터 제거 시도
    print("\n빈 큐에서 데이터 제거 시도")
    print(f"제거된 데이터: {queue.dequeue()}")    # None

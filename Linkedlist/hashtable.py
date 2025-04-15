from doubledir_linkedlist import doublelinkedlist

class HashData:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
class HashTable:
    def __init__(self):
        """해시 테이블은 10개의 공간을 할당하고, 각 공간의 요소들은 연결리스트로 연결됩니다."""
        self.arr = [doublelinkedlist() for _ in range(10)] # 각 인덱스(key)에 대해 데이터를 저장할 공간 생성
        
    def _hash_function(self, key): # 아주 단순한 해시함수를 가정하자
        """간단히 key값을 10으로 나눈 값을 반환하는 해시 함수를 정의합니다."""
        return key%10  
    
    def _set(self, key, value):
        """
        데이터를 삽입합니다. 
        예를 들어 HashTable._set(20, "홍길동")이라고 하면, 다음과 같습니다.
        self.arr[0(20%10)].insert_at(0, HashData(20, "홍길동"))
        insert_at은 각각 인덱스값과 데이터를 인자로 받습니다.
        """
        self.arr[self._hash_function(key)].insert_at(0, HashData(key, value))
    
    def _get(self, key):
        """
        key값을 인자로 받아, 해당 key값을 갖는 value를 조회합니다.
        예를 들어 HashTable._get(20)이라고 하면, 20의 key값을 갖는 연결리스트의 노드를 순차적으로 탐색하여 대상을 찾아냅니다.
        """
        curr = self.arr[self._hash_function(key)].head
        while curr!=None:
            if curr.data.key == key:
                return curr.data.value
            curr = curr.next # 일치하지 않을 경우 다음 노드로 이동하기
        return None # 다 읽어봤는데 일치하는 데이터가 없을 경우
    
    def _remove(self, key):
        """
        해당 key값을 갖는 리스트의 인덱스를 반환하여, 해당 인덱스의 연결리스트를 순차적으로 탐색합니다.
        탐색 후 해당 key값에 해당하는 데이터를 인덱스 기반으로 제거합니다.
        """
        lst = self.arr[self._hash_function(key)] # 해당 key값을 갖는 부분의 연결리스트
        curr = lst.head
        deleted_idx = 0
        while(curr != None):
            if curr.data.key == key:
                return lst.delete_at(deleted_idx)
            curr = curr.next
            deleted_idx += 1
        return None # 일치하는 데이터가 없을 경우

if __name__ == "__main__":
    
    hash_table = HashTable()
    # 값 추가
    hash_table._set(1, "이운재")
    hash_table._set(4, "최진철")
    hash_table._set(20, "홍명보")
    hash_table._set(6, "유상철")
    hash_table._set(22, "송종국")
    hash_table._set(21, "레전드")
    hash_table._set(5, "김남일")
    hash_table._set(10, "이영표")
    hash_table._set(8, "최태욱")
    hash_table._set(9, "설기현")
    hash_table._set(14, "이천수")

    # 출력
    print(f"1: {hash_table._get(1)}") # 이운재
    hash_table._remove(1)  # 항목 제거
    print(f"1: {hash_table._get(1)}") # None
    print(f"21: {hash_table._get(21)}")
        
    # print(hash_table._set.__doc__)
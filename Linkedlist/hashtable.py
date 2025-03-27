from doubledir_linkedlist import doublelinkedlist

class hashdata:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
class hashtable:
    def __init__(self):
        self.arr = [doublelinkedlist() for _ in range(10)] # 각 인덱스(key)에 대해 데이터를 저장할 공간 생성
        
    def hash_function(self, key): # 아주 단순한 해시함수를 가정하자
        return key%10  
    
    def set(self, key, value):
        self.arr[self.hash_function(key)].insert_at(0, hashdata(key, value))
        # e.g. key=20 -> self.arr[0].insert_at(0, hashdata(20, value))
    
    def get(self, key):
        curr = self.arr[self.hash_function(key)].head
        while curr!=None:
            if curr.data.key == key:
                return curr.data.value
            curr = curr.next # 일치하지 않을 경우 다음 노드로 이동하기
        return None # 다 읽어봤는데 일치하는 데이터가 없을 경우
    
    def remove(self, key):
        lst = self.arr[self.hash_function(key)]
        curr = lst.head
        deleted_idx = 0
        while(curr != None):
            if curr.data.key == key:
                return lst.delete_at(deleted_idx)
            curr = curr.next
            deleted_idx += 1
        return None # 일치하는 데이터가 없을 경우

if __name__ == "__main__":
    hash_table = hashtable()
    # 값 추가
    hash_table.set(1, "이운재")
    hash_table.set(4, "최진철")
    hash_table.set(20, "홍명보")
    hash_table.set(6, "유상철")
    hash_table.set(22, "송종국")
    hash_table.set(21, "레전드")
    hash_table.set(5, "김남일")
    hash_table.set(10, "이영표")
    hash_table.set(8, "최태욱")
    hash_table.set(9, "설기현")
    hash_table.set(14, "이천수")

    # 출력
    print(f"1: {hash_table.get(1)}") # 이운재
    hash_table.remove(1)  # 항목 제거
    print(f"1: {hash_table.get(1)}") # None
    print(f"21: {hash_table.get(21)}")
        

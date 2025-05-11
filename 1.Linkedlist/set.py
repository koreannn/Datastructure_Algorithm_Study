from hashtable import hashtable

class hashset:
    def __init__(self):
        self.hash_table = hashtable()
    
    def add(self, key):
        if self.hash_table.get(key) == None:
            self.hash_table.set(key, True)
    
    def contains(self, key):
        return self.hash_table.get(key) != None
    
    def remove(self, key):
        self.hash_table.remove(key)
    
    def clear(self):
        for i in range(len(self.hash_table.arr)):
            self.hash_table.arr[i].clear()
    
    def is_empty(self):
        is_empty = True
        for i in range(len(self.hash_table.arr)):
            if self.hash_table.arr[i].head != None:
                is_empty = False
                break
        return is_empty
    
    def print_all(self):
        for i in range(len(self.hash_table.arr)):
            if self.hash_table.arr[i].head is not None:
                print(f"Bucket {i}:", end=" ")
                self.hash_table.arr[i].print_all()
            else:
                print(f"Bucket {i}: Empty")

if __name__ == "__main__":
    hash_set = hashset()
    
    print(f"isEmpty: {hash_set.is_empty()}")
    print(f"=====데이터 삽입=====") 
    hash_set.add(1)
    hash_set.add(2)
    hash_set.add(3)
    hash_set.add(4)
    hash_set.add(5)
    hash_set.print_all()
    print(f"isEmpty: {hash_set.is_empty()}")
    
    print("===== 데이터 체크 =====")
    print(f"1: {hash_set.contains(1)}")
    print(f"2: {hash_set.contains(2)}")
    
    print(f"=====데이터 삭제=====")
    hash_set.remove(1)
    hash_set.remove(2)
    hash_set.print_all()
    print(f"isEmpty: {hash_set.is_empty()}")
    
    print(f"=====데이터 체크 2=====")
    print(f"1: {hash_set.contains(1)}")
    
    print(f"===== Clear =====")
    hash_set.clear()
    hash_set.print_all()
    print(f"isEmpty: {hash_set.is_empty()}")
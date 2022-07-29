class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_slots()
  
    def create_slots(self):
        return [[] for _ in range(self.size)]
  
    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        slot = self.hash_table[hashed_key]
        found_key = False
        for index, item in enumerate(slot):
            item_key = item[0]
            if item_key == key:
                found_key = True
                break
        if found_key:
            slot[index] = (key, val)
        else:
            slot.append((key, val))
  
    # Return searched value with specific key:
    def get_val(self, key):
        hashed_key = hash(key) % self.size
        slot = self.hash_table[hashed_key]
        found_key = False
        for index, item in enumerate(slot):
            item_key, item_val = item
            if item_key == key:
                found_key = True
                break
  
        if found_key:
            return item_val
        else:
            return "No record found"
  
    def delete_val(self, key):
        
        hashed_key = hash(key) % self.size
        slot = self.hash_table[hashed_key]
        found_key = False
        for index, item in enumerate(slot):
            item_key  = item[0]
              
            if item_key == key:
                found_key = True
                break
        if found_key:
            slot.pop(index)
        return

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
  
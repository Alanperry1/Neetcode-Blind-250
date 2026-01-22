from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        # Time Complexity: O(1) - initialization
        # Space Complexity: O(capacity) - OrderedDict can store up to capacity items
        self.capacity=capacity
        self.cache=OrderedDict()

    def get(self, key: int) -> int:
        # Time Complexity: O(1) - OrderedDict operations are O(1)
        # Space Complexity: O(1) - no additional space used
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # Time Complexity: O(1) - OrderedDict operations are O(1)
        # Space Complexity: O(1) - no additional space used
        if key in self.cache:
            self.cache.move_to_end(key)        
        self.cache[key]=value
        if len(self.cache)>self.capacity:
            self.cache.popitem(last=False)

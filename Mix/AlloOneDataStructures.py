"""
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.
Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
"""
class AllOne:

    def __init__(self):
        self.key_count = {}
        self.count_keys = {}
        self.min_count = None
        self.max_count = None
        
    def inc(self, key: str) -> None:
        if key in self.key_count:
            old_count = self.key_count[key]
            new_count = old_count + 1
            self.key_count[key] = new_count
            
            self.count_keys[old_count].remove(key)
            if not self.count_keys[old_count]:
                del self.count_keys[old_count]
                if self.min_count == old_count:
                    self.min_count += 1
            
            if new_count not in self.count_keys:
                self.count_keys[new_count] = set()
            self.count_keys[new_count].add(key)
            
            if self.max_count is None or new_count > self.max_count:
                self.max_count = new_count
        else:
            self.key_count[key] = 1
            if 1 not in self.count_keys:
                self.count_keys[1] = set()
            self.count_keys[1].add(key)
            
            if self.min_count is None or self.min_count > 1:
                self.min_count = 1
            if self.max_count is None:
                self.max_count = 1
        
    def dec(self, key: str) -> None:
        if key in self.key_count:
            old_count = self.key_count[key]
            new_count = old_count - 1
            
            self.count_keys[old_count].remove(key)
            if not self.count_keys[old_count]:
                del self.count_keys[old_count]
                if self.max_count == old_count:
                    self.max_count -= 1
                if self.min_count == old_count:
                    self.min_count = new_count if new_count > 0 else None
            
            if new_count > 0:
                self.key_count[key] = new_count
                if new_count not in self.count_keys:
                    self.count_keys[new_count] = set()
                self.count_keys[new_count].add(key)
                
                if self.min_count is None or new_count < self.min_count:
                    self.min_count = new_count
            else:
                del self.key_count[key]
                if not self.key_count:
                    self.min_count = None
                    self.max_count = None

    def getMaxKey(self) -> str:
        if self.max_count is None:
            return ""
        return next(iter(self.count_keys[self.max_count]))
        
    def getMinKey(self) -> str:
        if self.min_count is None:
            return ""
        return next(iter(self.count_keys[self.min_count]))
        
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
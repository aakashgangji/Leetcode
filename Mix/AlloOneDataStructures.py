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
class ListNode:
    def __init__(self, frequency):
        self.freq = frequency
        self.previous = None
        self.next = None
        self.items = set()
    
    
class AllOne:
    def __init__(self):
        self.start = ListNode(0)  # Starting dummy node
        self.end = ListNode(0)  # Ending dummy node
        self.start.next = self.end  # Connect start to end
        self.end.previous = self.start  # Connect end to start
        self.lookup = {}  # Store item-node association
    
    def inc(self, item: str) -> None:
        if item in self.lookup:
            current = self.lookup[item]
            current_freq = current.freq
            current.items.remove(item)
    
            next_node = current.next
            if next_node == self.end or next_node.freq != current_freq + 1:
                new_node = ListNode(current_freq + 1)
                new_node.items.add(item)
                new_node.previous = current
                new_node.next = next_node
                current.next = new_node
                next_node.previous = new_node
                self.lookup[item] = new_node
            else:
                next_node.items.add(item)
                self.lookup[item] = next_node
                
            if not current.items:
                self.deleteNode(current)
        else:
            first_node = self.start.next
            if first_node == self.end or first_node.freq > 1:
                new_node = ListNode(1)
                new_node.items.add(item)
                new_node.previous = self.start
                new_node.next = first_node
                self.start.next = new_node
                first_node.previous = new_node
                self.lookup[item] = new_node
            else:
                first_node.items.add(item)
                self.lookup[item] = first_node
    
    def dec(self, item: str) -> None:
        if item not in self.lookup:
            return
    
        current = self.lookup[item]
        current.items.remove(item)
        current_freq = current.freq
    
        if current_freq == 1:
            del self.lookup[item]
        else:
            previous_node = current.previous
            if previous_node == self.start or previous_node.freq != current_freq - 1:
                new_node = ListNode(current_freq - 1)
                new_node.items.add(item)
                new_node.previous = previous_node
                new_node.next = current
                previous_node.next = new_node
                current.previous = new_node
                self.lookup[item] = new_node
            else:
                previous_node.items.add(item)
                self.lookup[item] = previous_node
    
        if not current.items:
            self.deleteNode(current)
    
    def getMaxKey(self) -> str:
        if self.end.previous == self.start:
            return ""
        return next(iter(self.end.previous.items))
    
    def getMinKey(self) -> str:
        if self.start.next == self.end:
            return ""
        return next(iter(self.start.next.items))
    
    def deleteNode(self, node):
        prev_node = node.previous
        next_node = node.next
        prev_node.next = next_node
        next_node.previous = prev_node
        
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
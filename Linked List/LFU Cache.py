"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
"""
class Node:  
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.freq = 1  
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

class DoublyLinkedList:  
    def __init__(self) -> None:
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_first(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node: Node) -> Node:
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = None
        return node

    def remove_last(self) -> Node:
        return self.remove(self.tail.prev)

    def is_empty(self) -> bool:
        return self.head.next == self.tail


class LFUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.min_freq = 0  
        self.node_map: dict[int, Node] = {} 
        self.freq_map: defaultdict[int, DoublyLinkedList] = defaultdict(DoublyLinkedList) 

    def get(self, key: int) -> int:
        if self.capacity == 0 or key not in self.node_map:
            return -1
        node = self.node_map[key]
        self._increment_frequency(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self._increment_frequency(node)
            return

        if len(self.node_map) == self.capacity:
            freq_list = self.freq_map[self.min_freq]
            evicted_node = freq_list.remove_last()
            del self.node_map[evicted_node.key]
        node = Node(key, value)
        self._add_node(node)
        self.node_map[key] = node
        self.min_freq = 1

    def _increment_frequency(self, node: Node) -> None:
        freq = node.freq
        freq_list = self.freq_map[freq]
        freq_list.remove(node)
        if freq_list.is_empty():
            del self.freq_map[freq]
            if freq == self.min_freq:
                self.min_freq += 1
        node.freq += 1
        self._add_node(node)

    def _add_node(self, node: Node) -> None:
        freq = node.freq
        freq_list = self.freq_map[freq]
        freq_list.add_first(node)
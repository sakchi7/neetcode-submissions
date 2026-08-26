class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        node.prev = self.head
        temp.prev = node

    def _remove(self, node):
        prevn = node.prev
        temp = node.next
        prevn.next = temp
        temp.prev = prevn

    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        node = self.lru[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node = self.lru[key]
            self._remove(node)
            self.lru.pop(key)
        if len(self.lru)>=self.cap:
            rem = self.tail.prev
            self._remove(rem)
            self.lru.pop(rem.key)
        nd = Node(key, value)
        self._add(nd)
        self.lru[key] = nd
        

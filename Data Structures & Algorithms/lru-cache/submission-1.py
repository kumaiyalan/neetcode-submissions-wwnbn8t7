class ListNode:
     def __init__(self, key, val, nxt, prev):
         self.key, self.val = key, val
         self.nxt, self.prev = nxt, prev

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.contains = {}
        self.left = ListNode("DummyLKey", "DummyLVal", None, None)
        self.right = ListNode("DummyRKey", "DummyRVal", None, None)
        self.left.nxt = self.right
        self.right.prev = self.left

    def insert(self, node):
        currLatest = self.right.prev
        currLatest.nxt = node
        self.right.prev = node
        node.nxt = self.right
        node.prev = currLatest
    
    def remove(self, node):
        prevNode = node.prev
        nxtNode = node.nxt
        prevNode.nxt = nxtNode
        nxtNode.prev = prevNode

    def get(self, key: int) -> int:
        if key in self.contains:
            self.remove(self.contains[key])
            self.insert(self.contains[key])
            return self.contains[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.contains:
            self.remove(self.contains[key])
            self.insert(self.contains[key])
            self.contains[key].val = value
        else:
            if len(self.contains) < self.size:
                nn = ListNode(key, value, None, None)
                self.contains[key] = nn
                self.insert(nn)
            else:
                rn = self.left.nxt
                self.remove(rn)
                self.contains.pop(rn.key)
                nn = ListNode(key, value, None, None)
                self.contains[key] = nn
                self.insert(nn)

        

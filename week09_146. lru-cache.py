class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def move_node_to_tail(self, key):
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_node_to_tail(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            new = ListNode(key, value)
            self.hashmap[key] = new
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new


if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # 缓存是{1 = 1}
    lRUCache.put(2, 2)  # 缓存是{1 = 1, 2 = 2}
    print(lRUCache.get(1))  # 返回1
    lRUCache.put(3, 3)  # 该操作会使得关键字2作废，缓存是{1 = 1, 3 = 3}
    print(lRUCache.get(2))  # 返回 - 1(未找到)
    lRUCache.put(4, 4)  # 该操作会使得关键字1作废，缓存是{4 = 4, 3 = 3}
    print(lRUCache.get(1))  # 返回 - 1(未找到)
    print(lRUCache.get(3))  # 返回3
    print(lRUCache.get(4))  # 返回4

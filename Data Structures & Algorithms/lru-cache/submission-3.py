class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.queue = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.queue:
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.queue) >= self.capacity:
            del self.cache[self.queue.popleft()]
        
        if key in self.cache:
            self.queue.remove(key)

        self.cache[key] = value
        self.queue.append(key)

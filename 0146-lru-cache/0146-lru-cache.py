class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []
        self.recent_dict  = dict()

    def get(self, key: int) -> int:
        if key in self.recent_dict:
            value = self.recent_dict[key]
            self.cache.remove((key,value))
            self.cache.append((key,value))

            return value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.recent_dict:
            temp = self.recent_dict[key]
            self.cache.remove((key,temp))
            self.cache.append((key,value))
            self.recent_dict[key] = value
            return
        elif len(self.cache) == self.capacity:
            temp = self.cache[0]
            self.cache.pop(0)
            self.recent_dict.pop(temp[0])
            self.cache.append((key,value))
            self.recent_dict[key] = value
        else:
            self.cache.append((key,value))
            self.recent_dict[key] = value
        
        
# class LRUCache:
#     def __init__(self,capacity):
#         self.capacity = capacity
#         self.cache = []
#     def get(self,key):
#         for i in range(len(self.cache)):
#             if self.cache[i][0] == key:
#                 val = self.cache[i][1]
#                 temp = self.cache[i]
#                 self.cache.pop(i)
#                 self.cache.append(temp)
#                 return val
#         return -1
#     def put(self,key,value):
#         for i in range(len(self.cache)):
#             if self.cache[i][0] == key:
#                 self.cache.pop(i)
#                 self.cache.append((key,value))
#                 return
#         if len(self.cache) == self.capacity:
#             self.cache.pop(0)
#             self.cache.append((key,value))
#         else:
#             self.cache.append((key,value))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
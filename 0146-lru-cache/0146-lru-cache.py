
# # better approach : t.c. = O(n) and s.c. = O(capacity)
# class LRUCache:
    
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = []
#         self.recent_dict  = dict()
    


#     def get(self, key: int) -> int:
#         if key in self.recent_dict:
#             value = self.recent_dict[key]
#             self.cache.remove((key,value))
#             self.cache.append((key,value))

#             return value
#         return -1
        

#     def put(self, key: int, value: int) -> None:
#         if key in self.recent_dict:
#             temp = self.recent_dict[key]
#             self.cache.remove((key,temp))
#             self.cache.append((key,value))
#             self.recent_dict[key] = value
#             return
#         elif len(self.cache) == self.capacity:
#             temp = self.cache[0]
#             self.cache.pop(0)
#             self.recent_dict.pop(temp[0])
#             self.cache.append((key,value))
#             self.recent_dict[key] = value
#         else:
#             self.cache.append((key,value))
#             self.recent_dict[key] = value
        
        


 # brute force approach : t.c. = O(n^2) and s.c. = O(capacity)  
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




# Optimal solution : t.c. = O(1) and s.c. = O(capacity)



class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)
        
        self.left.next = self.right
        self.right.prev = self.left
    
    # Remove a node from DLL
    def remove(self,node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert a node at MRU side
    def insert(self,node):
        last = self.right.prev

        last.next = node
        node.prev = last

        node.next = self.right
        self.right.prev = node


    # Get value
    def get(self,key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.value

    # Insert/Update value
    def put(self,key,value):

        # key already existes
        if key in self.cache:
            node = self.cache[key]

            #update value
            node.value = value

            # Move to MRU
            self.remove(node)
            self.insert(node)
        
        # Key does not exist
        else:
            node = Node(key,value)

            # Add to dictionary
            self.cache[key] = node

            # Add to MRU position
            self.insert(node)
        
        # Cache is full
        if len(self.cache) > self.capacity:

            # First node after left = LRU
            lru = self.left.next

            # Remove from DLL
            self.remove(lru)

            # Remove from DLL
            del self.cache[lru.key]







# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
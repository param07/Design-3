## Problem 2: LRU Cache(https://leetcode.com/problems/lru-cache/)

# Method-1: LRU Cache with LinkedListNode defined outside LRUCache class
# Time Complexity : O(1) -- get(), O(1) -- put()
# Space Complexity : O(capacity)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# In LRU cache, whenever get() or put() operation happens that node becomes the Most Recently used node. Also if the capacity of cache is full, and 
# we do a put() operation for a node that already does not exist, the least recent used node is removed from the cache and we add the latest node
# to the most recently used side. So we need to maintain order of the nodes in terms of its addition and usage. We cannot use array here as we
# remove node from one and add node from another. So either one of the operation could be expensive. To overcome this we can use LinkedList. But
# when updating an existing node or getting value of a node, we need to remove the node from its current position and add to the most recently used
# side. So this removal operation could be expensive if using LinkedList. Doubly LinkedList helps to overcome this issue as well. For get() operation to 
# be efficient we use a hashmap, where we store key as key of node and value as node itself. Here we are maintaining the least recently used side 
# towards the head and most recently used side towards the tail of the doubly linkedlist.


class LinkedListNode(object):
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = LinkedListNode(-1, -1) # least recently used
        self.tail = LinkedListNode(-1, -1) # most recently used
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lruMap = {}
        self.maxCapacity = capacity
        # self.currCapacity = 0

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def addNodeToLast(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key): # O(1)
        """
        :type key: int
        :rtype: int
        """
        if(key not in self.lruMap):
            return -1

        # get the node
        node = self.lruMap[key]
        # get the value to be returned
        value = node.val
        # remove the node from current position
        self.removeNode(node)
        # put the node to most recent used
        self.addNodeToLast(node)

        return value
        

    def put(self, key, value): # O(1)
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if(key in self.lruMap):
            # update the value for the key
            node = self.lruMap[key]
            node.val = value
            # remove the node from current position
            self.removeNode(node)
            # put the node to most recent used
            self.addNodeToLast(node)
        else:
            # it is a new node
            newNode = LinkedListNode(key, value)
            # check capacity first
            if(self.maxCapacity == len(self.lruMap)):
                # capacity is full
                # remove the least recently used
                leastRecentUsedNode = self.head.next
                # remove the node
                self.removeNode(leastRecentUsedNode)
                # remove from map
                self.lruMap.pop(leastRecentUsedNode.key)
            # else:
            #     self.currCapacity += 1

            # add to the map
            self.lruMap[key] = newNode
            # put the node to most recent used
            self.addNodeToLast(newNode)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
print("Method-1: LRU Cache with LinkedListNode defined outside LRUCache class")
lruCache = LRUCache(5)
lruCache.put(1,1)
lruCache.put(2,2)
lruCache.put(3,3)
lruCache.put(4,4)
lruCache.put(5,5)
print(lruCache.get(1))
lruCache.put(6,6)
print(lruCache.get(2))
lruCache.put(3,20)
lruCache.put(7,7)
print(lruCache.get(4))
print(lruCache.get(3))






# Method-2: LRU Cache with LinkedListNode defined inside the LRUCache class
# Time Complexity : O(1) -- get(), O(1) -- put()
# Space Complexity : O(capacity)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# In LRU cache, whenever get() or put() operation happens that node becomes the Most Recently used node. Also if the capacity of cache is full, and 
# we do a put() operation for a node that already does not exist, the least recent used node is removed from the cache and we add the latest node
# to the most recently used side. So we need to maintain order of the nodes in terms of its addition and usage. We cannot use array here as we
# remove node from one and add node from another. So either one of the operation could be expensive. To overcome this we can use LinkedList. But
# when updating an existing node or getting value of a node, we need to remove the node from its current position and add to the most recently used
# side. So this removal operation could be expensive if using LinkedList. Doubly LinkedList helps to overcome this issue as well. For get() operation to 
# be efficient we use a hashmap, where we store key as key of node and value as node itself. Here we are maintaining the least recently used side 
# towards the head and most recently used side towards the tail of the doubly linkedlist.




class LRUCache(object):

    class LinkedListNode(object):
        def __init__(self, key, val):
            self.next = None
            self.prev = None
            self.key = key
            self.val = val

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = LinkedListNode(-1, -1) # least recently used
        self.tail = LinkedListNode(-1, -1) # most recently used
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lruMap = {}
        self.maxCapacity = capacity
        # self.currCapacity = 0

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def addNodeToLast(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key): # O(1)
        """
        :type key: int
        :rtype: int
        """
        if(key not in self.lruMap):
            return -1

        # get the node
        node = self.lruMap[key]
        # get the value to be returned
        value = node.val
        # remove the node from current position
        self.removeNode(node)
        # put the node to most recent used
        self.addNodeToLast(node)

        return value
        

    def put(self, key, value): # O(1)
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if(key in self.lruMap):
            # update the value for the key
            node = self.lruMap[key]
            node.val = value
            # remove the node from current position
            self.removeNode(node)
            # put the node to most recent used
            self.addNodeToLast(node)
        else:
            # it is a new node
            newNode = LinkedListNode(key, value)
            # check capacity first
            if(self.maxCapacity == len(self.lruMap)):
                # capacity is full
                # remove the least recently used
                leastRecentUsedNode = self.head.next
                # remove the node
                self.removeNode(leastRecentUsedNode)
                # remove from map
                self.lruMap.pop(leastRecentUsedNode.key)
            # else:
            #     self.currCapacity += 1

            # add to the map
            self.lruMap[key] = newNode
            # put the node to most recent used
            self.addNodeToLast(newNode)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
print("Method-2: LRU Cache with LinkedListNode defined inside the LRUCache class")
lruCache = LRUCache(5)
lruCache.put(1,1)
lruCache.put(2,2)
lruCache.put(3,3)
lruCache.put(4,4)
lruCache.put(5,5)
print(lruCache.get(1))
lruCache.put(6,6)
print(lruCache.get(2))
lruCache.put(3,20)
lruCache.put(7,7)
print(lruCache.get(4))
print(lruCache.get(3))


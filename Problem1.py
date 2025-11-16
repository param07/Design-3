## Problem 1: Flatten Nested List Iterator (https://leetcode.com/problems/flatten-nested-list-iterator/)

# Method1: Using original/native iterator to the list of NestedInteger
# Time Complexity : hasNext() -- Amortized O(1), in worst case while loop would be the max depth of the nested lists, next() -- O(1) perfect
# Space Complexity : O(d) where d is the maximum depth of nested lists (stack size)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# We have to implement iterator for NestedInteger class that is NestedIterator. As we have to do controlled recursion, we would be
# using stack for it. But if we only use stack and we have a list as input, we would still need not achieve lazy loading. For our
# NestedIterator to be lazy loading we need a lazy loading data structure, hence we use an original iterator on our nested list of 
# NestedInteger class. We have Next() and HasNext() method for NestedIterator and next() and hasNext() method for original native 
# iterator. However, in python we dont have hasNext() method for iterators. So we are using "next((self.stack)[-1], None)". So 
# This way you can check for None to see if you've reached the end of the iterator otherwise we need to check for StopIteration exception.
# The Next() function of the NestedIterator would return an Integer. So we need to do heavy loading in the HasNext() 
# method. HasNext() is called before Next() always. So HasNext() is the one that would compute our NestedInteger nextEle
# The stack if of type Stack<Iterator<NestedInteger>> -- original iterator. We create an iterator to the initial list and add to the
# stack. We get the next() from the iterator at top of the stack. We store this in our self.nextEle variable, as pointer to 
# the iterator moves to the next element. If the next() exists, then we check if it is an Integer. 
# If it is an Integer, then we return the value of HasNext() as true and the self.nextEle variable would have the NestedInteger.
# If it is not an Integer, then it is List of NestedInteger but of type NestedInteger. Then, we get the list of this NestedInteger
# get an iterator to the list and push to it to the stack.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        if value is None:
            self._integer = None
            self._list = []
        elif isinstance(value, int):
            self._integer = value
            self._list = None
        else:
            raise TypeError("Invalid type for NestedInteger")

    def isInteger(self):
        return self._integer is not None

    def getInteger(self):
        return self._integer

    def getList(self):
        return self._list

    def add(self, elem):
        if self._list is None:
            self._list = []
            self._integer = None
        self._list.append(elem)

    def __repr__(self):
        return f"{self._integer if self.isInteger() else self._list}"

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # stack of type original iterators
        # iterator of type <NestedInteger>
        # Stack<Iterator<NestedInteger>>
        self.stack = [iter(nestedList)]
        # nextEle of type NestedInteger
        # <NestedInteger>
        self.nextEle = None
        
    # next of NestedIterator
    def next(self):#O(1) -- perfect
        """
        :rtype: int
        """
        return (self.nextEle).getInteger()
        
    # hasNext of NestedIterator
    def hasNext(self):# Only upto the depth
        """
        :rtype: bool
        """
        while(self.stack):
            self.nextEle = next((self.stack)[-1], None)
            if(not (self.nextEle)):
                # if the iterator at the top of the stack is completely explored
                # then pop that out
                self.stack.pop()
            else:
                # next element exists for the iterator at the top of the stack
                # NestedInteger
                if((self.nextEle).isInteger()):
                    # if the iterator is not fully explored and if it is an integer
                    # we got an integer, so hasNext would be True
                    return True
                else:
                    # iterator is not fully explored and it is not an integer
                    # means it is a list. This object is of type NestedIntger and 
                    # it is not a list
                    # so we get the list and get its iterator and push it to the stack
                    self.stack.append(iter((self.nextEle).getList()))

        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

inputArr = [[1, 2], 3, [4, [5, 6]]]

def buildNestedInteger(obj):
    """Convert a Python list/int into NestedInteger."""
    if isinstance(obj, int):
        return NestedInteger(obj)

    nested = NestedInteger()
    for item in obj:
        nested.add(buildNestedInteger(item))
    return nested


def makeNestedList(arr):
    """Return List[NestedInteger] for a Python list."""
    return [buildNestedInteger(item) for item in arr]

nestedList = makeNestedList(inputArr)
print(nestedList)

print("Method1: Using original/native iterator to the list of NestedInteger")
nestedIterObject = NestedIterator(nestedList)
print(nestedIterObject.hasNext())
print(nestedIterObject.next())
print(nestedIterObject.hasNext())
print(nestedIterObject.next())
print(nestedIterObject.hasNext())
print(nestedIterObject.next())
print(nestedIterObject.hasNext())
print(nestedIterObject.next())
print(nestedIterObject.hasNext())
print(nestedIterObject.next())
print(nestedIterObject.hasNext())
print(nestedIterObject.next())
print(nestedIterObject.hasNext())



# Method2: Using 2 stacks. Stack1 --- for storing list of type NestedIntegers. Stack2 --- for storing last index of the lists that is current/last pointer to all the NestedInteger Lists currently in the stack1
# Time Complexity : hasNext() -- Amortized O(1), in worst case while loop would be the max depth of the nested lists, next() -- O(1) perfect
# Space Complexity : O(d) where d is the maximum depth of nested lists (stack size)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# Here we are using 2 stacks. Stack1 --- keep track of current working lists of NestedIntegers
# Stack2 to keep track indices of all working lists in stack1. We start with putting the current nestedlist in stack1 and current
# index to that list as 0 in stack2. When we get the element at current index of the current working list, we check if the current
# element of type NestedInteger is an Integer or a list. Also for this current working list we increment the pointer as we have
# processed the current element. We check if current element is an integer, we return true from the hasNext() function.
# If it is not an integer, then we get the list and add this new list to our stack1 and index = 0 to this list in stack2.
# These two stacks help to maintain the lazy loading of the NestedIterator


# Using 2 stacks
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # stack1 to keep track of current working list
        self.listStack = [nestedList]
        # stack2 to keep track indices of all working lists in stack1
        self.indexStack = [0]
        # next element of type NestedInteger
        self.nextEle = None


    def next(self):
        """
        :rtype: int
        """
        return self.nextEle.getInteger()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while(self.listStack):
            if(len(self.listStack[-1]) == self.indexStack[-1]):
                # if index of current working list finishes
                # then pop from the stacks
                self.listStack.pop()
                self.indexStack.pop()
            else:
                currList = self.listStack[-1]
                currIndex = self.indexStack.pop()
                # curr element of type NestedInteger
                # could be an Integer or a list of type NestedInteger
                self.nextEle = currList[currIndex]
                # increase the pointer to the current list
                self.indexStack.append(currIndex + 1)

                # check curr element
                if(self.nextEle.isInteger()):
                    return True
                else:
                    # it is of type NestedInteger but it is a list
                    # so get the list and add to the stack
                    self.listStack.append(self.nextEle.getList())
                    # add pointer to this new list added to the stack
                    self.indexStack.append(0)


        return False
    

print("Method2: Using 2 stacks. Stack1 --- for storing list of type NestedIntegers. Stack2 --- for storing last index of the lists that is current/last pointer to all the NestedInteger Lists currently in the stack1")
nestedIterObject = NestedIterator(nestedList)
print(nestedIterObject.hasNext())
print(nestedIterObject.next())
print(nestedIterObject.hasNext())
print(nestedIterObject.next())
print(nestedIterObject.hasNext())
print(nestedIterObject.next())
print(nestedIterObject.hasNext())
print(nestedIterObject.next())
print(nestedIterObject.hasNext())
print(nestedIterObject.next())
print(nestedIterObject.hasNext())
print(nestedIterObject.next())
print(nestedIterObject.hasNext())
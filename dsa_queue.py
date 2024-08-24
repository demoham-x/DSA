from os import *
from sys import *
from collections import *
from math import *

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self, size):
        # Write your code here
        self.queue_size = size
        self.count = 0
        self.head = None
        self.tail = None
        pass

    # Pushes 'X' in the front of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def pushFront(self, x):
        # Write your code here
        temp = Node(x)
        if self.head == None:#appending when it is empty
            self.head = temp
            self.tail = temp
            self.count += 1
            return True
        if self.queue_size != self.count:#appending when it its not empty
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
            self.count += 1
            return True
        else:
            return False

    # Pushes 'X' in the back of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def pushRear(self, x):
        # Write your code here
        temp = Node(x)
        if self.tail == None:
            self.head = temp
            self.tail = temp
            self.count += 1
            return True
        if self.queue_size != self.count:
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp
            self.count += 1
            return True
        else:
            return False

    # Pops an element from the front of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def popFront(self):
        # Write your code here
        if self.count == 0:
            return -1
        temp_data = self.head.data        
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        del temp
        self.count -= 1
        return temp_data

    # Pops an element from the back of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def popRear(self):
        # Write your code here
        if self.count == 0:
            return -1
        temp_data = self.tail.data        
        temp = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        del temp
        self.count -= 1
        return temp_data

    # Returns the first element of the deque. If the deque is empty, it returns -1.
    def getFront(self):
        # Write your code here
        if self.count == 0:
            return -1
        return self.head.data

    # Returns the last element of the deque. If the deque is empty, it returns -1.
    def getRear(self):
        # Write your code here
        if self.count == 0:
            return -1
        return self.tail.data

    # Returns true if the deque is empty. Otherwise returns false.
    def isEmpty(self):
        # Write your code here
        if self.count == 0:
            return True
        return False

    # Returns true if the deque is full. Otherwise returns false.
    def isFull(self):
        # Write your code here
        if self.queue_size == self.count:
            return True
        return False

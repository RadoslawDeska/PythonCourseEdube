'''
Estimated time

15-30 minutes
Level of difficulty

Easy/Medium
Objectives

    improving the student's skills in defining subclasses;
    adding a new functionality to an existing class.

Scenario

Your task is to slightly extend the Queue class' capabilities. We want it to have a parameterless method that returns True if the queue is empty and False otherwise.

Complete the code we've provided in the editor. Run it to check whether it outputs a similar result to ours.

Expected output

1
dog
False
Queue empty

'''
from collections import deque

class QueueError(IndexError):  # Choose base class for the new exception.
    pass

class Queue:
    def __init__(self):
        # self.queue = []
        # OR
        self.queue = deque()

    def put(self, elem):
        self.queue.append(elem)

    def get(self):
        if not self.queue:
            raise QueueError
        
        first = self.queue[0]
        # self.queue.pop(0)
        # OR
        self.queue.popleft() # IF USING DEQUE
        
        return first
    
class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    
    def isempty(self):
        # if not self.queue:
        #     return True
        # else:
        #     return False
        
        # OR
        return not self.queue

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

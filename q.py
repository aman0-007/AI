class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    
    def peek(self):
        if self.front is None:
            print("Queue is empty!!!")
            return None
        return self.front.data
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.front is None
    
    def enqueue(self,data):
        newNode = Node(data)
        if self.rear is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.size += 1
    
    def dequeue(self):
        if self.front is None:
            print("Queue is empty!!!")
            return
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        
        return removed_data


# queue = Queue()

# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)

# print("Front element:", queue.peek())
# print("Dequeued item:", queue.dequeue())
# print("Front element after dequeue:", queue.peek())
# print("Is the queue empty?", queue.isEmpty())
# print("Queue size:", queue.getSize())
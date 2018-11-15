# Implement a Stack using a queue
class Queue:

  #Constructor creates a list
  def __init__(self):
      self.queue = list()

  #Adding elements to queue
  def enqueue(self, data):
      #Checking to avoid duplicate entry (not mandatory)
      if data not in self.queue:
          self.queue.insert(0, data)
          return True
      return False

  #Removing the last element from the queue
  def dequeue(self):
      if len(self.queue) > 0:
          return self.queue.pop()
      return ("Queue Empty!")

  #Getting the size of the queue
  def size(self):
      return len(self.queue)

  #printing the elements of the queue
  def printQueue(self):
      return self.queue

  def peek(self):
    return self.queue[len(self.queue) - 1]



class Stack:

  #Constructor that creates a queue
  def __init__(self):
    self.stack = Queue()

  #Adding elements to stack
  def push(self, data):
    temp = []
    if self.stack.size() is not 0:
      for i in range(self.stack.size()):
        temp.append(self.stack.dequeue())
      self.stack.enqueue(data)
      for i in range(len(temp)):
        self.stack.enqueue(temp[i])
    else:
      self.stack.enqueue(data)
    print('stack after data pushed = ', self.stack.printQueue())
  
  def pop(self):
    if self.stack.size() is not 0:
      # print('before pop', self.stack.printQueue())
      self.stack.dequeue()
    print('after pop', self.stack.printQueue())
  
  def isEmpty(self):
    if(self.stack.size() is 0):
      print('length is 0, returning True')
      return True
    print('length is not 0, returning False')
    return False

  def top(self):
    if self.stack.size() is not 0:
      print('top of the stack is', self.stack.peek())
      return self.stack.peek()


stack = Stack()
print('Created new stack with items in order: 1 2 3 4 5')
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.isEmpty()
stack.top()

print('popping off items')
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.isEmpty()
stack.top()


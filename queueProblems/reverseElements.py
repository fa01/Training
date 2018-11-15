#Given an integer k and a queue of integers, we need to reverse the order of the first k elements of the queue, 
#leaving the other elements in the same relative order.
from Queue import Queue

def reverseElements(queue, k):
  if queue.size() is not 0:
    temp = []
    for i in range(0, k):
      temp.append(queue.dequeue())
    print('temp = ', temp)
    restElements = []
    for i in range(0, queue.size()):
      restElements.append(queue.dequeue())
    print('restElements', restElements)
    for i in range(0, len(restElements)):
      queue.enqueue(restElements[len(restElements) - i - 1])
    print('Rest Elements added to Queue', queue.printQueue())
    for i in range(0, k):
      queue.enqueue(temp[i])
    print('Queue with reversed items = ', queue.printQueue())

    
  print('Reversed queue =', queue.printQueue())


# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.enqueue(5)
# reverseElements(queue, 2)
    

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)
reverseElements(queue, 4)

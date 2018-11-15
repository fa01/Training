#Given a number n, write a function that generates and prints all binary numbers with decimal values from 1 to n.
from Queue import Queue

def generateBinaryNumbers(n):
  queue = Queue()

  queue.enqueue('1')

  while n > 0:
    value = queue.dequeue()
    print(value)

    queue.enqueue(value + '0')
    queue.enqueue(value + '1')
    n = n - 1

generateBinaryNumbers(10)

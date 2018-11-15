class Node:
  def __init__(self, data = None):
    self.data = data
    self.next = None
  
class SLinkedList:
  def __init__(self):
    self.head = None

  def listprint(self):
    printval = self.head
    while printval is not None:
        print(printval.data)
        printval = printval.next

  def addToBeginning(self, data):
    node = Node(data)
    node.next = self.head
    self.head = node

  def addToEnd(self, data):
    node = Node(data)
    if self.head is None:
      self.head = node
      return
    traversed = self.head
    while traversed.next is not None:
      traversed = traversed.next
    traversed.next = node

  def addInBetween(self, middleNode, data):
    if middleNode is None:
      return
    node = Node(data)
    node.next = middleNode.next
    middleNode.next = node

  def remove(self, data):
    node = self.head

    if node is not None:
      if node.data == data:
        self.head = node.next
        node = None
        return
    
    while node is not None:
      if node.data == data:
        break
      prev = node
      node = node.next
    
    if node == None:
      return
    
    prev.next = node.next
    node = None


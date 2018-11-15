# Reverse a LinkedList

from LinkedList import SLinkedList

def reverseLinkedList(linkedList, node, prev):
  print('node = ', node.data)
  # print('next =', node.next.data)
  if node.next is None:
    linkedList.head = node
    node.next = prev
    return

  nextNode = node.next
  node.next = prev
  prev =  node
  node = nextNode

  return reverseLinkedList(linkedList, node, prev)


list1 = SLinkedList()
list1.addToEnd('Mon')
list1.addToEnd('Tue')
list1.addToEnd("Wed")
reverseLinkedList(list1, list1.head, None)
list1.listprint()

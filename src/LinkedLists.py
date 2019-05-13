"""
Implementing linked lists
"""

class LinkedNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.prev = None


#Create an instance
#Say we want to link 3 nodes with names a->b->c with values 3, 1 and 4

#define 
head = LinkedNode(3)
body = LinkedNode(1)
tail = LinkedNode(4)

#forward links
head.next = body
body.next = tail

#backward links
body.prev = head
tail.prev = body

#a's value
head.val #should be 3
#The value of a's neighbor to the right
head.next.val #should be 1
head.next.next.val #should be 4

tail.val
tail.prev
tail.prev.val
tail.prev.prev.val

#Create a list of nodes for reference by position
linkedList = [head,body,tail]

linkedList[0] #object
linkedList[1].next.val #should be 4
linkedList[len(linkedList)-1].prev
linkedList[len(linkedList)-1].prev.val

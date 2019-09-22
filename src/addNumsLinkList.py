"""
Add two numbers (ints) when each is stored in a linked list with each digit in a node and in reverse order, 
so the unit's place is at the head of the list.
So given input l1 and l2 where each is a head node, output a result that is also the head of a linked list.

Example:
    342
   +265
   ----
    607 

Given input: 'l1' and 'l2' where l1 is head node of a list storing values 2->4->-3 and similarly l2 is head of a list that stores 5->6->2,
the output should be the head l3 of a list with values 7->0->6   

Example:
l1: 2->4->3->9
l2: 5->6->6->3
output: 7->0->0->3->1
"""

class LinkNode:
    def __init__(self,x):
        self.val = x
        self.next = None

#example inputs
l1 = LinkNode(2)
l1.next = LinkNode(4)
l1.next.next = LinkNode(3)
l1.next.next.next = LinkNode(9)

l2 = LinkNode(5)
l2.next = LinkNode(6)
l2.next.next = LinkNode(6)
l2.next.next.next = LinkNode(3)

# to visualize the list elements
def printList(l):
    str1=''
    while l:
        str1 += str(l.val)
        l=l.next
        if l:
            str1 += '->'
    print(str1)

#adding values stored in lists
#carry is here to avoid situations like 7->0->10->2->1. (e.g. previous version had carry initialized to 0 inside func)
def addList(l1,l2,carry=0): 
    if l1.val != None and l2.val != None:
        sum = carry + l1.val + l2.val
        if sum >9:
            carry = 1
            sum -= 10
    elif l1.val != None:
        sum = carry + l1.val
    elif l2.val != None:
        sum = carry + l2.val
    else:
        sum = None
    #the output
    l3 = LinkNode(sum)
    if l1.next and l2.next:
        l3.next = addList(l1.next, l2.next, carry)
        l3.next.val =  addList(l1.next, l2.next, carry).val
    elif l1.next: #use dummy node for recursive call
        l1 = l1.next
        l3.next = LinkNode(addList(l1, LinkNode(None), carry).val)
    elif l2.next: #use dummy node for recursive call
        l2 = l2.next
        l3.next = LinkNode(addList(l2, LinkNode(None), carry).val)
    elif carry == 1: #if there's carry still left over add another node
        l3.next = LinkNode(carry)    
    return l3

printList(l1)
printList(l2)
printList(addList(l1,l2))

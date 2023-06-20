from dtos import SLinkedList
from dtos import Node
from dtos import ListNode
from Add_Two_Numbers import addTwoNumbers
from Remove_Nth_Node_From_End_of_List import removeNthFromEnd

list1 = SLinkedList()
list1.head = Node(1)
e2 = Node(2)
e3 = Node(3)
list1.head.next = e2
e2.next = e3
list2 = SLinkedList()
list2.head = Node(1)
e2 = Node(2)
e3 = Node(3)
list2.head.next = e2
e2.next = e3
print(addTwoNumbers(list1,list2))
n = 1
head = ListNode(1)
head.next = ListNode(2)
print(removeNthFromEnd(head, n))






        

from dtos import SLinkedList
from dtos import ListNode

def addTwoNumbers(l1: SLinkedList, l2: SLinkedList) -> ListNode:
        head = ListNode()
        current = head
        current1 = l1.head
        current2 = l2.head
        module = 0
        while current1 != None or current2 != None or module != 0:
            if l1:
                l1_value = current1.value
            else:
                l1_value = 0
            if l2:
                l2_value = current2.value
            else:
                l2_value = 0
            sum = l1_value + l2_value + module
            current.next = SLinkedList(sum % 10)
            module = sum // 10
            current1 = current1.next if current1 else None
            current2 = current2.next if current2 else None
            current = current.next
        return(head.next)
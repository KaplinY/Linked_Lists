from dtos import ListNode
        
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        current = head
        length = 0
        while current:
            current = current.next
            length += 1
        node = length - n - 1
        current = head
        i=0
        while current:
            prev = current
            current = current.next
            if i == node:
                break
            i+=1
        if current == None:
            return(head.next)
        prev.next = current.next
        current = None
        return(head)
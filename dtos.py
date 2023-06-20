class Node:
   def __init__(self, value=None):
      self.value = value
      self.next = None

class SLinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
               current = current.next
            current.next = new_node
        else:
           self.head = new_node

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None

    def insert(self, new_element, position):
        count=1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while current:
            if count+1 == position:
                new_element.next = current.next
                current.next = new_element
                return
            else:
                count+=1
                current = current.next
        pass

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            
    def check(self, value):
        current = self.head
        while current:
            if current.value == value:
                return(True)
            current = current.next
        return(False)
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        if not self.head:
            self.head = new_element
            return

        prev_element = self.head
        new_element.next = prev_element
        self.head = new_element
        return

    def delete_first(self):
        if not self.head: 
            return
        if not self.head.next:
            deleted_el = self.head
            self.head = None
            return deleted_el
        
        deleted_el = self.head
        self.head = self.head.next
        deleted_el.next = None
        return deleted_el

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        if not self.ll.head:
            self.ll.head = new_element
            return
        second_el = self.ll.head # Create Ref
        new_element.next = second_el # Add Ref to new_element
        self.ll.head = new_element # making the new_element the first one 
        return 

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        if not self.ll.head:
            # print('No Element Found!')
            return 
        
        if not self.ll.head.next:
            pop_el = self.ll.head
            self.ll.head = None
            pop_el.next = None
            return pop_el
        
        pop_el = self.ll.head
        self.ll.head = self.ll.head.next
        pop_el.next = None
        return  pop_el
        
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)


# ll_list = LinkedList(e1)

# print(ll_list.head.next)


# Start setting up a Stack
stack = Stack(e1)
# Test stack functionality
stack.push(e2)
stack.push(e3)


print (stack.pop().value)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop())
stack.push(e4)
print (stack.pop().value)
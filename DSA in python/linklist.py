"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

# insert the element.
# get_position returns the element at a certain position.
# deletes the element.

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

    def get_position(self, position):
        element= self.head
        count = 1
        if self.head:
            if position == count:
                return element
            while count < position:
                count += 1
                if element.next != None:
                    element = element.next
                else:
                    return None
            return element       
        return None 

    def insert(self, new_element, position):
       if position < 1:
          print("Invalid position. Position must be 1 or greater.")
          return 
       currentEl = self.head
       count = 1
       if self.head:
        if position == count:
            new_element.next = currentEl
            self.head = new_element
        else:
            while count < position:
                count += 1
                currentEl = currentEl.next
                if count == position:
                    new_element.next = currentEl
                    currentEl = new_element

                    count2 = 1
                    currentEl2 = self.head
                    while count2 < position-1:
                        count2 += 1
                        currentEl2 = currentEl2.next
                        if count2 == position-1:
                            currentEl2.next = new_element
       else:
         self.head = new_element

    def delete(self, value):
        currentEl = self.head
        count = 1
        if self.head:
            if count == value:
                self.head = currentEl.next
            else:
                while count < value: 
                    count += 1
                    currentEl = currentEl.next
                    if count == value:
                        currentEl2 = self.head
                        count2 = 1
                        while count2 < value:
                            if count2 == value-1:
                                currentEl2.next = currentEl.next
                            count += 1

# Test cases
# Set up some Elements
e1 = Element('1')
e2 = Element('2')
e3 = Element('3')
e4 = Element('4')
e5 = Element('5')
e6 = Element('6')

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)


check = Element('check')


ll.insert(check, 4)


print(ll.get_position(3).value)


"""Go till current_node becomes position - 1 """

# current_node = self.head
# for _ in range(position - 2):
#             if current_node is None:
#                 print("Invalid position. Position exceeds the length of the list.")
#                 return
#             current_node = current_node.next
#         if current_node is None:
#             print("Invalid position. Position exceeds the length of the list.")
#             return
#         new_node.next = current_node.next
#         current_node.next = new_node

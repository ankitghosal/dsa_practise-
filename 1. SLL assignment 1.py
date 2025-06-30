
'''Singly Linked List'''

# 1. define a class Node to discuss a node of a singly linked list.
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


# 2. define a class SLL to implement SIngly Linked List with "__init__()" method to create and initialise start referrence variable.

class SLL:
    def __init__(self, start=None):
        self.start = start
        
# 3. define a method is "empty" to check if the linked list is empty in SLL class.
    def is_empty(self):
        return self.start==None
    
# 4. in class SLL, define a method "insert_at_start()" to ''insert an element at the starting'' of the list.       

    def insert_at_start(self, data):
        n = Node(data, self.start)  # Connecting with 'next nodes'
        self.start = n              # Connecting with 'Start'

# 5. in class SLL, define a method "insert_at_last()" to ''insert an element at the end'' of the list. 
    def insert_at_last(self, data):
        n = Node(data)  #as it's the last obj so next = None( so not putting value)
        if not self.is_empty():  #therefore, fn wont run if it's empty
            temp=self.start     # temp - used in traversing
            while temp.next is not None:
                temp=temp.next
            temp.next=n

        # if list was empty
        else:
            self.start=n

# 6. in class SLL, define a method "search()" to find the node with specified element value.
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp     # if item value same with temp data then it's the same temp fine. So return
            temp=temp.next
        return None     # this indicated the search is fail

# 7. in class SLL, define a method "insert_after()" to insert a new code after a given node of the list
    def insert_after(self,temp,data): # temp cz need to search the new node after which it'll insert
        if temp is not None:
            n=Node(data, temp.next)
            temp.next=n

# 8. in class SLL, define a method to print all the elements of the list.
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item, end= ' ')
            temp=temp.next

# 10. in class SLL, define a method delete_first() to delete first element from the list.
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
        
# 11. in class SLL, define a method delete_last() to delete last element from the list.
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next in None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

# 12. in class SLL, define a method delete_item() to delete specified element from the list.
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next

# 9. in class SLL, implement iterator  for SLL to access all the elements of the list in a sequence.

    def __iter__(self):
        return SLLIterator(self.start)

class SLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data


# Driver code
mylist=SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()
mylist.delete_item(20)
print()

mylist.print_list()
print()







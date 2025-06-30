#1. create Node
class Node:
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next
        

#2. Create Start
class SLL:
    def __init__(self, start=None):
        self.start=start

#3. Check if Node is Empty

    def is_empty(self):
        return self.start==None

#4. insert element at starting of the list
    def insert_at_start(self, data):
        n=Node(data, self.start)
        self.start=n

#5. insert at last of the list
    def insert_at_last(self, data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n


    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n

    def insert_at_last(self, data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
                temp.next=n
        else:
            self.start=n

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
    

    def insert_at_start(self, data):
        n=Node(data, self.start)
        self.start=n

    def insert_at_end(self, data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
                temp.next=n

        else:
            self.start=n

# Search a value
    def search(self, data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    



    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None


    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data, temp.next)
            temp.nex=n

    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next

mylist=SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.priint_list()
print()




class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class singlyLinkedList:
    def __init__(self):
        self.headval=None

# Function for printing the linkedlist
    def printList(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

# Function for know the size of linkedList
    def size(self):
        if self.headval == None:
            print("linkedList is Empty")
            return 0
        count = 0
        temp = self.headval
        
        while temp is not None:
            temp = temp.nextval
            count += 1
        return count

# Adding Node at the begining
    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

# Adding Node at the End
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return 
        temp = self.headval
        while(temp.nextval):
            temp = temp.nextval
        temp.nextval = NewNode

# Adding Node at the particular index
    def AddAtPosition(self, idx, newdata):
        NewNode = Node(newdata)
        if idx<0 or idx>self.size():
            print("Wrong idx")
            return

        temp = self.headval
        for i in range(idx-1):
            temp = temp.nextval
        
        temp1 = temp.nextval
        temp.nextval = NewNode
        NewNode.nextval = temp1

# Removing fron linkedlist
    def remove(self, data):
        temp = self.headval

        if temp is not None:
            if temp.dataval==data:
                self.headval = temp.next
                temp=None
                return
        while temp is not None:
            if temp.dataval==data:
                break
            pre = temp
            temp = temp.nextval
        
        if temp==None:
            print("Didnot find the node which you want to remove")
            return

        pre.nextval = temp.nextval
        temp=None



list1 = singlyLinkedList()
list1.headval = Node(10)
n2 = Node(20)
n3 = Node(30)

list1.headval.nextval = n2
n2.nextval = n3

# adding at begining
list1.AtBegining(1)

# adding at end
list1.AtEnd(50)

# add at particular index
list1.AddAtPosition(2, 80)

print("Before removing")
list1.printList()

# Remove
list1.remove(30)

print("After removing")
list1.printList()
# len = list1.size()
# print(len)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

#connecting nodes
node1.next=node2
node2.next=node3
node3.next=node4


#inerting at beginning
# head=node1
# new_node=Node(50)
# new_node.next=head
# head=new_node

#printing the linked list
# head=node1
# current=head
# while (current != None):
#     print(current.data,end="->")
#     current=current.next
# print(None)


#insert node in beginning
head=node1
new=Node(50)
new.next=head
head=new
current=head

while (current != None):
    print(current.data,end="->")
    current=current.next
print(None)



#inertion at end


head=node1
new=Node(50)
current=head

while current.next is not None:
    current=current.next
current.next=new

head=node1
current=head
while (current != None):
    print(current.data,end="->")
    current=current.next
print(None)


#insertion at specific position
#creating node to add 
new=Node(25)

head=node1
current=head

#adding aftrer 20
while current is not None and current.data!=20:
    current=current.next

new.next=current.next
current.next=new

current=head
while (current != None):
    print(current.data,end="->")
    current=current.next
print(None)
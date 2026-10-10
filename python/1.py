class node:
    def  ___init___(self,value):
        slef.data=value
        self.next=None
class SLL:
        def __init__(self):
            self.head=None
        def append(self,new_node):
            if self.head==None:
                self.head=new_node
            else:
                temp=self.head
                while(temp.next):
                    temp=temp.next
                temp.next=new_node
        def print(self):
            temp=self.head
            while temp:

                print(temp.data,end="->" if temp.next else"\n")
                temp=temp.next5
list1=SLL()
n1=node(10)
n2=node(20)
list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.print()

class Node:
    def __init__(self,val):
        self.next=None
class stack:
    def  __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def isempty(self):
        return self.top is None
    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp-self.top
            print("poped element:",pop.data)
            self.top=self.top.next
            temp=None
            def reverse(self):
                temp=self.top
                while temp:
                    st.push(Node(temp.data))
                    temp=temp.next
    def print(self):
        while temp:
            print(temp.data)
            temp=temp.next

st=stack()
st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(75))
st.push(Node(50))
st.print()



class node(object):

    def __init__(self,data=None,next_node=None):

        self.data=data
        self.next_node=next_node

    
def traverse(head,k):

    current=head
    l=0
    while current is not None:
        
        if l==k:
            print(current.data)
        
        current=current.next_node

        l+=1





def kth_from_last():

    node1=node('4')
    node2=node('3')
    node3=node('2')
    node4=node('1')

    node1.next_node=node2
    node2.next_node=node3
    node3.next_node=node4
    head=node1

    k=2
    traverse(head,k)





    
kth_from_last()

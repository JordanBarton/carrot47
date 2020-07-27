
class node:
    def __init__(self , value = None):
        self.value = value
        self.next_value = None
        
class linked_list:
    def __init__(self):
        self.head_value = None
        
    def print_list(self):
        print_value = self.head_value
        while print_value != None:
            print(print_value.value)
            print_value = print_value.next_value
        print("\n")
            
    def start(self,value):
        new_node = node(value)
        new_node.next_value = self.head_value
        self.head_value = new_node
        
        
    def end(self,value):
        new_node = node(value)
        #if the list is empty make end the start
        if  self.head_value is None:
            self.head_value = new_node
            
        #loop over list to get the current last element
        else:
            
            temp = self.head_value
            while(temp.next_value):#if next value exists loop
                temp = temp.next_value
            
            #once there is no next value it exits the list
            #now we have the current last node which we can add to
            temp.next_value = new_node
            
            
                #string ,node
    def inner(self,value,location):
        new_node = node(value)
        if location is None:
            print("the location doesn't exist")
        else:
            
            new_node.next_value = location.next_value
            #create a linked list of size 2
            location.next_value = new_node
            #link it onto the location
            
            
    def delete_node(self, node_to_delete):
        
        if  self.head_value is None:
            print("no header value")
            
        #loop over list to get the current last element
        else:
            
        
            temp = self.head_value
            flag = True
            while flag == True:
                temp = temp.next_value
                if temp.next_value == node_to_delete:

                    temp.next_value = temp.next_value.next_value
                    flag = False
                




list1 = linked_list()

e1 = node("monday")
e2 = node("tuesday")
e3 = node("wednesday")




list1.head_value = e1
e1.next_value = e2
e2.next_value = e3

list1.print_list()

list1.start("sunday")

list1.print_list()

list1.end("thursday")

list1.print_list()

list1.inner("jordan day",list1.head_value.next_value)

list1.print_list()

list1.delete_node(list1.head_value.next_value.next_value)

list1.print_list()

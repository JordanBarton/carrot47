import re
import numpy as np

#check for repeat characters
def ex1_1():
    string = str('Hhel lo121 343')

    previous=[]

    for i in range(0,len(string)):

     
       
             for j in range(0,len(previous)):

               

                 if str(string[i].lower())==str(previous[j]):

                        print('the character: ',string[i],' is a repeat')


             previous.append(str(string[i].lower()))

   
  
#replace whitespace
def ex1_2():




    string1='godly'
    string2='dogly'

    s1=''.join(sorted(string1))
    s2=''.join(sorted(string2))
    print(s1)
    print(s2)

    if s1==s2:
        print('they are a permutation of each other')

    if s1!=s2:
        print('they are NOT a permutation of each other')
    


#check if permutation
def ex1_3():

    string = 'i like dogs'

    new_string=re.sub(' ', '%20%', string)

    print(new_string)

            

#check if palindrome
def ex1_4():

    string='rotor'

    new_string=string[::-1]

    if new_string==string:

        print(string,' is a palindrome')

    else:

        print(string,' is NOT a palindrome')


#1 or zero edits away for 2 strings
#e.g pale and palet is True
#pale and pal True
#pale and palets False
def ex1_5():

    string1= 'pale'
    string2= 'palet'
    test='abcdefghijklmnopqrstuvwxyz'

    if string1==string2:

        print('no edits required')

    else:

        
        for i in range(0,len(string1)+1):

            s1=''
            s2=''

            for j in range(0,len(string1)):

                if j<i:
                    s1+=string1[j]
                if j>=i:
                    s2+=string1[j]

            #print(s1,s2)

            for k in range(0,len(test)):

                s=s1+test[k]+s2

                if s==string2:

                    print('add the letter ',test[k],'to the ',i+1,'th character of ' ,string1 ,'to get ',string2)


            for i in range(0,len(string1)+1):

                s1=''
                s2=''

                for j in range(0,len(string1)):

                    if j<i:
                        s1+=string1[j]
                    if j>i:
                        s2+=string1[j]

                

                s=s1+s2

                if s==string2:
                    print('remove the letter ',string1[i],'from the ',i+1,'th character of ',string1 ,'to get ',string2)

                               
                               

            












                      

#string compression aaabbcc->a3b2c2
def ex1_6():
    result=''
    
    string1='aaabbcc'

    string=string1+str(1)
       
    j=1
    for i in range(0,len(string)-1):

        if string[i+1]==string[i]:
            j+=1

        else:
            
            join=string[i-1]+str(j)
            j=1

            result+=join

    print(result)       

          
        
   


#rotate a square matrix'
def ex1_7():

    def ccw(A):

      
       
        B=np.zeros((len(A),len(A)))
        for i in range(0,len(A)):   

            for j in range(0,len(A)):

                B[j][i]=A[i][j]


        C=B[::-1]
        print(C,'\n')
        return C 
        #COUNTER

    A=[[1,2,3],[4,5,6],[7,8,9]]

    print(A)

    ccw(ccw(ccw(A)))


#set row 0 if any zeroes in a matrix          
def ex1_8():

    A=[[1,0,2],[1,4,1],[0,0,12]]
    C=[]

    
    for i in range(0,len(A)):
        B=[]
        if min(A[i])==0:

          

             for j in range(0,len(A[i])):

                 B.append(0)

        else:
            for k in range(0,len(A[i])):

                 B.append(A[i][k])

        C.append(B)

    print(C)


#slide a string and check if equal to another string  
def ex1_9():

    a='123456789'
    n=len(a)

    b='567891234'

    
    a=a+a

    for k in range(0,n):
        s=''
        for i in range(k,n+k):

            s+=a[i]

        if s==b:

            print('1 permutation required')

        

    



def ex2_1():

    class node(object):

        def __init__(self,data,next_node=None):

            self.data=data
            self.next_node=next_node



    def traverse(head):
        current_node=head
        while current_node is not None:
            print(current_node.data)
           
            current_node=current_node.next_node


            

    def delete_node(head,value):

        current_node=head
        previous_node=None
        while current_node is not None:
            

              if current_node.data==value:

                  if previous_node is None:
                      print('here')
                      new_head=current_node.next_node
                      current_node.next_node=None
                      return newhead

                  previous_node.next_node=current_node.next_node
                  return head


              previous_node=current_node
              current_node=current_node.next_node
                

        return head



    def remove_dups(head):


        current_node=head
        while current_node is not None:


            second_node=current_node

            
            while second_node.next_node is not None:

                
                if second_node.next_node.data==current_node.data:
                    
                    second_node.next_node=second_node.next_node.next_node

                else:
                    second_node=second_node.next_node

            current_node=current_node.next_node

            
        return head

                
    node1=node('5')
    node2=node('0')
    node3=node('1')
    node4=node('1')
    node5=node('8')
    node6=node('9')
    node7=node('1')
    node8=node('5')

    node1.next_node=node2
    node2.next_node=node3
    node3.next_node=node4
    node4.next_node=node5
    node5.next_node=node6
    node6.next_node=node7
    node7.next_node=node8

    head=node1

    traverse(head)
    print('\n')



    head=remove_dups(head)

    traverse(head)

    
               
    

           
def ex2_2():



    


    
    

import random

string='hello'
array1=[5,6,7,8,4,9,0,1,2,3,51]
array2=[5,6,7,8,9,0,1,2,3,51]

def reverse_string(string):

    reverse=''
    for i in range(0,len(string)):
        

        reverse+=''+string[len(string)-i-1]

    return reverse

        
        

def find_missing(array1,array2):

    a1=sorted(array1)

    a2=sorted(array2)

    for i in range(0,len(array1)):

        if a1[i]!=a2[i]:

            print(a1[i] ,'is missing')

            return a1[i]







def shuffle_string(string):

    choose=0
    for i in range(0,round(len(string))):

       
        choose=random.randint(0,len(string)-1)
        
        old= string[i]
        new= string[choose]

        
        string[i]=new
        
        



    print(string)






shuffle_string(string)





















    

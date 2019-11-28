
#example is ['p','e','r','f','e','c','t',' ','m','a','k','e','s',' ','p','r','a','c','t','i','c','e']

# want to return ['p','r','a','c','t','i','c','e',' ','m','a','k','e','s',' ','p','e','r','f','e','c','t']


#need to save everything up to whitespace and make that its own substring
#do this for every whitespace
#then reverse the order of the substrings and reform the string
def reverse_sentence(string):


    sub=[]
    subnew=[]
    for i in range(len(string)):

       
            
        
        if string[i]!=' ':


            sub.append(string[i])

    
        if string[i]==' ' or i==len(string)-1:
            sub.append(' ')

            subnew.append(sub)

            sub=[]

        

    subnew=subnew[::-1]
    print(len(subnew))

    reversed_string=[]
    for i in range(0,len(subnew)):

        for j in range(0,len(subnew[i])):

            
            print(i,j)

            if i ==len(subnew)-1 and j == len(subnew[i])-1:

                pass

            else:

                reversed_string.append(subnew[i][j])



    print(reversed_string)
        






string=['p','e','r','f','e','c','t',' ','m','a','k','e','s',' ','p','r','a','c','t','i','c','e']

reverse_sentence(string)

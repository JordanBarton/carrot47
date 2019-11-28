import sys

M=[]
for inp in sys.stdin:
    M.append(str(inp))
    


def EXPLODE(x):
    sumx=0
    x=str(x)
    for i in x:
        sumx+=int(x)
        
    return sumx


for N in M:
    revN = N[::-1]
    
    sumA = 0
    sumB = 0
    for i in range(len(revN)):
        if (i)%2==0:
            sumA+= int(revN[i])
        elif(i+1)%2==0:
            if int(revN[i])*2 > 9:
                sumB += EXPLODE(revN[i])
            else:
                sumB += int(revN[i])
    
    if (sumA+sumB)%10==0:
        print('Yes')
    else:
        print('No')
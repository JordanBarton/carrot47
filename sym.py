nearest=[]
with open('cost full2.csv') as file:
     
    
  
        for line in file:
            s=line.split(',')
            row=[]
            for i in range(0,215):
                row.append(s[i])
            nearest.append(row)
file.close()
n=0
for i in range(0,len(nearest)):
    for j in range(0,len(nearest)):
    
        if int(nearest[i][j])!=int(nearest[j][i]):
            print(int(nearest[i][j])-int(nearest[j][i]))
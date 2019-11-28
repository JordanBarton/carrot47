#currently hill hill cost
#want a square of to/from


import csv
To=[]
From=[]
Cost=[]
rows=[]
with open('cost_matrix_2.csv','r') as file:

    csv_read=csv.reader(file,delimiter=',')
    l=0

    for line in csv_read:
        if l==0:
            pass

        if l!=0:

            From.append(line[0])
            To.append(line[1])
            Cost.append(line[2])

            rows.append([line[0],line[1],line[2]])

        l+=1

data_matrix=[]
To_sorted=sorted(To)
From_sorted=sorted(From)



From_new=[]
To_new=[]
for i in range(0,len(From)-1):

    if From_sorted[i+1]!=From_sorted[i]:
        From_new.append(From_sorted[i])


for i in range(0,len(To)-1):
    if To_sorted[i+1]!=To_sorted[i]:
    
        To_new.append(To_sorted[i])




header=[]
for i in range(-1,len(From_new)):

    if i==-1:
        header.append('To\From')

    else:
        header.append(From_new[i])

data_matrix.append(header)




for i in range(0,len(From_new)):
   

    end=To_new[i]
    row=[]
    row.append(end)
    
    for j in range(0,len(From_new)):

        start=From_new[j]

        
        for k in range(0,len(rows)-1):

            if start==rows[k][0] and end == rows[k][1]:

                row.append(rows[k][2])

            if start==rows[k][0] and end!=rows[k][1]:
    
                if rows[k+1][0]!=rows[k][0] and rows[k+1][1]!=rows[k][1]:

                    row.append(0)


    
        
        data_matrix.append(row)







with open('square.csv', mode='w',newline='') as new_file:
    new_file_writer = csv.writer(new_file, delimiter=',')


    for i in range(0,len(data_matrix[0])-1):
           
                new_file_writer.writerow(data_matrix[i])


        

    




   
            
    

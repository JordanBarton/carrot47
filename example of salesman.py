import random, numpy, math, copy, matplotlib.pyplot as plt

import csv

#def distance(lat,long):


with open('coordsOfExtendedWainwrights.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    
    lat=[]
    long=[]
    i=0
    for row in csvReader:
        i+=1
        if i!=1:
            lat.append(float(row[8]))
            long.append(float(row[9]))
N=len(lat)
            
X=[random.sample(range(100), 2) for x in range(N)];
for i in range(0,N):
    X[i][1]=float(lat[i])
    X[i][0]=float(long[i])

print(X)

        


cities = X

tour = random.sample(range(N),N);

for temperature in numpy.logspace(0,5,num=100000)[::-1]:
    [i,j] = sorted(random.sample(range(N),2));
    newTour =  tour[:i] + tour[j:j+1] +  tour[i+1:j] + tour[i:i+1] + tour[j+1:];
    if math.exp( ( sum([ math.sqrt(sum([(cities[tour[(k+1) % N]][d] - cities[tour[k % N]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]]) - sum([math.sqrt(sum([(cities[newTour[(k+1) % N]][d] - cities[newTour[k % N]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]])) / temperature) > random.random():
        tour = copy.copy(newTour);
        
fig, ax = plt.subplots()

ax.plot([cities[tour[i % N]][0] for i in range(N+1)], [cities[tour[i % N]][1] for i in range(N+1)], 'ro');

   

for i in range(0,N):
    ax.annotate(i, (X[i][0],X[i][1]))
    
plt.plot([cities[tour[i % N]][0] for i in range(N+1)], [cities[tour[i % N]][1] for i in range(N+1)], 'ro');

   
    
 
plt.show()
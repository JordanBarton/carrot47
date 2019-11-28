
points=[[1,1],[2,1],[3,-1],[2,-1]]

origin=[2,2]

k=6



def kth_closest(origin,points,k):

    #want the kth closest point
    #first need to determine closest points
    distance_squared=[] 
    for index,coord in enumerate(points):

     
    #returns distance squared but we can still rank order without sqrt
        d=[pow(coord[0]-origin[0],2)+pow(coord[1]-origin[1],2),coord]
        distance_squared.append(d)


    print(distance_squared)
    distance_squared_sorted=sorted(distance_squared)
    print(distance_squared_sorted)

    for i,coord in enumerate(distance_squared_sorted):

        if i+1==k:

            print(coord[1])

            return coord[1]


kth_closest(origin,points,k)

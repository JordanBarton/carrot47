#plot a path from start to end
import matplotlib.pyplot as plt


def plot_path(path_indices,direct,new_record):
    
        fig= plt.figure('route of Wainwrights')
        with open('indices.csv') as file:
            places=[]
            x_index=[]
            y_index=[]
            for line in file:
               s=line.split(',')
               places.append(s[0])
               x_index.append(s[1])
               y_index.append(s[2])    
        file.close()
    
       
        for k in range(0,len(path_indices)):
                
                if k==len(path_indices)-1:
                    (x,y)=path_indices[k]
                    (xnew,ynew)=path_indices[0]
                    plt.plot([x,xnew],[y,ynew],'g-')
                    plt.text(x,y,str(k+1))
                    
                else:
                    (x,y)=path_indices[k]
                    (xnew,ynew)=path_indices[k+1]
                  
                    
                    plt.plot([x,xnew],[y,ynew],'g-')
                    plt.text(x,y,str(k+1))
                
                
            
                  

                    
            
                
                
        
         
      #  plt.plot(441	,756,'bo')
        plt.grid()
    
        plt.text(0,0,'model: '+str(new_record))
                 
       
        plt.show()
        fig.savefig(direct, dpi=fig.dpi)

def main(path_indices,direct,new_record):
    
    
    plot_path(path_indices,direct,new_record)

if __name__=='main':

    main()




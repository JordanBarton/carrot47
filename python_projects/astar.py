#want to a*
import pygame
import time
#def save_path: reconstruct path once completed



def button(msg,x,y,width,height,colour_on,colour_off):
          
    font = pygame.font.Font('freesansbold.ttf', 32) 
  
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+width>mouse[0]>x and y+width>mouse[1]>y:
        pygame.draw.rect(display_surface,colour_on,(x,y,width,height)) 
       
        if click[0] == 1:
            time.sleep(0)
            return 1

    else:
        pygame.draw.rect(display_surface,colour_off,(x,y,width,height)) 



     
            
    








class Node:
    def __init__(self, parent = None, position = None):
        self.parent=parent
        self.position = position
        self.g = 0 #from start to current
        self.h = 0# from current to end
        self.f = 0

        #define a way to check if nodes are different or not
        def __eq__(self,other_node):
            return self.position == other_node.position












def astar(maze, start_pos, end_pos):

    start_node = Node(None, start_pos)
    end_node = Node(None, end_pos)
 
 
    open_set   = []
    closed_set = []
    
    open_set.append(start_node)
    
    #came from = None
    
   
    #g = inf
    #g(start_node) = 0
    
    #h = inf
    #h(start) = #manhattan metric to end
    
    #f = g+h
    
    while len(open_set) != 0:
        
        #initialise the first step
        current_node = open_set[0]
        i = 0
        current_i = 0
        
        #look for improvements
        for i , node in enumerate(open_set):
            if node.f < current_node.f:
                current_node = node
                current_i    = i
        
        #add current_node to closed list
        open_set.pop(current_i)
        closed_set.append(current_node)
        
        if int(current_node.position[0]) == int(end_node.position[0]) and int(current_node.position[1]) == int(end_node.position[1]) :
           
            path = []
            #complete when back to start
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
                
            return path[::-1]
            
            
        candidate = []
        for new_pos in [(0,-1),
                        (0,1),
                        (-1,0),
                        (1,0),
                        (-1,1),
                        (-1,-1),
                        (1,-1),
                        (1,1)]:
                
                node_pos = (current_node.position[0]+new_pos[0],
                            current_node.position[1]+new_pos[1])
                
                #eliminate node_positions outside of maze and obstactles
                if node_pos[0]>len(maze)-1 or node_pos[0]<0 or node_pos[1]>len(maze)-1 or node_pos[1] <0 :
                    continue
                
                
                if maze[node_pos[0]][node_pos[1]] !=0:
                    continue
            
                new_node = Node(current_node,node_pos)
                candidate.append(new_node)
        
        for child in candidate:
            child.g = current_node.g + 1
            child.h = (child.position[0] - end_node.position[0])**2+(child.position[1] - end_node.position[1])**2
            child.f = child.g + child.h
          
        
            for open_node in open_set:
                if child == open_node and child.g > open_node.g:
                    continue
                
            open_set.append(child)
                #if neighbour not in open set:
                    #open_set.add(neighbour)
            




pygame.init() 
  
# define the RGB value for white, 
#  green, blue colour . 
black = (0,0,0)
white = (255, 255, 255) 
green = (0, 200, 0) 
red = (200,0,0)
bright_red = (255,0,0)
bright_green=(0,255,0)
blue = (0,0,255)


# assigning values to X and Y variable 
X = 1000
Y = 1100
  
# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((X, Y )) 
  
# set the pygame window name 
pygame.display.set_caption('a*') 
  
# create a font object. 
# 1st parameter is the font file 
# which is present in pygame. 
# 2nd parameter is size of the font 
display_surface.fill(black) 
start = (0, 0)
end = (7, 6)
N=10
playing = True
maze = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]



while playing:
  
    
    pygame.event.pump()
    pygame.display.update()
    for i in range(0,N):
        for j in range(0,N):
            if maze[i][j] == 1:
                button("",100*i,100*j,100,100,black,black)
            else:
                maze[i][j] = button("",100*i,100*j,100,100,black,white)
  
    end_game = button("run",0,1000,1100,100,bright_green,bright_red)
    if end_game ==1 :
        for i in range(0,N):
            for j in range(0,N):
                if maze[i][j] == None:
                    maze[i][j] = 0
        path = astar(maze, start, end)   
        
        for i in range(0,N):
            for j in range(0,N):
                for k in range(0,len(path)):
                    if i==path[k][0] and j ==path[k][1]:
                        button("",100*i,100*j,100,100,blue,blue)
                    
    button("",100*start[0],100*start[1],100,100,green,green)
    button("",100*end[0],100*end[1],100,100,red,red)
    pygame.display.update()
    
        

    
    
    for event in pygame.event.get() : 
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
  
            # deactivates the pygame library 
            pygame.quit() 
  
            # quit the program. 
            quit() 
    pygame.display.update()
     


#now need to create a UI
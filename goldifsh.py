
import random



class parent:
    def __init__(self,name):
        self.name=name
        self.health=random.random()


    def hello(self):
        print('hello i am ', self.name)

    def doctor_needed(self):
        if self.health < 0.8:
            return True
        else:
            return False



class child(parent):
    def hello(self):
        print('all is good,' ,self.name,'wil take care of you')
    def heal(self,robo):
        robo.health=random.uniform(robo.health,1)
        print(robo.name,'healed by',self.name)
     
    


y=child('bobby')
child_list=[]
for i in range(5):
    x=parent('roger'+str(i))
    if x.doctor_needed():
        print('health level',x.name,'is',x.health)
        y.heal(x)
        print('health level',x.health)
        child_list.append((x.name,x.health))


print(child_list)

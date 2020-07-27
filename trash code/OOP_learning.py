

class dog:  
    def __init__(self, name, breed, colour, age):
    
        self.name = name
        self.breed = breed
        self.colour = colour
        self.age = age
       
        
    def set_name(self,name):
        self.name = name
        
    def get_name(self):
        return self.name
  
  
    def bark(self):
        print("bark")
        
    def add_one(self, x):
        return x + 1
        
        
        
d = dog("tim", "pug", "brown", 3)
d.set_name("bill") 
d.get_name()




d.bark()

print(type(d))

print(d.add_one(5))























class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade


class course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students =[]
        
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for i in self.students:
            value += i.get_grade()
        
        return value/len(self.students)
    
    
s1 = student("tim", 19, 95)
s2 = student("bill", 18, 10)
s3 = student("gill", 10, 50)

science = course("science" , 2)
science.add_student(s1)
science.add_student(s2)
science.add_student(s3)

science.get_average_grade()
        
    
    
    

class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(self.name, self.age)
        
    def speak(self):
        print("no idea")


class cat(pet): 
    def __init__(self, name, age, colour):
        super().__init__(name,age)
        self.colour = colour
    
    
    def speak(self):
        print("meow")
        
class dog(pet):
    def speak(self):
        print("bark")
        
class fish(pet):
    pass
        
p = dog("phil" , 19)
p.speak() 
 
d = dog("tim" , 19)
d.speak()

c = cat("bill" , 34, "blue")
c.speak()

f =  fish("bubbles", 10)
f.speak()


















class person:
    number_of_people = 0
    g = 9.81
    
    def __init__(self, name):
        self.name = name
        person.number_of_people += 1
        
     
#these only act on class attributes, variables before __init__
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people_ += 1
        
        
p1 = person("jordan")

p2 = person("adam")

print(person.number_of_people_())




class math:
    
    @staticmethod
    def add5(x):
        return x + 5
    
    
    @staticmethod
    def pr():
        print("run")

print(math.add5(54))
math.pr()
#%%



def largest_number(*args):

    return max(args)


#create global class dog
class pet:
    
    #define global fixed attributes
    
    #define global variable attributes
    def __init__(self , name, age, breed):
        
        self.name = name
        self.age = age
        self.species = "dog"
        self.breed= breed
        
    #define global functions
    def speak(self, sound):
        print("hi i am a" , self.breed, "called", self.name, "and i say" , sound)
        
    def change_species(self, new_species):
        self.species = new_species
        
    def change_breed(self, new_breed):
        self.breed = new_breed
        
        
    


a = pet("albert", 10, "pug")

b = pet("barry", 1, "springer spaniel")

c = pet("carry", 4.5, "poodle")
    
a.speak("woof")

b.speak("bark")

c.speak("meow")
    
c.change_species("cat")
c.change_breed("tabby")

c.speak("meow")




    
    
#%%
    
    
class dog:
        
          #global fixed attributes
          species = "mammal"
          
          #global variables
          def __init__(self,age,name):
              self.age     =   age
              self.name    =   name
 
              
          def get_details(self):
              return "hi i am {}, i am {} years old".format(self.name,
                                                           self.age)
    
    
class springer_spaniel(dog):
        
            def speak(self, sound):
                return sound
            
    
class pug(dog):

            def speak(self, sound):
                return sound
    
    
a = springer_spaniel(10, "alpha") 

b = pug(1, "beta") 



a_details = a.get_details()

a_speak = a.speak("woof")




b_details = b.get_details()

b_speak = b.speak("oink")
    
    
    
#is instance allows us to check where our objects lie on the hierarchy
isinstance(a,pug)
    
    
    
    
    
    
#%% exercises

class family:
    
    pets = []
    
    def __init__(self, pets):
        self.species = "mammal"
        self.pets = pets



class dog:
    
    
    
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        self.is_hungry = False
        self.is_walking = False
   
        
    def speak(self, sound):
        return "i say {}".format(sound)
    
    def run(self, speed):
        return "i run {}".format(speed)
    
    def eat(self):
        self.is_hungry = True
        
    def walk(self):
        self.is_walking = True



a = dog("tom",6)
b = dog("fletcher",7)
c = dog("larry" , 10)

my_family = family([a,b,c])




print("i have {} dogs".format(len(my_family.pets)),
      a.name, "is", a.age,",",
      b.name, "is", b.age,",",
      c.name, "is", c.age,
      "and they're all {}s of course".format(my_family.species))


#want to know how many are hungry
a.eat()
a.is_hungry

n = 0
for i in my_family.pets:
    if i.is_hungry == True:
        n+=1
print(n,"of them are hungry")


#want to make them walk
a.walk()
c.walk()
for i in my_family.pets:
    if i.is_walking == True:
        print("{} is walking!".format(i.name))
    else:
        print("{} is NOT walking!".format(i.name))
     
#%%
        
class vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def honk():
        print("beep")
        
        
class car():
    def __init__(self, make, model, year):
        super().__init__(make, model, year) # = self.make  = make
                                            #   self.model = model
                                            #   self.year  = year
        
        
        self.wheels = 4
        
        
        
a = car ("hyundai", "i30", "2015")      

        
        
#%% multiple inheritance
        
#aquatic
        #-> penguin
#ambulatory
        
class aquatic:
    def __init__(self,name):
        self.name = name
        
    def swim(self):
        print("{} is swimming".format(self.name))
        
    def greet(self):
        print("yoyoyoyoyo")
    
    
class ambulatory:
     def __init__(self,name):
        self.name = name
        
     def walk(self):
         print("{} is walking".format(self.name))
         
     def greet(self):
         print("hi")
    
    

class penguin(ambulatory,aquatic):
    def __init__(self,name):
        super().__init__(name) # = self.name = name

    
    
a = aquatic("bob")
b = ambulatory("phil")
c = penguin("david")


a.swim()
a.greet()

b.walk()
b.greet()


c.walk()
c.swim()
c.greet()

#%%


import builtins


class extend_str:
    def first_and_last_char(self):
        return self[0] + self[-1]

builtins.str = extend_str

str(101).first_and_last_char()

#%% poker hand exercise




#deck
    #shuffle
    #deal (to a player with removal)

#cards
    #number
    #suit
    
from random import shuffle
             
class deck:
    cards = []
    
    def __init__(self,cards):
        self.cards = cards
        
        
    def show_deck(self):
        for card in self.cards:
            print(card.show_card())
            
    def shuffle(self):
        shuffle(self.cards)
        return self
    
    def deal(self):
        return self.cards.pop()
        


class card:
    
    def __init__(self, number, suit):
        self.suit = suit
        self.number = number 
        
    def show_card(self):
        return "{} of {}".format(self.suit,self.number)




suits = ["heart","diamond","club","spade"]
numbers = ["ace",2,3,4,5,6,7,8,9,10,"jack","queen","king"]


total_cards = []
for i in suits:
    for j in numbers:
        new_card = card(i,j)
        total_cards.append(new_card)

       
playing_deck = deck(total_cards)

playing_deck.show_deck()


print("\nnow shuffling\n")
playing_deck.shuffle() # would love to make my own shuffle
playing_deck.show_deck()

print("\nnow dealing\n")
playing_deck.deal()
playing_deck.deal()
playing_deck.show_deck()

#TODO: deal to n players 
#TODO: flop, river, turn
#TODO: burn cards

#%% holy shit never knew you could do this


def shout():
    return "WHOA!"

def whisper():
    return "Shhhh"

def perform_action(func):
    print("something is happening")
    return func()

perform_action(shout)
# something is happening
# 'WHOA!'

perform_action(whisper)
# something is happening
# 'Shhhh'

#%%
#function in a function replaced with decorator notation
def new_decorator(function):#<-----------------¬
 #                        v                      ^
    def inner_function():#v
        print("before")#  v
        function()#<------/
        print("after")
        
    return inner_function()



def decorate_me():
    print("YOYOYOYO")

new_decorator(decorate_me)#--------------------^


################
#use decorator notation


#--------v
def new(func):
    def inner():
        print("before")
        func()
        print("after")
#^       
    return inner()
#^
@new#<-------¬
def decor():#|
    print("YOYOYOOYOY")
    
    
#seems trivial but if i want to use N functions its useful e.g..  
def do_action(fun):  
    def wrap_fun():
        print("something")
        fun()
        return fun()
    return wrap_fun

    
@do_action  
def whisper():
    return "shhhhhh"
 
@do_action    
def shout():
    return "HEEEEEEEEEEEEEEEEEEY"

whisper()
shout()

#%% lambdas
#useful for small functions e.g
#USEFUL FOR LINEAR ALGEBRA e.g square elements etc
def add(x,y):
    return x+y
print(add(1,2))

addition = lambda a,b:a+b
print(addition(1,2))

vector=[1,2,3,4]
list(map(lambda elements:elements**2, vector))

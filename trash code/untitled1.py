from sqlalchemy import create_engine , func
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship , backref

from datetime import date




def add_row(Object,Table):
    

    existing_name = session.query(Table)
    
    count = 0
    for existing_rows in existing_name:
        if Object.name == existing_rows.name:
            count+=1
        
    if count == 0:   
          session.add(Object)
        
        





#create engine
#'sqlite:///census.sqlite'
#'sqlite:///:memory:'

engine = create_engine('postgresql://XXXXXX:XXXXX@localhost:5432/actors')
Session = sessionmaker(bind=engine)



#create base layer
Base = declarative_base()



#we are going to use our SQL database to track users: username and password
#table must have a name
#use a primary key = rownumber

#the USER table will be a subclass of Base
#define the structure of the rows of a table

#create a helper table for the many_to_many relationships
movies_to_actors = Table("movies_to_actors",
                         Base.metadata,
                         Column("movie_id",Integer,ForeignKey("movies.id")),
                         Column("actor_id",Integer,ForeignKey("actors.id")))
        



#each actor only 1 twitter login so one_to_one
class login(Base):
    __tablename__ = "logins"
    
    id = Column(Integer , primary_key = True) 
    #first column is primary key , rowwnumbers
    username = Column(String)
    #second column is name
    password = Column(String)
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
        
#many actors can star in many movies so many_to_many    
class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer , primary_key = True)
    title = Column(String)
    release_date = Column(Date)
    
    actors = relationship("Actor", secondary = movies_to_actors)
    # difference is here
    #no actor id as we use the helper table for that    
    
    def __init__(self,title,release_date):
        self.title = title
        self.release_date = release_date
    
    
#many actors can star in many movies so many_to_many
class Actor(Base):
    __tablename__ = "actors"
    
    id = Column(Integer, primary_key = True)
    name = Column(String)
    age = Column(Integer)
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    
#actor 1 address so one_to_one
class Address(Base):
    __tablename__ = "addresses"
    
    id = Column(Integer, primary_key = True)
    house_name = Column(String)
    street_name = Column(String)
    city = Column(String)
    country = Column(String)
    
    actor_id = Column(Integer , ForeignKey("actors.id"))
    actor  = relationship("Actor", backref = backref("Address", uselist = False))
    # difference is here
    
    def __init__(self,house_name,street_name,city,country,actor):
        self.house_name = house_name
        self.street_name = street_name
        self.city = city
        self.country= country
        self.actor = actor
        
        
#actor 1 can have many houses so many to one
class Stuntman(Base):
    __tablename__ = "stuntmen"
    
    id = Column(Integer, primary_key = True)
    stuntman_name = Column(String)
    stuntman_age = Column(Integer)
    
    actor_id = Column(Integer , ForeignKey("actors.id"))
    actor  = relationship("Actor", backref = "Stuntman") # difference is here
    
    def __init__(self,stuntman_name,stuntman_age,actor):
        self.stuntman_name = stuntman_name
        self.stuntman_age = stuntman_age
        self.actor = actor
        
    

#create the table
Base.metadata.create_all(engine)

session = Session()


mov = session.query(Movie)\
         .all()
         
for m in mov:
    print("{}".format(m))



#create actors
matt_damon = Actor("matt_damon",38)
benedict_cumberbatch = Actor("benedict_cumberbatch" , 40)
linsey_lohan = Actor("linsey_lohan",30)



#create movies
fast_and_furious = Movie("fast_and_furious",date(2002,12,10))
godfather = Movie("godfather",date(1950,12,10))
avengers = Movie("avengers",date(2012,7,7))

#Add actors to movies
fast_and_furious.actors =[matt_damon]
godfather.actors  = [benedict_cumberbatch]
avengers.actors = [ linsey_lohan , matt_damon , benedict_cumberbatch ]


#house_name,street_name,city,country,actor
#create addresses
matt_contact = Address("51", "Burbank", "CA","america", matt_damon)
linsey_contact = Address("461", "lewis close", "CA","america", linsey_lohan )
ben_contact1 = Address("415", "carrington road", "CA","america", benedict_cumberbatch )
ben_contact2 = Address("4126", "sandy lane", "preston","England",benedict_cumberbatch )


#create stuntmen
matt_stuntman = Stuntman("John Doe", 10, matt_damon)
linsey_stuntman = Stuntman("John Roe", 20, linsey_lohan)
ben_stuntman = Stuntman("Richard Roe", 78, benedict_cumberbatch)


add_row(Actor("jordan barton" , 22) , Actor)
#session.add(matt_damon)
#session.add(benedict_cumberbatch)
#session.add(linsey_lohan)

#session.add(fast_and_furious)
#session.add(godfather)
#session.add(avengers)

#session.add(matt_contact)
#session.add(ben_contact1)
#session.add(ben_contact2)
#session.add(linsey_contact)

#session.add(matt_stuntman)
#session.add(ben_stuntman)
#session.add(linsey_stuntman)


session.commit()
session.close()


#now we would like to make some queries regarding the database
                     #Actor,Movie,Address,Stuntman etc.. Base??
#operators on queries include count(),filter(),delete().distinct()
                             #first(),get(),join(),limit(),order_by()
                             #exists()
#also note that now in python \ replaces the %>% in R      
new_movies = session.query(Movie)\
         .filter(Movie.release_date > date(2000,1,1))\
         .all()
         #removes the godfather

for movie in new_movies:
    print("{} released on {}".format(movie.title,movie.release_date))


       
ben_movies = session.query(Movie)\
            .join(Actor, Movie.actors)\
            .filter(Actor.name == "benedict cumberbatch")\
            .all()
            
for movie in ben_movies:
     print("{} released on {}".format(movie.title,movie.release_date))

uk_actors = session.query(Address)\
            .join(Actor, Address.actor)\
            .filter(Address.country == "England")\
            .all()
            
for actor in uk_actors:
         print("{} lives in {}".format(actor.actor.name, actor.country))

       
      #here i show how to mutate a database
ten_times_age = session.query(Address)\
                       .join(Actor, Address.actor)\
                       .add_columns((Actor.age*10).label("ageten"))\
                       .all()
                       
for ages in ten_times_age:
    print ( "{}".format(ages.ageten))
#TODO: add a row that counts how many properties an actor owns!
       #filter out all actors that only own one property
       
       
      #trying to use func.count()????
#number_of_properties = session.query(Address)\
#                       .join(Actor, Address.actor)\
#                       .add_columns(func.count(Address.actor).label("n"))\
#                       .all()
                       
#for properties in number_of_properties:
#    print( "{},{}".format(properties.n, properties.Address.actor.name))
                       
       
       
       
       
       
       
       
       

#create a row
#user1 = login(username = "jordan" , password = "password123")
#user2 = loginusername = "callum" , password = "password123")

#schedule a change
#session.add(user1)
#session.add(user2)

#add all changes to database
#session.commit()

#user_details = session.query(User).filter_by(username = "jordan").all()


#for user in user_details:
#    print("{},{}".format(user.username,user.password))







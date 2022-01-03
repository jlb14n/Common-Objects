class Animal:
    """Animal class"""
    def __init__(self,species,name='',age=0):
        print('Creating animal')
        self.__name = name
        self.__species=species
        self.__age=age
    
    @property
    def name(self):
        print('Getting name')
        return self.__name

    @property
    def species(self):
        print('Getting species')
        return self.__species
    
    @property
    def age(self):
        print('Getting age')
        return self.__age

    @name.setter
    def name(self,new_name):
        print('Setting name')
        self.__name=new_name
    
    @species.setter
    def species(self,new_species):
        print('Setting species')
        self.__species=new_species

    @age.setter
    def age(self,new_age):
        print('Setting age')
        self.__age=new_age

    def move(self):
        print('Moving')
    
    def eat(self,food='something'):
        print('Eating {0}'.format(food))
    
    def drink(self, liquid='water'):
        print('Drinking {0}'.format(liquid))

class Book:
    """Book class"""
    def __init__(self,title,author,publisher='',published=0,pages=0,language=''):
        print('Creating book')
        self.__title=title
        self.__author=author
        self.__publisher=publisher
        self.__published=published
        self.__pages=pages
        self.__language=language
    
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def publisher(self):
        return self.__publisher

    @property
    def published(self):
        return self.__published

    @property
    def pages(self):
        return self.__pages

    @property
    def language(self):
        return self.__language
    
    @title.setter
    def title(self,new_title):
        self.__title=new_title

    @author.setter
    def author(self,new_author):
        self.__author=new_author

    @publisher.setter
    def publisher(self,new_publisher):
        self.__publisher=new_publisher

    @published.setter
    def published(self,new_published):
        self.__published=new_published

    @pages.setter
    def pages(self,new_pages):
        self.__pages=new_pages

    @language.setter
    def language(self,new_language):
        self.__language=new_language
    
    def open():
        print('Book has been opened')
    
    def close():
        print('Book has been closed')

class Vehicle:
    """Vehicle class"""
    def __init__(self, manufacturer,model,year,color=''):
        self.__manufacturer=manufacturer
        self.__model=model
        self.__year=year
        self.__color=color
    
    @property
    def manufacturer(self):
        return self.__manufacturer

    @property
    def model(self):
        return self.__model
        
    @property
    def year(self):
        return self.__year
        
    @property
    def color(self):
        return self.__color

    @manufacturer.setter
    def manufacturer(self,new_manufacturer):
        self.__manufacturer=new_manufacturer

    @model.setter
    def model(self,new_model):
        self.__model=new_model
        
    @year.setter
    def year(self,new_year):
        self.__year=new_year
        
    @color.setter
    def color(self,new_color):
        self.__color=new_color
    
    def startEngine(): 
        print('Engine is started')
    
    def accelerate(): #Future directions: create a speed property that is increased or decreased with these behaviors, possibly at a max as related to the gear
        print('Increasing speed')
    
    def brake():
        print('Decreasing speed')
    
    def shiftUp(): #Future direction: Create a gear property that goes up or down by one with these behaviors
        print('Increasing gear')
    
    def shiftDown():
        print('Decreasing gear')
    
    def turnLeft():
        print('Turning left')
    
    def turnRight():
        print('Turn right')
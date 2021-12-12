Object-Oriented Programming Defined

In object-oriented programming, concepts are modeled as classes and objects. An idea is defined using a class, 
and an instance of this class is called an object. Almost everything in Python is an object, including strings, 
lists, dictionaries, and numbers. When we create a list in Python, we’re creating an object which is an instance of 
the list class, which represents the concept of a list. Classes also have attributes and methods associated with them. 
Attributes are the characteristics of the class, while methods are functions that are part of the class.





Classes and Objects in Detail

We can use the type() function to figure out what class a 
variable or value belongs to. For example, type(" ") tells us 
that this is a string class. The only attribute in this case is the 
string value, but there are a bunch of methods associated with the 
class. We've seen the upper() method, which returns the string in 
all uppercase, as well as isnumeric() which returns a boolean 
telling us whether or not the string is a number. You can use the 
dir() function to print all the attributes and methods of an object.
Each string is an instance of the string class, having the same methods of the parent class. Since the content of the string is different, the methods will return different values. You can also use the help() function on an object, which will return the documentation for the corresponding class. This will show all the methods for the class, along with parameters the methods receive, 
types of return values, and a description of the methods.








Special Methods

Instead of creating classes with empty or default values, we can set these values when we create the instance. 
This ensures that we don't miss an important value and avoids a lot of unnecessary lines of code. To do this,
we use a special method called a constructor. Below is an example of an Apple class with a constructor method defined.

>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor






When you call the name of a class, the constructor of that class is called. This constructor method is always named __init__. 
You might remember that special methods start and end with two underscore characters. 
In our example above, the constructor method takes the self variable, which represents the instance, 
as well as color and flavor parameters. These parameters are then used by the constructor method to set the values 
for the current instance. So we can now create a new instance of the Apple class and set the color and flavor values all in go:
  
 
>>> jonagold = Apple("red", "sweet")
>>> print(jonagold.color)
Red





In addition to the __init__ constructor special method, there is also the __str__ special method. 
This method allows us to define how an instance of an object will be printed when it’s passed to the print() function. 
If an object doesn’t have this special method defined, it will wind up using the default representation, 
which will print the position of the object in memory. 
Not super useful. Here is our Apple class, with the __str__ method added:
  
  
  
>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...     def __str__(self):
...         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
...




Now, when we pass an Apple object to the print function, we get a nice formatted string:


>>> jonagold = Apple("red", "sweet")
>>> print(jonagold)
This apple is red and its flavor is sweet




This apple is red and its flavor is sweet

It's good practice to think about how your class might be used and
to define a __str__ method when creating objects that you may want to print later.

















Documenting with Docstrings

The Python help function can be super helpful for easily pulling up documentation for classes and methods. 
We can call the help function on one of our classes,
which will return some basic info about the methods defined in our class:

>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...     def __str__(self):
...         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
... 
>>> help(Apple)
Help on class Apple in module __main__:

class Apple(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self, color, flavor)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __str__(self)
 |      Return str(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

  
  
  
  
  
  
  
  
  We can add documentation to our own classes, methods, and functions using docstrings. 
  A docstring is a short text explanation of what something does. You can add a docstring to a method, function, 
  or class by first defining it, then adding a description inside triple quotes. Let's take the example of this function:
  
  >>> def to_seconds(hours, minutes, seconds):
...     """Returns the amount of seconds in the given hours, minutes and seconds."""
...     return hours*3600+minutes*60+seconds
... 



We have our function called to_seconds on the first line, followed by the docstring which is indented to the right 
and wrapped in triple quotes. Last up is the function body. Now, when we call the help function on our to_seconds function,
we get a handy description of what the function does:

>>> help(to_seconds)
Help on function to_seconds in module __main__:

to_seconds(hours, minutes, seconds)
    Returns the amount of seconds in the given hours, minutes and seconds.

  
  
  
  
  Docstrings are super useful for documenting our custom classes, methods, and functions, 
  but also when working with new libraries or functions. 
  You'll be extremely grateful for docstrings when you have to work with code that someone else wrote!


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
Classes and Methods Cheat Sheet (Optional)



Classes and Methods Cheat Sheet

In the past few videos, we’ve seen how to define classes and methods in Python. Here, you’ll find a run-down of everything we’ve covered, so you can refer to it whenever you need a refresher.
Defining classes and methods

class ClassName:
    def method_name(self, other_parameters):
        body_of_method
        
        


        
        
        
Classes and Instances

    Classes define the behavior of all instances of a specific class.

    Each variable of a specific class is an instance or object.

    Objects can have attributes, which store information about the object.

    You can make objects do work by calling their methods.

    The first parameter of the methods (self) represents the current instance.

    Methods are just like functions, but they can only be used through a class.
    
    
    
    
    
    
    
Special methods

    Special methods start and end with __.

    Special methods have specific names, like __init__ for the constructor or __str__ for the conversion to string.
    
    
    
    
    
    
    
    
Documenting classes, methods and functions

    You can add documentation to classes, methods, and functions by using docstrings right after the definition. Like this:
    
    
    
class ClassName:
    """Documentation for the class."""
    def method_name(self, other_parameters):
        """Documentation for the method."""
        body_of_method
        
def function_name(parameters):
    """Documentation for the function."""
    body_of_function
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
Object Inheritance

In object-oriented programming, the concept of inheritance allows you to build relationships between objects, 
grouping together similar concepts and reducing code duplication. 
Let's create a custom Fruit class with color and flavor attributes:


>>> class Fruit:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...




5

We defined a Fruit class with a constructor for color and flavor attributes. Next, 
we'll define an Apple class along with a new Grape class,
both of which we want to inherit properties and behaviors from the Fruit class:
  
  
  >>> class Apple(Fruit):
...     pass
... 
>>> class Grape(Fruit):
...     pass
... 






In Python, we use parentheses in the class declaration to have the class inherit from the Fruit class. 
So in this example, we’re instructing our computer that both the Apple class and Grape class inherit from the Fruit class. 
This means that they both have the same constructor method which sets the color and flavor attributes. 
We can now create instances of our Apple and Grape classes:
    
    
    
    
    >>> granny_smith = Apple("green", "tart")
>>> carnelian = Grape("purple", "sweet")
>>> print(granny_smith.flavor)
tart
>>> print(carnelian.color)
purple








Inheritance allows us to define attributes or methods that are shared by all types of fruit without 
having to define them in each fruit class individually. 
We can then also define specific attributes or methods that are only relevant for a specific type of fruit. 
Let's look at another example, this time with animals:



>>> class Animal:
...     sound = ""
...     def __init__(self, name):
...         self.name = name
...     def speak(self):
...         print("{sound} I'm {name}! {sound}".format(
...             name=self.name, sound=self.sound))
... 
>>> class Piglet(Animal):
...     sound = "Oink!"
... 
>>> class Cow(Animal):
...     sound = "Moooo"
...








We defined a parent class, Animal, with two animal types inheriting from that class: Piglet and Cow. 
  The parent Animal class has an attribute to store the sound the animal makes, and the constructor class takes the name 
  that will be assigned to the instance when it's created. There is also the speak method, 
  which will print the name of the animal along with the sound it makes. We defined the Piglet and Cow classes, 
  which inherit from the Animal class, and we set the sound attributes for each animal type. 
  Now, we can create instances of our Piglet and Cow classes and have them speak:




>>> hamlet = Piglet("Hamlet")
>>> hamlet.speak()
Oink! I'm Hamlet! Oink!
... 
>>> class Cow(Animal):
...     sound = "Moooo"
... 
>>> milky = Cow("Milky White")
>>> milky.speak()
Moooo I'm Milky White! Moooo
    
  

  
 We create instances of both the Piglet and Cow class, and set the names for our instances. 
  Then we call the speak method of each instance, which results in the formatted string being printed; 
  it includes the sound the animal type makes, 
  along with the instance name we assigned.
    

  

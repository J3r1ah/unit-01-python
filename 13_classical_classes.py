"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

class Person:
   race = "hispanic"
   
   def __init__(self, name, age):
     self.name = name
     self.age = age


Jeriah = Person("Jeriah", 17)
print(Jeriah.name)
print(Jeriah.age)
print(Jeriah.race)

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
  
class Animal:
   def speak(self):
      pass

class Dog(Animal):
      def speak(self):
         return "bark"
    
      
class Cat(Animal):
      def speak(self):
         return "Meow"

my_Dog = Dog()
my_Cat = Cat()
print(f"Dog says: {my_Dog.speak()}")
print(f"Cat says: {my_Cat.speak()}")





"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
    

   







 
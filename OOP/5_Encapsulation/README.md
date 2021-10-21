# What is Encapsulation?

When working with classes and dealing with sensitive data, providing global access to all the attributes used within the program is not a good choice. Encapsulation offers a way to access the required attributes without providing the full-fledged access to any of the attributes. 

Updating, modifying, or deleting data from variables can be done through the use of methods that are defined specifically for the purpose. The benefit of using this approach to programming is improved control over the input data and better security.

# What is Encapsulation in Python?

The concept of Encapsulation is the same in all OOP languages. The difference is seen when the concepts are applied to particular languages. 

Python doesn't have any access modifiers (public or private) like Java and provides access to all variables and methods globally. 

# Methods to Control Access

## Using Single Underscore

A common Python programming convention to identify a private variable is by prefixing it with an underscore. Now, this doesn't really make any difference on the compiler side. But being a convention that programmers have picked up on, it tells other programmers that the variables or methods have to be used only within the scope of the class.

    #Use of underscore

    class Person:

        def __init__(self, name, age):

            self.name = name
            self._age = age

        def display(self):
            print(self.name)
            print(self._age)


    p1 = Person("Vasu", 28)

    # accessing using method
    p1.display()

    # accessing outside class
    print(p1.name)
    print(p1._age)
    
## Using Double underscore

If you want to make class members i.e. methods and variables private, then you should prefix them with double underscores. But python offers some sort of support to the private modifier. This mechanism is called Name mangling. With this, it is still possible to access the class members from outside it.

### Name mangling

In python, any identifier with __Var is rewritten by a python interpreter as _Classname__Var.

    #Use of double underscore

    class Person:

        def __init__(self, name, age):

            self.name = name
            self.__age = age

        def display(self):
            print(self.name)
            print(self.__age)


    p1 = Person("Vasu", 28)

    # accessing using method
    p1.display()

    # accessing outside class
    print(p1.name)
    print(p1.__age) # It will throw error as Python interpreter has internally created '_Person__age' instead of '__age' (name mangling)
    print(p1._Person__age)

    print(p1.__dict__)



# Object Oreinted Programming:
Objects are created from classes 
Class contains complete design parameters of its objects and then we can create as many objects as we want from the class.
Every thing we create in python is an object of a class 
A class is a blueprint or a template for the object
Class contains all parameters and functionalities for the objects to be created
Object created from a class is an instance of the class 
To know if an object is an instance of a particular class:
    isinstance(object, class)

**What is inside an object**:
- Properties
- Functionalities

**Class Object contains two types of informations termed as attributes of the object:**
1. Data attribute: define the state of the object, known as property
2. Function: define the behavior of the object, known as methods

**DOT NOTATION**
Attributes (Data and Functions) of the object can be accessed using dot notation
    - In Data, only object-name.name-of-data-attribute
    - In Functions, object-name.name-of-functions-attribute()
    <!-- object instantiated -->
    variable-name = Class-name(arguments)
    <!-- object initialization -->
    variable-name.attributes

Class --> 1. (Object/Instance --> (Attributes --> 1. Properties --> 2. Methods))
          2. (Class Attributes --> 1. Properties --> 2. Methods)

**Benifits of OOP:**
    Object-Focused Design
    Code Re-use
    Complex Design but simple when used

Types of methods in class:
1. Instance Method: A method connected to the instance of object of a class 
2. Class Method: A method connected to a class
3. Static Method: A method not connected to a class or instances
4. abstarct Method: A method that is redifined inside another class

*If we have any attribute at the class level we can access it within an instance of that class*
Class Raghad:
    name = "Raghad"
    skills = ["CSS","HTML","JS"]


```
class Student:
    department='Mechatronics'
    offSubjects=['Mech','LA','ES','CP-II','MOM','Proj']
    def __init__(self,fName,lName,reg):
        self.fName=fName
        self.lName=lName
        self.reg=reg
        self.email=f'{self.reg.lower()}@uet.edu.pk'
        self.courses=['Proj']
    
    def registerSubject(self,*sub):
        for s in sub:
            if s not in Student.offSubjects:
                raise ValueError(f'{s} is not offered!')
            if s in Student.offSubjects and s not in self.courses:
                self.courses.append(s)
            

## Main Program ##
std1=Student('Anwar','Ali','MCT-UET-01') 
std2=Student('Akbar','Khan','MCT-UET-02')
std3=Student('Hamza','Akhtar','MCT-UET-03')

std1.registerSubject('CP-II','MOM','MOM')
print(std1.courses)


```


Child classes can override or extend the attributes and methods of parent classes. In other words, child classes inherit all of the parent’s attributes and methods but can also specify attributes and methods that are unique to themselves.


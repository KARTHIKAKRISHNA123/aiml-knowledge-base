    # class Student:

    #     def __init__(self):
    #         print("Constructor is called")
    #     subject = "Python"
    #     college = "ABC College"
    #     year = "4th Year"

    # stu1 = Student()
    # print(stu1)
    # print(stu1.subject)
    # l1 = [1, 2, 3]
    # print(type(l1))
    # print(type(stu1))
    # s = set()
    # print(type(s))


        # class Student:
        #     College = "ABC College" # class variable
        #     PI = 3.14    # class variable of lower priority than its instance variable version


        #     def __init__(self): #default constructor
        #         print("Constructor is called")
        #     def __init__(self, name, cgpa): #parameterized constructor
        #         self.name = name # instance variable
        #         self.cgpa = cgpa
        #         self.PI = 3.14159 # instance variable of higher priority than its class variable version
        #         print("Constructor is called")
        #         # 1 latest init__ will be considered only multiple  constructors init__ not allowed 

        #     def get_cgpa(self):
        #         return self.cgpa

        # stu1 = Student("Alice", 3.8)
        # print(stu1)
        # # Example 1: Basic Class Definition and Object Creation
        # print(stu1.name)
        # print(stu1.cgpa)

        # print(f"CGPA of {stu1.name} is {stu1.get_cgpa()}")

        # print(Student.College)  # Accessing class variable without creating an object
        # print(stu1.College)    # Accessing class variable through an object


# class Laptop:
#     storage_type = "SSD"  # class variable or attribute

#     def __init__(self, RAM, storage_capacity):
#         self.RAM = RAM  # instance variable or attribute
#         self.storage_capacity = storage_capacity  # instance variable or attribute

#     def get_info(self):#instance method its first parameter is always self
#         return f"Laptop with {self.RAM} RAM and {self.storage_capacity} storage." #instance method can access instance variables and class variables or attributes
    
#     @classmethod #class method its first parameter is always cls and it is decorated with @classmethod
#     def get_storage_type(cls):
#         return f"Laptop storage type is {cls.storage_type}." #class method can access class variables or attributes only
    
#     @staticmethod
#     def calc_discounted_price(price, discount):
#         return price - (price * discount / 100) #static method cannot access instance variables or class variables
    

# lap1 = Laptop("16GB", "512GB")
# lap2 = Laptop("8GB", "1TB")
# print(lap1.get_info())  # Output: Laptop with 16GB RAM and 512GB storage.
# print(lap2.get_info())  # Output: Laptop with 8GB RAM and
# print(lap1.calc_discounted_price(100000, 10))


# class Product:
#     count = 0  # class variable to keep track of number of products

#     def __init__ (self, name, price):
#         self.name = name
#         self.price = price
#         Product.count += 1

#     @staticmethod
#     def apply_discount(price , discount_percentage):
#         discount_amount = price * (discount_percentage / 100)
#         return price - discount_amount
    
#     @classmethod
#     def get_product_count(cls):
#         return f"Total products created: {cls.count}"
    
# product1 = Product("Laptop", 1000)
# discounted_price = Product.apply_discount(product1.price, 10)
# print(f"Discounted price of {product1.name} is {discounted_price}")
# print(f"Total products created: {Product.count}")
# print(Product.get_product_count())



# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         #self._balance = balance  # Protected attribute but still accessible outside the class
#         self.__balance = balance  # Private attribute but still accessible outside the class with name mangling

#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self, new_balance):
#         if new_balance >= 0:
#             self.__balance = new_balance
#         else:
#             print("Balance cannot be negative.")

# account = BankAccount("John Doe", 1000)
# #print(account.__balance)  # This will raise an AttributeError
# print(account.get_balance())  # Accessing balance using getter method
# account.set_balance(1500)  # Updating balance using setter method
# print(account.name, account._BankAccount__balance)  # Accessing private attribute using name mangling


    # class Employee:
    #     start_time = "9 AM"  # class variable
    #     end_time = "5 PM"    # class variable

    #     def change_time(self, new_end_time):
    #         self.end_time = new_end_time  # instance variable
        
    # class Teacher(Employee):
    #         def __init__(self, subject):
    #             self.subject = subject

    # class AdminStaff(Employee):
    #      def __init__(self, role):
    #             self.role = role
        
    # t1 = Teacher("Mathematics")
    # t1.change_time("6 PM")
    # print(f"Teacher's subject: {t1.subject}")
    # print(t1.subject, t1.start_time, t1.end_time)
    # staff1 = AdminStaff("Manager")
    # print(staff1.role, staff1.start_time, staff1.end_time)

#Multi Level Inheritance

        # class Teacher:

        #     def __init__(self, salary):
        #         self.salary = salary
            
        # class Student:
        #     def __init__(self, gpa):
        #         self.gpa = gpa

        # class TA(Teacher, Student):
        #     def __init__(self, salary, gpa, name):
        #         super().__init__(salary)
        #         Student.__init__(self, gpa)
        #         self.name = name

        # ta1 = TA(15_000, 9.3, "Shraddha")

        # print(ta1.name, ta1.gpa, ta1.salary)


# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Lion(Animal):
#     def make_sound(self):
#         return "Roar"

# class Cow(Animal):
#     def make_sound(self):
#         return "Moo"

# lion = Lion()
# lion.make_sound()  # Output: "Roar"


# cow = Cow()
# cow.make_sound()  # Output: "Moo"

#Polymorphism - overriding

    # from typing import override


    # print(1 + 2, "Hello" + " World")

    # class Employee:
    #     def get_designation(self):
    #         print("designation = employee")
        
    # class Teacher(Employee):
    #     @override
    #     def get_designation(self):
    #         print("designation = teacher")

    # t1 = Teacher()
    # t1.get_designation()

#polymorphism - ducktyping
class Teacher():
    def get_designation(self):
        print("designation = teacher")

class Accountant():
    def get_designation(self):
        print("designation = accountant")

t1 = Teacher()
t1.get_designation()
a1 = Accountant()
a1.get_designation()

# when both classes have method which walks like a duck and quacks like a duck then it is called ducktyping
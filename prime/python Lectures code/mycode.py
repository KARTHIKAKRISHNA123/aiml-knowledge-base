# print("Hello, World!")

# _name = "KK"
# _age = 20
# PI = 3.14 
# Partner = None

# print(_name, _age, PI)

# print(type(_name))
# print(type(_age))
# print(type(PI))
# print(type(Partner))

# ''' 
# Three single quotes for multi-line comments
# '''

# tot_price = 100
# full_name = "Karthika Krishna M"

# num1 = 1
# num2 = 3
# print("The sum of two numbers is:", num1 + num2)

# a = 10 
# b = 5
# print(a / b)  # Division
# print(a // b) # Floor Division
# print("IN division there is an implicit conversion to float")
# print("In floor division the decimal part is removed")

# ans1 = int(5 + 10.0) # Explicit conversion to int which is Type Casting
# ans2 = 5 + 10.0 # Implicit conversion to float which is Type Conversion


# c = float(input("Enter first number: "))
# d = float(input("Enter second number: "))
# print("The sum of two numbers is:", c + d)
# print("The Average of two numbers is:", (c + d) / 2)

# a = input("Enter your name: ")
# b = int (input("Enter your age: "))
# print('Hi', a, ', You are', b, 'years old.')

# a = int (input ("Enter an integer: "))
# b = int (input ("Enter another integer: "))
# c = float (input ("Enter a float: "))
# d = float(a) + float(b) + c
# print("The average is:", d / 3) 



# a = input("Enter a string containing numbers: ")
# print(int(a), type(int(a)))
# print(float(a), type(float(a)))
# print("\"",str(a),"\"", type(str(a)))

# x = 10 + 3 * 2 ** 2 #22
# print(x) 
# follows pemdas and bodmas rules

# a = int (input ("Enter an integer: "))
# b = int (input ("Enter another integer: "))

# temp = a
# a = b
# b = temp
# print("After swapping: a =", a, ", b =", b)


# a = int (input ("Enter temperature in Celsius: "))
# b = float (a)
# c = (b * (9 / 5)) + 32
# print("Temperature in Fahrenheit is:", c)

# a = int (input ("Enter the radius of the circle: "))
# PI = 3.14
# area = PI * a * a
# print("The area of the circle is:", area)

# a = float (input ("Enter the principal amount: "))
# r = float (input ("Enter the rate of interest: "))
# t = float (input ("Enter the time in years: "))

# SI = (a * r * t) / 100
# print("The Simple Interest is:", SI)


# a = float (input ("Enter a decimal number: "))
# print("The integer value is:", a // 1)
# print("The decimal part is:", a % 1)
# print("The decimal part rounded to nearest integer is:", round(a % 1))




# a = float (input ("Enter a decimal number: "))
# print("The integer part is:", int(a))
# print("The fractional part is: ", format(a - int(a), '.2f')[:3])


# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")
#     print("You can drive a car.")

# else: 
#     print("You cannot vote yet.")


# color = input("Enter the color:") 
# if color == "red":
#     print("Stop")
# elif color == "yellow":
#     print("Get Ready")
# elif color == "green":
#     print("Go")
# else:
#     print("Invalid Color")


# match color: 
#     case "red":
#         print("stop")
#     case "Yellow":
#         print("wait")
#     case "Green": 
#         print("Go")
#     case _:
#         print("Wrong colour")


# n = int(input("Enter table number: "))
# i = int(input("Enter times number: "))

# j = 1

# while j <= i:
#     print(n, "x", j, "=", n * j)
#     j += 1  


# string = "Hello, World!"

# for char in string:
#     print(char)

# if 'W' in string:
#     print("Yes, 'W' is present in the string.")

# i = 1
# while i <= 10:
#     if (i % 2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1


# word = "Artificial Intelligence"
# i = 0

# for letter in word:
#     if letter == "i" or letter == "I":
#         i += 1
        
# print("Number of Is in the word:", i)


# def calc_avg(num1, num2, num3):
#     total = num1 + num2 + num3
#     avg = total / 3
#     return avg  

# print("The average is:", calc_avg(10, 20, 30))

# def sum(a, b = 1):
#     return a + b

# print(sum(70))

# sum = lambda a, b, c: a * b + c
# print("The result is:", sum(5, 10, 2))

# fact = 1
# for i in range (1, 5 + 1):
#     fact = fact * i
# print("The factorial is:", fact)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print("The factorial is:", factorial(5))

# salary = float(input("Enter your salary: "))

# if salary < 30000:
#     print("Your tax rate is 5%")
# elif salary >= 30000 and salary < 70000:
#     print("Your tax rate is 15%")
# else:
#     print("Your tax rate is 25%")


# def even_num(a, b):

#     for num in range(a, b + 1):
#         if num % 2 == 0:
#             print(num)

# even_num(1, 20)


# def digits(num):
#     sum = 0
#     while num > 0:
#         digit = num % 10
#         print(digit)
#         sum += digit
#         num = num // 10
    
#     return sum

# print(digits(12345)) 



# def digits(num):
#     digits_list = []
#     while num > 0:
#         digit = num % 10
#         digits_list.append(digit)
#         num = num // 10
#     for digit in reversed(digits_list):
#         print(digit)


# def num_digits(num):
#     count = 0
#     while num > 0:
#         count += 1
#         num = num // 10 
#     print("The number of digits is:", count) 


# num_digits(12345)


# for i in range(1, 101) :
#     if i % 3 == 0 and i % 5 == 0:
#         print("divisible by 3 and 5 both -FIZZBUZZ", i)
#     elif i % 3 == 0:
#         print("Fizz - divisible by 3", i)
#     elif i % 5 == 0:
#         print("Buzz - divisible by 5", i)
#     else:
#         print(i)


# print("Enter Quit to exit")

# while True: 
#     num1 = input("Enter a number: ")
#     if num1 == "Quit": 
#         break
#     num2 = input("Enter another number: ")
#     if num2 == "Quit":
#         break
#     print("The sum is:", int(num1) + int(num2))


# def calculator (a, b, operation):
#     if operation == "+":
#         return a + b
#     elif operation == "-":
#         return a - b
#     elif operation == "*":
#         return a * b
#     elif operation == "/":
#         return a / b
#     else:
#         return "Invalid operation"



# print(calculator(10, 5, "+"))
# print(calculator(10, 5, "-"))
# print(calculator(10, 5, "*"))
# print(calculator(10, 5, "/"))

# a = int (input ("Enter an integer: "))
# b = int (input ("Enter another integer: "))
# c = input ("Enter an operator ( +, -, *, /): ")

# print(calculator(a, b, c))


# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# print(is_prime(12))

# SECRET = 777

# while True:
#     n = int(input("Enter a number to guess the secret number: "))

#     if n == SECRET:
#         print("You win")
#         break
#     elif n < SECRET:
#         print("Too low")
#     else:
#         print("Too high")


# word1 = "I Love"
# word2 = "Python"

# print(word1 + " " + word2)
# print(len(word1))

# print(word1[2])
# print(word1[2:5])
# print(word1[:5])
# print(word1[2:])
# print(word1[-1])
# print(word1[-3:-1])

# for char in word2:
#     print(char)

# word1[3] = 'a' # This will raise an error because strings are immutable


# word = "I study Artificial Intelligence"
# print(word.lower())
# print(word.upper())
# print(word.replace("Artificial", "Machine"))
# print(word.split(" "))
# print("Number of characters in the string:", len(word))
# print("Index of 'Artificial':", word.index("Artificial"))
# print(word[8:])
# print(word[::-1])
# print(word.strip())
# print(word.count("i"))
# print(word.startswith("I"))
# print(word.endswith("Intelligence"))
# print(word.find("study"))
# print(word.capitalize())
# print(word.title())
# print(word.isalpha())
# print(word.isdigit())
# print(word.swapcase())
# print(" ".join(["I", "love", "Python"]))
# print(word.center(50))
# print(word[8:len(word)])
# word2 = "Python"
# print(word2[-4:-2]) 

# a = 5
# b = 10
# sum = a + b
# print("The sum of", a, "and", b, "is:", sum) 
# print("The sum of {} and {} is: {}".format(a, b, sum))

# print(f"The sum of {a} and {b} is: {sum}")

# print("The values of a and b are {a} and {b} and their values can be reused {b}".format(a = 12, b = 15))
# print(f"The values of a and b are {a} and {b} and sum is {a + b} and their average is {(a + b) / 2}")

#Strings are immutable as in java.
#Lists are mutable . It is ordered and allows duplicate elements and they are classes and have methods
#Tuples are immutable and they are ordered and allow duplicate elements and they are classes and have methods
#Dictionaries are mutable and they are unordered and do not allow duplicate keys
#Sets are mutable and they are unordered and do not allow duplicate elements

# marks = [85, 90, 78, 92, 88, "A"]
# print(marks)
# marks[2] = 80
# print(marks)

# # List can store different data types

# print(type(marks))

# # When we do slicing the original list remains unchanged
# # When we do slicing in list sublist is created similar to substring in strings
# print(marks[1:4])
# print(marks[:3])
# print(marks[-4: -2])  

# list = [1, 2, 3, 4, 5]
# list.append(6)
# print(list)
# list.insert(2, 20)
# list.sort()
# list.sort(reverse = True)
# print(list)
# list.reverse()
# print(list)
# idx = 0
# for item in list:
#     if item == 3:
#         print(f"index of 3 is {idx}")
#         break
#     idx += 1


# tup = (10, 20, 20, 30, 40, 50)

# # tup[2] = 35
# # This will raise an error because tuples are immutable
# print(tup)

# print(type(tup))
# tup1 = (1)
# print(type(tup1))  # This will be of type int considering single value without comma as math expression
# tup2 = (1,)
# print(type(tup2))  # This will be of type tuple
# # Slicing works similar to lists and strings and everything else similar to lists
# sum = 0
# for item in tup:
#     sum += item
# print("The sum is:", sum)
# print("The count of 20 is:", tup.count(20))
# print("The first ocurrence of 20 at index of 20 is:", tup.index(20))

# info = {
#     "name": "Karthika Krishna M",
#     "age": 20,
#     "city": "Alangulam",
#     "is_student": True,
#     "grades": [80, 90, 75],
#     "subjects": ["Math", "Science", "English"],
#     "cgpa": 8.5,
#     3.14: "Pi Value"



# }

# print(info)
# print(type(info))
# print("Name:", info["name"])
# print("Age:", info["age"])
# print("City:", info["city"])
# print("Is Student:", info["is_student"])
# print("Grades:", info["grades"])
# print("Subjects:", info["subjects"])
# print("CGPA:", info["cgpa"])
# print("Pi Value:", info[3.14])
# info["age"] = 21
# print("Updated Age:", info["age"])
# print("Keys:", info.keys())
# print("Values:", info.values()) 
# print("Items:", info.items())

# dict_keys = list(info.keys())
# print(type(dict_keys))
# print(info.get("cgpa")) # returns None if key not found but info["key"] raises error the lines after this will not be executed
# print(info.get("country", "Not Found")) # returns default value if key not found

# info.update({"country": "India"})

# s = {1, 2, 3, 3, 3}

# print(len(s))
# s.add(5)
# empty_set1 = {} # This creates an empty dictionary not set
# empty_set2 = set() # This creates an empty set
# print(type(empty_set1))
# print(type(empty_set2))
# s.add(5)
# s.remove(2)
# s.discard(10) # does not raise error if element not found
# #s.clear()
# print(s)
# s.pop() # removes an arbitrary element
# print(s)

# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}

# print("Union:", s1 | s2)
# print("Intersection:", s1 & s2)
# print("Difference:", s1 - s2)
# print("Symmetric Difference:", s1 ^ s2) #xor for sets prints elements not in both sets

# print(s1.intersection(s2))
# print(s1.union(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
# print(s1.isdisjoint(s2))
# print(s1.issubset(s2))
# print(s1.issuperset(s2))

#Practice Problems
#1
# info = [
#     ("Karthika", " Science",),
#     ("Arun", "Mathematics"),
#     ("Meena", "Science"),
#     ("Karthika", "Mathematics"),
#     ("Arun", "Science"),
#     ("Meena", "Mathematics"),
#     ("Karthika", "English"),
#     ("Arun", "English"),
#     ("Meena", "English"),

# ]

# unique_courses = set()


# for tup in info:
#     #print(tup) #prints each tuple
#     #print(tup[0]) #prints only names
#     #print(tup[1]) #prints only subjects
#     unique_courses.add(tup[1])

# print("Unique courses offered are:", unique_courses)

# for name, course in info:
#     if course == "Science":
#         print(f"{name} is enrolled in Science")
#     unique_courses.add(course)

# print("Unique courses offered are:", unique_courses)

# info2 = dict()

# for name, course in info:
#     if (info2.get(name) == None):
#         info2.update({name: set()})
#         info2.get(name).add(course)
#     else:
#         info2.get(name).add(course)

# print(info2)

#Assignment Problems

#1
# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     return s == s[::-1]

# print(is_palindrome("Madam"))
# print(is_palindrome("race car"))

#2
# list = [10, 23, 45, 70, 11, 3, 5, 8, 13]
# sum = 0

# for val in list: 
#     sum += val

# print("The sum of all elements in the list is:", sum)
# avg = sum / len(list)
# print("The average of the elements in the list is:", avg) 

#3
# list1 = [1, 2, 3]
# list2 = [2, 4, 5]

# list = list1 + list2
# list.sort()
# print(list)

#4
# tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# even = ()
# odd = ()

# for val in tuple:
#     if val % 2 == 0:
#         even += (val,)
#     else:
#         odd += (val,)

# print(even) 
# print(odd)

#5
# def main(): 
#     student_data = {}

#     while True:
#         print("Student Management System")
#         print("A - Add Student")
#         print("B - Update student marks")
#         print("C - Search Student")
#         print("D - Display all students")
#         print("E - Exit")

#         choice = input("Enter your choice: ").upper()

#         if choice == "A":
#             name = input("enter student name:  ")
#             marks = float(input("enter student marks: "))
#             student_data[name] = marks
#             print(f"Student {name} and his/her marks {marks}  added successfully.")
#         elif choice == "B":
#             name = input("enter student name to update marks:  ")
#             if name in student_data:
#                 marks = float(input("Enter new marks: "))
#                 student_data[name] = marks
#                 print(f"Marks for student {name} updated successfully.")
#             else:
#                 print(f"Student {name} not found.")
#         elif choice == "C":
#             name = input("enter student name to search:  ")
#             if name in student_data:
#                 print(f"Student: {name}, Marks: {student_data[name]}")
#             else:
#                 print(f"Student {name} not found.")
#         elif choice == "D":
#             if student_data:
#                 for name, marks in student_data.items():
#                     print(f"Student: {name}, Marks: {marks}")
#             else:
#                 print("No student data available.")
#         elif choice == "E":
#             print("Exiting Student Management System.")
#             break
#         else:
#             print("Invalid choice. Please try again.")  

# if __name__ == "__main__":
#     main()

#6

# words =["apple","banana","kiwi","cherry","mango"]
# dict_lengths = {}

# for word in words:
#     dict_lengths[word] = len(word)
# print(dict_lengths)

#7
# str = input("Enter a string: ")
# i = 0
# for char in str:
#     if char == ' ':
#         i += 1
# print("Number of spaces in the string:", i)

#8
# set1 = [1, 2, 3, 4]
# set2 = [5, 6, 7, 8]
# set1 = set(set1)
# set2 = set(set2)

# if set1.intersection(set2):
#     print("lists have common elements")
# else:
#     print("lists have no common elements")

# set3 = [1, 2, 3]
# set4 = [3, 4]
# set3 = set(set3)
# set4 = set(set4)

# if set3.intersection(set4):
#     print("lists have common elements")
# else:
#     print("lists have no common elements")

#9
    # def find_duplicates(list):
    #     seen = set()
    #     duplicates = set()

    #     for item in list:
    #         if item in seen:
    #             duplicates.add(item)
    #         else:
    #             seen.add(item)
        
    #     print("Seen items:", seen)
    #     print("Duplicates:", duplicates)
    #     print("Original list:", list)

    # print(find_duplicates([1, 2, 3, 4, 2, 5, 3, 6]))
    # print(find_duplicates(['apple', 'banana', 'kiwi', 'apple', 'cherry', 'banana']))

#10
str = input("Enter a string: ")
seen = set()
duplicates = set()

for char in str:
    if char in seen:
        duplicates.add(char)
    else:
        seen.add(char)

print("Seen characters:", seen)
print("Duplicate characters:", duplicates)
print("Unique characters:", seen - duplicates)
print("Length of the unique characters set:", len(seen - duplicates))
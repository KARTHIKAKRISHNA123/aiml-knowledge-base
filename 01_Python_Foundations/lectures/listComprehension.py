# squares = []

# for i in range(6):
#     squares += [i * i]

# print(squares)

# List Comprehension = [output for iterable in item if condition]

sq = [i * i for i in range(6)]
sq2 = [i * i for i in range(6) if i % 2 == 1]
print(sq2)

nums = [-1 , -2, -3, -4, -5, 8, 9]
nums = [0 if i < 0 else i for i in nums] 
print(nums)

words = ["apple", "banana", "kiwi", "cherry", "mango"]
words = [val.upper() for val in words]
print(words)
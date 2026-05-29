# f = open("sample.txt", "a")
# # data = f.read()
# # data_in_first_line = f.readline()
# # print(data)
# # print(data_in_first_line)
# # print(type(data))
# f.write("\n Hello World to overwrite the file")

# f.close()

# f = open("Sample2.txt", "w+")
# data = f.read()
# print(data) # Prints original content

# f.write("\n Hello from KK to this file")

# # FIX: Move the cursor back to the start (0th position)
# f.seek(0) 

# data2 = f.read()
# print(data2) # Now this will print everything, including the new line
# f.close() 

# f = open("Sample2.txt", "r+")
# data = f.read()
# print(data) # Prints original content

# f.write("\n Hello from KK to this file")

# # FIX: Move the cursor back to the start (0th position)
# f.seek(0) 

# data2 = f.read()
# print(data2) # Now this will print everything, including the new line
# f.close()


# f = open("Sample2.txt", "a+")
# data = f.read()
# print(data) # Prints original content

# f.write("\n Hello from KK to this file")

# # FIX: Move the cursor back to the start (0th position)
# f.seek(0) 

# data2 = f.read()
# print(data2) # Now this will print everything, including the new line
# f.close()


# with open("Sample.txt" , "r") as f: #No need of explicitly close
#     data = f.read()
#     print(len(data))

# import os

# os.remove("Sample2.txt")

data = True
line = 1

with open("Sample.txt" , "r") as f: #No need of explicitly close
    while data:
        data = f.readline()
        if "python" in data:
            print(f"python found in line {line}")
        line += 1
        print(data)
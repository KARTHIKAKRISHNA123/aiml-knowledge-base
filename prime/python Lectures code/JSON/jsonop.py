import json

# json_str = '{"name": "KK", "isTeacher": false, "address" : {"city" : "Delhi", "country" : "India"}, "subjects" : ["Python", "AI/ML"]}'
# print(type(json_str))
# print(json_str)

# py_obj = json.loads(json_str)
# print(type(py_obj))
# print(py_obj)

# json_str = json.dumps(py_obj)
# print(type(json_str))
# print(json_str) 

# with open ("data.json", "r") as f:
#     py_obj = json.load(f)
#     print(type(py_obj))

data = {
    "name" : "Shraddha",
    "age" : 27,
    "isTeacher" : True
}

with open ("data2.json", "w") as f:
    json.dump(data, f, indent = 4, sort_keys=True)

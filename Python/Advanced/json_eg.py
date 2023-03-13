import json
print("-----------json to dict------------------")


x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(type(y))

print("-----------dict to json------------------")

z={"name":True, "age":False, "city":None}
print(z)
print(type(z))
p=json.dumps(z)
print(p)
print("-----------------------------")

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
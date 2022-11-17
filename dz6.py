result = []

def divider(a, b):

   try:
      if a < b:
          raise ValueError
   except:
       print("Value Error")

   try:
      if b > 100:
          raise IndexError
   except:
       print ("Index Error")
   try:
      return a/b
   except:
       print("Index Error")

data = {10: 2, 2: 5, "123": 4, "[]": 15, 18: 0, 8 : 4}

print([cls.__name__ for cls in Exception.__subclasses__()])

for key in data:
       res = divider(key, data[key])
       result.append(res)

print(result)
def my_function(x, y):
    a = x + y
    b = x - y
    return a, b

var1, var2 = my_function(10, 20)


print(my_function(10, 20))


import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")

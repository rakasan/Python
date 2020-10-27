"""
Just an application that calculates the area
"""

print("We are live!!")

shape = raw_input("Enter C for Circle or T for Triangle: ")
if(shape == 'C'):
  radius = float(raw_input("Give me a radius "))
  area = radius **2 *3.14159
  print(area)
elif(shape == 'T'):
  base = float(raw_input("Give me the base "))
  height = float(raw_input("Give me the height "))
  area = base / 2 * height
  print(area)
else:
  print("Exiting as no valid condition was selected")
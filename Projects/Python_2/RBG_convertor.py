def convert():
  choice = True
  while(choice):
    option = raw_input("nter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:")
    if(option == "1"):
      print("RGB to Hex...")
      rgb_hex()
    elif(option == "2"):
      print("Hex to RBG...")
      hex_rbg()
    elif(option == 'X'):
      choice = False
    else:
      print("Wrong choice")
      choice = False
    

def rgb_hex():
  invalid_msg = "Invalid values are entered"
  red = int(raw_input("Red :"))
  if((red > 255) or (red < 0)):
    print(invalid_msg) 
    return 
  green = int(raw_input("Green :"))
  if((green > 255) or (green < 0)):
    print(invalid_msg) 
    return 
  blue = int(raw_input("Blue :"))
  if((green > 255) or (green < 0)):
    print(invalid_msg) 
    return 
  var = red << 16 + green << 8 + blue
  print(hex(var)[2:].upper())
 
def hex_rbg():
  hex_val = raw_input("Give me the hex value ")
  if(len(hex_val) != 6):
    print("Invalid hex value")
    return
  else:
    hex_val = int(hex_val, 16)
  two_hex_digits = 2**8
  blue = hex_val % two_hex_digits

  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits

  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print "The hex code is Red %s Green %s Blue %s " % (red,green,blue)

convert()
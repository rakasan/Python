# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  type = get_drink_type()
  print("Alright, that's a "+size+" "+type)
  name = input("Can I get your name please")
  print("Thanks "+name+"! Your drink will be ready shortly.")
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>')
  if res == 'a':
    returnValue = "coffee"
  elif res =='b':
    returnValue = "mocha"
  elif res == 'c':
    returnValue = order_latte()
  else :
   print_message() 
   return get_drink_type()

  return returnValue

def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>')
  if res == 'a':
    returnValue = "latte"
  elif res =='b':
    returnValue = "non-fat latte"
  elif res == 'c':
    returnValue = "soy latte"
  else :
   print_message() 
   return order_latte()

  return returnValue

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    returnValue = "small"
  elif res =='b':
    returnValue = "medium"
  elif res == 'c':
    returnValue = "Large"
  else :
   print_message() 
   return get_size()

  return returnValue

# Call coffee_bot()!
coffee_bot()

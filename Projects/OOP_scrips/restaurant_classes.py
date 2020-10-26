class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises
  
class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return "{} menu available from {} to {}".format(self.name,self.start_time,self.end_time)
  def calculate_bill(self,purchased_items):
    summ = 0
    for element in purchased_items:
      if element in self.items:
        summ +=self.items.get(element)
    return summ


class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self,time):
    returnList = []
    for element in self.menus:
   #   print(str(time) + " " + str(element.start_time) + " " + str(element.end_time))
      if (time > element.start_time) and (time < element.end_time):
        returnList.append(element.name)
    return returnList

brunch = Menu("brunch",{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
},1100,1600)

early_bird = Menu("early_bird",{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
},1500,1800)

dinner = Menu("dinner",{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
},1700,2300)

kids = Menu("kids",{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
},1100,2100)

flagship_store = Franchise("1232 West End Road",[brunch,early_bird,dinner,kids])

new_installment = Franchise("12 East Mulberry Street",[brunch,early_bird,dinner,kids])

NewBussiness = Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])

#print(new_installment.available_menus(1200))
#print(kids.calculate_bill(['apple juice']))
class BankAccount(object):
  balace = 0
  def __init__(self,name):
    self.name = name
  def __ref__(self):
    return "This account belongs to %s and has %s" % (self.name,self.balance)
  def show_balance(self):
    print "The balance is %s.2f" % self.name
  def deposit(self,amount):
    if(amount <= 10):
      print("The amount you want to deposit is to low")
      return
    else:
      print "You currently have %s.2f" % self.balance
      self.balance +=amount
      self.show_balance()
    def withdraw(self,amount):
      if(amount > self.balance):
        print "You do not have enough money"
        return
      else:
        print "You are withdrawing %s.2f" % amount
        self.balance -= amount
        self.show_balance()
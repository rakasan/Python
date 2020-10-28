"""
Command Line Calendar
version 0.1
"""

from time import sleep,strftime

USERNAME = "Vlad"
calendar = {}
def start_calendar():
  welcome()
  start = True
  while(start == True):
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit ")
    user_choice.upper()
    if(user_choice == 'V'):
      if(len(calendar.keys()) <1):
        print("There are no entries")
      else:
        print(calendar)
    elif(user_choice == 'U'):
      date = raw_input("What Date")
      update = raw_input("Enter the update")
      calendar[date] = update
      print(calendar)
    elif(user_choice == "A"):
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print("Date input is wrong")
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if(try_again == "Y"):
          continue
        else:
          start = False
      else:
        calendar[date] = event
    elif(user_choice == 'D'):
      if(len(calendar.keys()) <1):
        print("Nothing to delete")
      else:
        event = raw_input("What event: ")
        for date in calendar.keys():
          if(calendar[date] == event):
            print("Event was deteled")
            del calendar[date]

    if(user_choice == 'X'):
      start = False

def welcome():
  print "welcome %s"% USERNAME
  print "Calendar is opening ..."
  sleep(1)
  print("Today is: "+ strftime("%A %B %d %Y"))
  print(strftime("%H %M %S"))
  sleep(1)
  print("What would you like to do ?")

start_calendar()
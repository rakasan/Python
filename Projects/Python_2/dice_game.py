"""
Roll Dice Game
Version 0.1

"""
from random import randint
from time import sleep


def get_user_guess():
  userChoice = int(raw_input("What is your guess "))
  return userChoice

def roll_dice(number_of_sides):
 # rand = randrange(number_of_sides)
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)

  max_val = 2 * number_of_sides
  print " The maximum possible value is %d " %max_val

  guess =get_user_guess()

  if(guess > max_val):
    print("You choose a value which exceeds the max allowed value")
  else:
    total_roll = first_roll + second_roll
    print("Rolling...")
    sleep(2)
    print "First roll %d"%first_roll
    sleep(1)
    print "Second roll %d"%second_roll
    print("Result ....")
    sleep(1)
    if(guess == total_roll):
      print("You were right")
    else:
      print("Try again")
roll_dice(6)
import random
from art import logo

print(logo)
print("Welcome to the number guessing game!\nI'm thinking of a number from 1 to 100")
level = input("Choose a difficulty level. Type easy or hard : ")

def compare(guess, attempt):
  """Compares the guess and the no chosen by the computer"""
  if int(guess) > no:
    print("Too high")
  elif int(guess) < no:
    print("Too low")
  elif int(guess) == no:
   print(f"You got it! The answer was {guess}")
   exit()
  elif attempt == 0:
    print("You ran out of guesses! Better luck next time!")

def make_a_guess(attempt):
  """Keeps track of attempt and prints the guesses"""""
  while(attempt > 0):
    print(f"You have {attempt} attempts remaining to guess the no")
    guess = input("Make a guess: ")
    return guess

no = random.randint(1,100)

if level == "easy":
  attempt = 10
  while attempt != 0:
    guess = make_a_guess(attempt)
    compare(guess, attempt)
    attempt -= 1

elif level == "hard":
  attempt = 5
  while attempt != 0:
    guess = make_a_guess(attempt)
    compare(guess, attempt)
    attempt -= 1

else:
  print("Invalid difficulty level. Please choose easy or hard")

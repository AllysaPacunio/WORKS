import random
import time

random.seed(time.time())
secret = random.randint(1, 10)
guessed = False

chances = 3
print("You have" ,chances, "chances! Ready! Go!")

print("\n")
print(secret)

while chances:
  guess = int(input("Input Guess: "))

  if guess > int(secret):
    print("Your guess is too high.")
    chances -= 1
    print("\n")
    
    if chances:
      print(f"You have" ,chances, "more chance(s)! Go for it!")
      print("\n")
  
  elif guess < int(secret):
    print("Your guess is too low.")
    chances -= 1
    
    if chances:
      print(f"You have" ,chances, "more chance(s)! Go for it!")
  
  else :
    print("Wow! you're great!")
    guessed= True
    break
  
if not guessed:
	print("Better luck next time!")



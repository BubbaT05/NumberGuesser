import random

playAgain = "Y"
secret = random.randint(1,10)
numGuess = 0
history = []

while playAgain == "Y":
  guess = int(input("Guess a number: "))
  numGuess += 1
  if guess == secret:
    print("That's Right! You Got It In", numGuess)
    playAgain = input("Play Again? ")
    secret = random.randint(1,10)
    history.append(numGuess)
    numGuess = 0
  elif guess > secret:
    print("Too High!")
  else:
    print("Too Low!")
  
for i in range(0, len(history)):
  print(f"Game {i+1}: {history[i]}")
print("Average: ", "{:.2f}".format(sum(history) / len(history)))
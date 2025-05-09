# Write code below 💖
  
import random

print("====================")
print("Rock Paper Scissors")
print("====================")
print("1) ✊")
print("2) 🤚")
print("3) ✌")
print("4) 🦎")
print("5) 🖖")

player = int(input("Pick a number: "))
CPU = random.randint(1, 5)

options = ["✊", "🤚", "✌", "🦎", "🖖"]
print(f"You chose: {options[player - 1]}")
print(f"CPU chose: {options[CPU - 1]}")

wins_against = {
  1: [3, 4],
  2: [1, 5],
  3: [2, 4],
  4: [2, 5],
  5: [1, 3]
}

if player == CPU:
  print("IT'S A TIE")
elif CPU in wins_against[player]:
  print("YOU WIN 🎉🥳")
else:
  print("CPU WINS 😢")

import random

energy = 100
hp = 100

print("you have been knocked out and are in a empty room")
ans1 = input('''what do you do?
a. cry
b. open the door
c. look for the lights''')

if ans1 = "a":
  energy-=1
  print("you cry and lose 1 energy. energy: " + energy)

if ans1 = "b":
  energy-=15
  print("you open the door and lose 15 energy. energy: " + energy)

if ans1 = "c":
  energy-=50
  hp-=15
  print("you try to find the lights and trip on someone's pookie bear. energy: " + energy + "health: " + hp)

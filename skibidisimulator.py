import random

energy = 100
hp = 100

print("you have been knocked out and are in a empty room")
ans1 = input('''what do you do?
a. cry
b. open the door
c. look for the lights''')

if ans1 == "a":
  energy=-1
  textenergy = energy
  print("you cry and lose 1 energy. energy: " + textenergy)

if ans1 == "b":
  energy=-15
  textenergy = energy
  print("you open the door and lose 15 energy. energy: " + textenergy)

if ans1 == "c":
  energy=-50
  textenergy = energy
  hp=-15
  texthp = hp
  print("you try to find the lights and trip on someone's pookie bear. energy: " + textenergy + "health: " + texthp)

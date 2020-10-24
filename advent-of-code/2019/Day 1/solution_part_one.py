import math

input = open('advent-of-code/2019/Day 1/input.txt', 'r').read().split('\n')

def strToInt(string):
  return int(string)

modules_mass = list(map(strToInt, input))

sum = 0
for mass in modules_mass:
  sum += math.floor(mass / 3) - 2

print(sum)
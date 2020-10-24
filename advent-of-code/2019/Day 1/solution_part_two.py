import math

input = open('advent-of-code/2019/Day 1/input.txt', 'r').read().split('\n')

def strToInt(string):
  return int(string)

def calcFuel(mass):
  return math.floor(mass / 3) - 2

modules_mass = list(map(strToInt, input))

sum = 0
for mass in modules_mass:
  fuel_needed = calcFuel(mass)
  while (fuel_needed > 0):
    sum += fuel_needed
    fuel_needed = calcFuel(fuel_needed)

print(sum)
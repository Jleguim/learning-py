# Given a list of numbers and a number k, 
# return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true 
# since 10 + 7 is 17.

def adds_up(n, ln):
  verdict = 0
  for x in ln:
    for y in ln:
      if (x + y == n):
        verdict = 1
  return verdict

does_it = adds_up(17, [10, 15, 3, 7])
print(does_it)
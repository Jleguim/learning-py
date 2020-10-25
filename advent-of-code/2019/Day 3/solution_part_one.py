def distance(vector1, vector2):
  return (abs(vector1['x'] - vector2['x']) + abs(vector1['y'] - vector2['y']))

# There might be a library for this, but it gets the job done.
def vector(x = 1, y = 1):
  return { 'x': x, 'y': y }

def addVector(vector1, vector2):
  return vector(vector1['x'] + vector2['x'], vector1['y'] + vector2['y'])

# This "algorithm" is way too slow for the puzzle input we are provided with.
# Might have to look into an actual algorithm to finish this part of the puzzle.
def find_collisions(vector_list1, vector_list2):
  collisions = []
  for vector1 in vector_list1:
    for vector2 in vector_list2:
      print(vector1, vector2)
      if (vector1 == vector2):
        collisions.append(vector(vector1['x'], vector1['y']))
  return collisions

def find_nearest(vector_point, vector_list):
  distances = []
  for vector_ in vector_list:
    dist_between = distance(vector_, vector_point)
    if (dist_between != 0): distances.append(dist_between)
  return sorted(distances)[0]

def move(operations, path_vector):
  current_position = path_vector[-1] # Takes the last element of the list

  vector_dict = {
    'R': vector(1, 0),
    'U': vector(0, 1),
    'L': vector(-1, 0),
    'D': vector(0, -1)
  }

  for operation in operations:
    times = int(operation[1:len(operation)])
    for i in range(times):
      new_position = addVector(current_position, vector_dict[operation[0]])
      current_position = vector(new_position['x'], new_position['y'])
      path_vector.append(new_position)

def parse(string):
  return string.split(',')

# This looks ugly as heck, mother of god
input = list(map(parse, open('Day 3/input.txt', 'r').read().split('\n'))) 
paths = [[vector()], [vector()]]

for i in range(len(input)):
  move(input[i], paths[i])

collisions = find_collisions(paths[0], paths[1])
nearest = find_nearest(vector(), collisions)
print(nearest)
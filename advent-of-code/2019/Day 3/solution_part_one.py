def distance(vector1, vector2):
  return (abs(vector1['x'] - vector2['x']) + abs(vector1['y'] - vector2['y']))

# There might be a library for this, but it gets the job done.
def vector(x = 0, y = 0):
  return { 'x': x, 'y': y }

def addVector(vector1, vector2):
  return vector(vector1['x'] + vector2['x'], vector1['y'] + vector2['y'])

def multVector(vector1, vector2):
  return vector(vector1['x'] * vector2['x'], vector1['y'] * vector2['y'])

def convert(v):
  a = v.split(',')
  return vector(int(a[0]), int(a[1]))

def parse(v):
  return str(v['x']) + ',' + str(v['y'])

def find_collisions(path1, path2):
  return path1.intersection(path2)

def find_nearest(vector_point, vector_list):
  nearest = 9999999
  for vector_ in vector_list:
    _vector = convert(vector_)
    dist_between = distance(_vector, vector_point)
    if (dist_between != 0 and nearest > dist_between): nearest = dist_between
  return nearest

def move(operations, path):
  current_location = convert(path.copy().pop()) # makes a copy of the set, takes the last element and converts it to a vector
                                                # is there any other way to get the last element without making a copy?
  vector_dict = {
    'R': vector(1, 0),
    'U': vector(0, 1),
    'L': vector(-1, 0),
    'D': vector(0, -1)
  }

  for opcodes in operations:
    direction = opcodes[0]
    steps = int(opcodes[1:len(opcodes)])
    for i in range(steps):
      new_location = addVector(current_location, vector_dict[direction])
      current_location = vector(new_location['x'], new_location['y'])
      path.add(parse(new_location)) # parses it back to a string so it can be stored in a set

# This looks ugly as heck, mother of god
def p(string): return string.split(',')
input = list(map(p, open('input.txt', 'r').read().split('\n'))) 

first_path = set({'0,0'})
second_path = set({'0,0'})

move(input[0], first_path)
move(input[1], second_path)

collisions = find_collisions(first_path, second_path)
closest = find_nearest(vector(0, 0), collisions)

print(closest)
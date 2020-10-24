separator = ','
input = open('./input.txt', 'r').read().split(separator)

def mod_four(i):
    return (i % 4) == 0

def toString(li):
  return separator.join(map(str, li))

opcodes = list(map(int, input))
functions = filter(mod_four, range(len(opcodes)))

for i in functions:
  opcode = opcodes[i]
  if (opcode == 99): break

  input1_index = opcodes[i+1]
  input2_index = opcodes[i+2]
  output_index = opcodes[i+3]

  input1 = opcodes[input1_index]
  input2 = opcodes[input2_index]

  if (opcode == 1): opcodes[output_index] = input1 + input2
  elif (opcode == 2): opcodes[output_index] = input1 * input2

print(toString(opcodes))
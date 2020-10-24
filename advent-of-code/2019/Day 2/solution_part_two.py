separator = ','
input = open('./input.txt', 'r').read().split(separator)

def mod_four(i):
    return (i % 4) == 0

def toString(li):
  return separator.join(map(str, li))

for noun in range(100):
  for verb in range(100):
    opcodes = list(map(int, input))
    functions = filter(mod_four, range(len(opcodes)))

    opcodes[1] = noun
    opcodes[2] = verb

    for instruction_pointer in functions:
      instruction = opcodes[instruction_pointer]

      parameterA_address = opcodes[instruction_pointer + 1]
      parameterB_address = opcodes[instruction_pointer + 2]
      parameterC_address = opcodes[instruction_pointer + 3]

      parameterA = opcodes[parameterA_address]
      parameterB = opcodes[parameterB_address]

      if (instruction == 1): opcodes[parameterC_address] = parameterA + parameterB
      elif (instruction == 2): opcodes[parameterC_address] = parameterA * parameterB
      elif (instruction == 99): break

    if (opcodes[0] == 19690720): print(100 * noun + verb)


# print(toString(opcodes))
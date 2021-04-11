import math

sigmoid = lambda x: 1 / (1 + math.exp(-x))

vector = (0.2, -1.11, 0.74)

for e in vector:
  print(sigmoid(e))
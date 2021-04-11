import math

def softmax(vector: tuple) -> tuple:
  vector_exp = []
  for e in vector:
    vector_exp.append(math.exp(e))

  denominator = 0
  for e in vector_exp:
    denominator += e

  result = []
  for e in vector_exp:
    result.append(e / denominator)
  return tuple(result)

print(softmax((13, 9, 9)))
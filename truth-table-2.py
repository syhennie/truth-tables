from itertools import product

expression = input()

variables = [item for item in sorted(set(expression.split())) if item.isupper()]

length = len(variables)

print(*[v for v in variables], "F")

for values in product([False, True], repeat=length):
    globals = {key: value for key, value in zip(variables, values)}
    print(*[int(v) for v in values], int(eval(expression, globals)))

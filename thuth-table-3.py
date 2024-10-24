from itertools import product

OPERATORS = {
    'not': 'not',
    'and': 'and',
    'or': 'or',
    '^': '!=',
    '->': '<=',
    '~': '==',
}

PRIORITY = {
    'not': 0,
    'and': 1,
    'or': 2,
    '^': 3,
    '->': 4,
    '~': 5,
    '(': 6,
}


def parse_expression(expression, variables):
    stack = []
    result = []

    expression = expression.replace('(', '( ').replace(')', ' )')

    for item in expression.split():
        if item in variables:
            result.append(item)
        elif item == '(':
            stack.append(item)
        elif item == ')':
            while stack[-1] != '(':
                result.append(OPERATORS[stack.pop()])
            stack.pop()
        elif item in OPERATORS:
            while stack and PRIORITY[item] >= PRIORITY[stack[-1]]:
                result.append(OPERATORS[stack.pop()])
            stack.append(item)
    while stack:
        result.append(OPERATORS[stack.pop()])
    return result


def evaluate(expression, variables):
    stack = []
    for item in expression:
        if item in variables:
            stack.append(variables[item])
        else:
            if item == 'not':
                stack.append(not stack.pop())
            else:
                variable2, variable1 = stack.pop(), stack.pop()
                stack.append(eval(f'{variable1} {item} {variable2}'))  # noqa
    return int(stack.pop())


expression = input()
variables = sorted(set([item for item in expression if item.isupper()]))
parsed_expression = parse_expression(expression, variables)
table = product([0, 1], repeat=len(variables))

print(*variables, 'F')
for values in table:
    globals = {key: value for key, value in zip(variables, values)}
    print(*values, evaluate(parsed_expression, globals))

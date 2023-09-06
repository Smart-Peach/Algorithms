from typing import List


def to_polish_entry(mat_expression: str) -> List:
    priority = {'**': 10, '*': 9, '/': 9, '+': 8, '-': 8, '<<': 7, '>>': 7, '<': 6, '>': 6, '<=': 6, '>=': 6,
                '==': 5, '!=': 5, '&': 4, '^': 3, '|': 2, '&&': 1,
                '||': 0, '(': -1, ')': -1}  # operators dictionary; only '**' - right associative operation
    symbols = mat_expression.split()  # Original expression
    stack = []  # For operations
    result = []  # Result
    for i in symbols:
        if i not in priority:  # if number, then add to the result
            result.append(i)
        else:
            if not len(stack):  # If stack is empty, then just push operator into stack
                stack.append(i)
            else:
                if i == '(':
                    stack.append(i)
                elif i == ')':
                    while stack[-1] != '(':
                        result.append(stack[-1])
                        stack.pop(-1)
                    stack.pop(-1)
                else:
                    while len(stack) and (priority[stack[-1]] >= priority[i]) and i != '**':
                        result.append(stack[-1])
                        stack.pop(-1)
                    stack.append(i)

    while len(stack):
        result.append(stack[-1])
        stack.pop(-1)
    return result


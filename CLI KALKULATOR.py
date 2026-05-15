from math import *

variables = {}


def evaluate(expr):
    try:
        return eval(expr, {"__builtins__": None}, variables)
    except Exception as e:
        return f"Error: {e}"


while True:
    command = input('>> ').strip()

    if command.upper() == 'EXIT':
        break

    parts = command.split(maxsplit=2)

    if parts[0].upper() == 'SET':
        var = parts[1]
        value = float(parts[2])
        variables[var] = value
        print(f'{var} = {value}')

    elif parts[0].upper() == 'EVAL':
        expr = parts[1]
        print(evaluate(expr))

    elif parts[0].upper() == 'LIST':
        for k, v in sorted(variables.items()):
            print(k, '=', v)

    else:
        print('Perintah tidak dikenali')

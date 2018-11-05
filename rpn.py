#!/usr/bin/env python3

import operator
import readline
import pdb
import sys


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod
}

def calculate(myarg, mode):
    stack = list()
    if mode == 1: # debug mode
        pdb.set_trace()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    debug_mode = 0
    if len(sys.argv) == 2:
        if sys.argv[1] == '-debug':
            debug_mode = 1
        else:
            raise TypeError("Invalid Option")
    while True:
        result = calculate(input("rpn calc> "), debug_mode)
        print("Result: ", result)

if __name__ == '__main__':
    main()

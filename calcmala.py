#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

operators = ['plus', 'minus']

try:

    integer1 = int(sys.argv[1])
    operator = sys.argv[2]
    integer2 = int(sys.argv[3])

except ValueError:
    sys.exit('Error: Non numerical parameters')

result = 'no result'

if operator not in operators:
    print('Operator not recognized')
    sys.exit()

print(integer1, operator, integer2)

if operator == 'plus':
    result = integer1 + integer2

elif operator == 'minus':
    result = integer1 - integer2

print('Result is:', result)

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculator ():

    def __init__(self):
        pass

    def plus(self, oper1, oper2):
        return int(oper1) + int(oper2)

    def minus(self, oper1, oper2):
        return int(oper1) - int(oper2)

    def times(self, oper1, oper2):
        return int(oper1)*int(oper2)

    def divided(self, oper1, oper2):
        return int(oper1)/int(oper2)

#If   this is executed on his own, do this:

def Operate():

    if sys.argv[2] == 'plus':
        result = calc.plus(sys.argv[1],sys.argv[3])
    elif sys.argv[2] == 'minus':
        result = calc.minus(sys.argv[1],sys.argv[3])
    elif sys.argv[2] == 'times':
        result = calc.times(sys.argv[1],sys.argv[3])
    elif sys.argv[2] == 'divided':
        result = calc.divided(sys.argv[1],sys.argv[3])
    else:
        print()
        sys.exit('Error: Only Add, Substract, Multiply or Divide operations are allowed')
    return result



if __name__ == "__main__":

    print()
    print('//----Adrián Rodrigo Castillo, 3o ISAM URJC-------')
    print('//----Simple calculator program')
    print()
    print('Input operand was: ' + str(sys.argv[2]) + ' and operands were: ' + str(sys.argv[1]) + ' and ' + str(sys.argv[3]))
    try:
        operand1 = int(sys.argv[1])
        operand2 = int(sys.argv[3])
    except ValueError:
        print()
        sys.exit('Error: operands must be integer numbers')

    calc = Calculator()
    result = Operate()
    print()
    print('Result is: ' + str(result))
    print()

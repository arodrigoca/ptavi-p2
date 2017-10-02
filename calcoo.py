#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora ():

    def __init__(self):
        pass

    def plus(self, oper1, oper2):
        return int(oper1) + int(oper2)

    def minus(self, oper1, oper2):
        return int(oper1) - int(oper2)


def Operate():

    if sys.argv[2] == 'suma':
        result = calc.plus(sys.argv[1], sys.argv[3])
    elif sys.argv[2] == 'resta':
        result = calc.minus(sys.argv[1], sys.argv[3])
    else:
        print()
        sys.exit('Error: Only suma or resta operations are allowed')
    return result


if __name__ == "__main__":

    print()
    print('//----Adrián Rodrigo Castillo, 3o ISAM URJC-------')
    print('//----Simple calculator program')
    print()
    print('Input operator was: ' + str(sys.argv[2]) + ' and operands were: ' + str(sys.argv[1]) + ' and ' + str(sys.argv[3]))
    try:
        operand1 = int(sys.argv[1])
        operand2 = int(sys.argv[3])
    except ValueError:
        print()
        sys.exit('Error: operands must be integer numbers')

    calc = Calculadora()
    result = Operate()
    print()
    print('Result is: ' + str(result))
    print()

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

class CalculadoraHija(Calculator):
    def __init__(self):
        pass
    def times(self, oper1, oper2):
        return int(oper1)*int(oper2)

    def divided(self, oper1, oper2):
        try:
            return int(oper1)/int(oper2)
        except:
            sys.exit("Error: Division by zero is not allowed")

#If   this is executed on his own, do this:

def Operations(opr, op1, op2, calc):

    if opr == 'suma':
        result = calc.plus(op1,op2)
    elif opr == 'resta':
        result = calc.minus(op1,op2)
    elif opr == 'multiplica':
        result = calc.times(op1,op2)
    elif opr == 'divide':
        result = calc.divided(op1,op2)
    else:
        print()
        sys.exit('Error: Only Add, Substract, Multiply or Divide operations are allowed')
    return result



def getData():

    data = text.readline()
    data = data.rstrip('\n')
    dataList = data.split(',')

    return dataList


def operateLine(calc):

        line = getData()
        for w in range(1,len(line)):
            if w < len(line):
                x = line[0]
                y = line[1]
                z = line[2]
                result = Operations(x, y, z, calc)
                print("wee")




if __name__ == "__main__":

    with open('op.txt', 'r') as text:
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

        opr = sys.argv[2]
        op1 = int(sys.argv[1])
        op2 = int(sys.argv[3])
        calc = CalculadoraHija()
        operateLine(calc)
        result = Operations(opr, op1, op2, calc)
        print()
        print('Result is: ' + str(result))
        print()

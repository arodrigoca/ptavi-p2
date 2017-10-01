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
            if w + 1 < len(line):
                if w == 1:    
                    opr = line[0]
                    op1 = line[w]
                    op2 = line[w+1]
                    print("first operation I do: ", opr,op1,op2)
                    result = Operations(opr, op1, op2, calc)
                    print("and result is: ", result)

                else:
                    op2 = line[w+1]
                    print("I do: ", opr, result, op2)
                    result = Operations(opr, result, op2, calc)
                    print("and result is: ", result)

        return result




if __name__ == "__main__":

    with open('op.txt', 'r') as text:
        print()
        print('//----Adrián Rodrigo Castillo, 3o ISAM URJC-------')
        print('//----Simple calculator program')
        print()
        calc = CalculadoraHija()
        goodResult = operateLine(calc)
        print()
        print('Result is: ', goodResult)
        print()
        print()

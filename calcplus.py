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



def getLine():

    data = text.readline()
    data = data.rstrip('\n')
    dataList = data.split(',')

    return dataList


def operateLine(calc):

    line = getLine()
    if line[0] != '':
        for w in range(1,len(line)):
            if w + 1 < len(line):
                if w == 1:    
                    opr = line[0]
                    op1 = line[w]
                    op2 = line[w+1]
                    result = Operations(opr, op1, op2, calc)
                else:
                    op2 = line[w+1]
                    result = Operations(opr, result, op2, calc)
        end = False
    else:
        end = True;
        result = None

    return (result, end)

def operateFile(calc):

    end = False
    results = []

    while end == False:
        result, end = operateLine(calc)
        if result != None:
            results.append(result)
    return results

if __name__ == "__main__":

    file = sys.argv[1]
    try:

        with open(file, 'r') as text:
            print()
            print('//----Adrián Rodrigo Castillo, 3o ISAM URJC-------')
            print('//----Simple calculator program. This time with CSVs in a text file')
            print()
            calc = CalculadoraHija()
            results = operateFile(calc)
            print()
            print('Results are: ', results)
            print()
            print()

    except FileNotFoundError:
        print("File not found. Try again with another file name")

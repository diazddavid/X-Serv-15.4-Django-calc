from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def operacion(self, op1, opType, op2):

    if opType == "+":
        to_return = str(op1 + op2) 
    elif opType == "-":
        to_return = str(op1 - op2)
    elif opType == "*":
        to_return = str(op1 * op2)
    else:
        to_return = str(op1 / op2)

    return HttpResponse("<body><h1> Su operacion " + str(op1)
                         + opType + op2  + " = " + to_return
                         + "</h1></body>")

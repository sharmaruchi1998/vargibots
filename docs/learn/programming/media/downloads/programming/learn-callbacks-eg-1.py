#!/usr/bin/python

def add(arg_a, arg_b):
    return (arg_a + arg_b)

def subtract(arg_a, arg_b):
    return (arg_a - arg_b)

def multiply(arg_a, arg_b):
    return (arg_a * arg_b)

def divide(arg_a, arg_b):
    return (arg_a / arg_b)

def calculate(arg_func_pointer, arg_num1, arg_num2):
    return ( arg_func_pointer(arg_num1, arg_num2) )

def main():
        
        print( "6 + 2 = " + str(calculate(add, 6, 2)) )
        print( "6 - 2 = " + str(calculate(subtract, 6, 2)) )
        print( "6 * 2 = " + str(calculate(multiply, 6, 2)) )
        print( "6 / 2 = " + str(calculate(divide, 6, 2)) )

        print('---------')

        print(str(add) + ' ' + str(type(add)))
        print(str(subtract) + ' ' + str(type(subtract)))
        print(str(multiply) + ' ' + str(type(multiply)))
        print(str(divide) + ' ' + str(type(divide)))


if __name__ == "__main__":
    main()
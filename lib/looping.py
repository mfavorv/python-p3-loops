#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=10
    while (i > 0):
       print(i)
       i-=1

    print("Happy New Year!")    
    pass

def square_integers(int_list):
    square_int = ([])
    for int in int_list:
        square = int*int
        square_int.append(square)

    return square_int   
    # code goes here!
    pass

def fizzbuzz():
    i = 1
    while (i < 101):
        three_multiple = i % 3
        five_multiple = i % 5
        if three_multiple == 0 and five_multiple == 0:
            print( "FizzBuzz")
        elif three_multiple == 0:
            print("Fizz")
        elif five_multiple == 0:
            print("Buzz")
        else: print(i)
        i+=1

    # code goes here!
    pass

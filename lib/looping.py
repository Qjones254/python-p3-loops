#!/usr/bin/env python3

def happy_new_year():
    # Initialize the countdown variable
    countdown = 10
    
    while countdown >= 0:
        print(countdown)
        countdown-=1
        print("Happy New Year!")


def square_integers(int_list):
    squared_list = [x ** 2 for x in int_list]
    return squared_list

numbers = [1, 2, 3, 4, 5]
squared_numbers = square_integers(numbers)
print(squared_numbers)


def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i % 3 ==0 and i % 5 ==0:
            print ("FizzBuzz")
        elif i % 3 ==0:
            print ("Fizz")
        elif i % 5 ==0:
            print("Buzz")
        else:
            print(i)

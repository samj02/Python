#Make the program below work, and print out two
#numbers multiplied together.
import random
x = input("Give me a number!")
x = int(x)

y = input("Give me another number!")
y = int(y)

def times_two_numbers(number_one, num_two):
    return  number_one*num_two
print(str(times_two_numbers(x, y)))
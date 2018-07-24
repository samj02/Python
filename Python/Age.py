import random
age = input("What is your age?");
age = int(age)

if age >= 0 and age <=4:

    print("You are a baby!");

elif age >=5 and age <=12:

    print("You are a child!");

elif age >=13 and age <=17:

    print("You are a teenager!");

elif age >=18:

    print("You are an adult!");

else:

    print("That is not an age!");
name = input("What is your name?");
name = name.rstrip()

print("Hello " + name + "! Find a way out this forest!");

way = input("YOU SEE FORK what way left/RIGHT")
way = way.rstrip()

if way == "left":
    print("You walk until ur a lost!")

elif way == "right":
    print("You walk until ur a lost!")

elif way == "up":
    print("You go up and see the exit! You Win!")

else:
    print("That is nota way!")



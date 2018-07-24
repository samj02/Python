import ctypes

ctypes.windll.user32.MessageBoxA,print( "Welcome to madlibs! \n Lets start!");

noun1 = input("Give me a Noun.");
noun1 = noun1.rstrip()

gender = input("Give me a Gender. | He/She.");
gender = gender.rstrip()

time = input("Give me a Time.");
time = time.rstrip()

emotion = input("Give me an Emotion.");
emotion = emotion.rstrip()



ctypes.windll.user32.MessageBoxA,print("There once was a " + noun1 + ". " + gender + " woke up at " + time + "." + gender +" was feeling very " + emotion + ".");



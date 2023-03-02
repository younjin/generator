def greetings(name):

    guess = input("Hello! Is your name {}? ".format(name))
    
    if guess.lower() == "yes":
        print("Hello, {}!".format(name))
    
    else:
        actual = input("Okay, what is your name then? ")
        print("Hello, {}!".format(actual))

greetings("Bobo")
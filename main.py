from time import sleep
import random

# Create Lists

try:
    def makelist(filepath, ):
        file = open(filepath, "r")
        listnum = file.readlines()
        varnum = random.choice(listnum)
        return varnum


    a_who = makelist("who.txt", )
    a_with = makelist("withwho.txt", )
    a_doing = makelist("whatdoin.txt", )
    a_where = makelist("where.txt", )
except IOError:
    print("Could not open a file. Please verify files")
except:
    print("Unexpected error")

def menu():
    print("Welcome to WordGame v 1.0!")
    sleep(1)
    print("This is a game where you can create crazy sentences by thinking up answers to Who? question for example.")
    sleep(3)
    print("Type '1' to start or '2' to exit program")
    u = int(input("Your choice: "))
    return u

while True:
    try:
        u = menu()
        if u == 1:
            u_who = input("OK, first question. Please be creative. Who? (examples: A dog, A sad kid): ")
            u_with = input("Cool, next. With who/what? (examples: a cat, an apple): ")
            u_doing = input("Nice! Here's next question. What <that person/thing> is doing? "
                            "(examples: talking to friends, singing ): ")
            u_where = input("Great, last question - Where? (examples: AT THE cinema, BEHIND THE supermarket): ")
            if u_who == "" or u_who == " ":
                u_who = "You"

            if u_with == "" or u_with == " ":
                u_with = "a cat"

            elif "with" in u_with or "With" in u_with:
                u_with.replace("with", "").replace("With", "")

            if u_doing == "" or u_doing == " ":
                u_doing = "handling an exception"

            elif "are" in u_doing or "is" in u_doing:
                u_doing.replace("are", "").replace("is", "")

            if u_where == "" or u_where == " ":
                u_where = "at the cinema"

            sleep(0.5)
            print("")
            print("First sentence: " + u_who + " with " + a_with + " are " + u_doing + " " + a_where + "." )
            sleep(2)
            print("")
            print("Second sentence: " + a_who + " with " + u_with + " are " + a_doing + " " + u_where + "." )
            print("")
            print("----------")
            print("")
            menu()

        elif u == 2:
            break
        else:
            sleep(1)
            print("")
            print("Type OPTION number from 1-2")
            print("")
            del u
            sleep(1)
            menu()
            u = int(input("Your choice: "))
    except ValueError:
        sleep(1)
        print("")
        print("Please type a NUMBER")
        print("")

print("Thank you for using WordGame. Report bugs at <GitHub link>")
sleep(2)
input("Press any key to exit ")

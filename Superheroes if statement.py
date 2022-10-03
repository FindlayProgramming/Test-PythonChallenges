import time

def Superheroes():
    print("Welcome to part one user!")
    print("This will take a moment...")
    time.sleep(3)
    antihero = input("Does your superhero kill criminals?")
    if antihero == "yes":
        question2 = input("Is your superhero Robby Reyes?")
        if question2 == "yes":
            print("The hero you're thinking of is Ghost Rider.")
        else:
            print("The hero you're thinking of is Moon Knight.")

Superheroes()

time.sleep(3)

def Superheroes2():
    print("Welcome to part two user!")
    print("This will take a moment...")
    time.sleep(3)
    Active = input("Is your superhero active?")
    if Active == "yes":
        question4 = input("Is your character blind?")
        if question4 == "no":
            print("The hero you're thinking of is Black Widow.")
        else:
            print("The hero you're thinking of is Daredevil.")

Superheroes2()

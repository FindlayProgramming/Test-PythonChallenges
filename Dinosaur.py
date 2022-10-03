import time

def Dinosaurs():
    password = input("Welcome user! Input your password:")
    while password == "D":
        print("Password acknowledged, this will take a moment...")
        time.sleep(3)
        break
    else:
        print("Error, try again.")
        exit()
    Skull = input("Does the dinosaur have a massive skull?")
    if Skull == "Yes":
        Horns= input("Does the dinosaur have blunt horns in front of the eyes?")
        if Horns == "Yes":
            print("The dinosaur is a Allosaurus!")
            print("Round 2...")
            time.sleep(3)
            Arms = input("Does the dinosaur have tiny arms?")
            if Arms == "Yes":
                print("The dinosaur is a T-Rex!")
            else:
                print("The dinosaur is a Spinosaurus!")
    else:
        Tail = input("Does the dinosaur have an absent tail?")
        if Tail == "Yes":
            print("The dinosaur is a Pterodactyl!")
        else:
            print("The dinosaur is a Dimetrodon!")
        print("Round 2...")
        time.sleep(3)
        Arms = input("Does the dinosaur have tiny arms?")
        if Arms == "Yes":
            print("The dinosaur is a T-Rex!")
        else:
            print("The dinosaur is a Spinosaurus!")
            exit()

Dinosaurs()


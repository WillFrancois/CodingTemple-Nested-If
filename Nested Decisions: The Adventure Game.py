#Task 1
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    #Task 3
    else:
        pass
elif place == "cave":

#Task 2 (Setting the scene)

    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You find a hidden treasure!")
    elif action == "proceed in the dark":
        print("You find a light at the end. You have escaped the cave!")
    #Task 3
    else:
        pass
#Task 3
else:
    pass


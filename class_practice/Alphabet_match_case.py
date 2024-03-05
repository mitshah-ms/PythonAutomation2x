alphabet1 = str(input("Enter an Alphabet to learn\t"))
alphabet1 = alphabet1.lower()

match alphabet1:
    case "a":
        print("Apple")
    case "b":
        print ("Ball")
    case "c":
        print ("Cat")
    case "d":
        print("Dog")
    case "e":
        print("Elephant")
    case _:
        print("No Idea")

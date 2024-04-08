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
    case "f":
        print("Fish")
    case "g":
        print("Grapes")

    case "h":
        print("Hat")
    case "i":
        print("Ice-Cream")
    case "j":
        print("Joker")
    case "k":
        print("Kite")
    case "l":
        print("Lion")
    case "m":
        print("Monkey")
    case "n":
        print("Nose")
    case "o":
        print("Orange")
    case "p":
        print("Parrot")
    case "q":
        print("Queen")
    case "r":
        print("Rabbit")
    case "s":
        print("Shoe")
    case "t":
        print("Table")
    case "u":
        print("Umbrella")
    case "v":
        print("Van")
    case "w":
        print("Watch")
    case "x":
        print("X-mas")
    case "y":
        print("Yak")
    case "z":
        print("Zebra")
    case _:
        print("No Idea")

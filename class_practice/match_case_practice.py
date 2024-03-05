'''
switch case is here match case
'''

numbers = int(input("Enter a number\t"))

match numbers:
    case 1:
        print("You have entered number 1")
    case 2:
        print("You have entered number 2")
    case 3:
        print("You have entered number 3")
    case _:
        print("\tNo !dea")

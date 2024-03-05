# find a factorial by function

def factorial_finder(fact):
    f = 1
    for i in range(1, fact + 1):
        f = f * i
    return f


a = int(input("Enter a number to find a factorial => "))
n = factorial_finder(a)
print(f"factorial of a given number is : {n}")

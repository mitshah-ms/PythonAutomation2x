number = int(input("Enter the Fac number\n"))
if number < 0:
    print("Fact")
elif number == 0:
    print("Fact - ", 1)
else:
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i

print("Fact ->>", fact)
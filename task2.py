# task 2. print table of by taking input from user...
number = int(input("Enter a number to print table-> "))
# print ("Given number for table is ",number)
# print (" 2 x 2 = ", 2 * 3)

print("2 x 1 = ", 2 * 1)
print("2 x 2 = ", 2 * 2)
print("2 x 3 = ", 2 * 3)
print("2 x 4 = ", 2 * 4)
print("2 x 5 = ", 2 * 5)
print("2 x 6 = ", 2 * 6)
print("2 x 7 = ", 2 * 7)
print("2 x 8 = ", 2 * 8)
print("2 x 9 = ", 2 * 9)
print("2 x 10 = ", 2 * 10)

print(f"\n<-- Your given table for print-->\n")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

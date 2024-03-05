# find factorial from given input
number = int(input("Enter number to find factorial -> "))
temp = number
factorial = int(number)
sml_num = int(number - 1)

for i in range(number):  # 0,1
    factorial = factorial * sml_num  # 1. 5*4=20 | 2.20*3=60 |
    sml_num = int(sml_num - 1)  # 1. 3 | 2. 2
    # if (sml_num == 1):
    print(f"{factorial}")  # 1. 20 | 2. 60
    # break

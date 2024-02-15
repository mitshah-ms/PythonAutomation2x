# checks for palidrome

str1 = str.lower(input("Enter the string -> "))
str2 = ""
trial = 0
for i in str1:
    trial += 1
    print(f"---Trial {trial}---")

    print(f"i = {i}")
    str2 = i + str2
    print(f"str2 = {str2}")

if str2 == str1:
    print(f"{str1} and {str2} are palindrome")
else:
    print(f"{str1} and {str2} are not a palindrome")

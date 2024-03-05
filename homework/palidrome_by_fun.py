# create a function to check palindrome string or number

# logic part and return the value
def palindrome_checker(str1):
    rev_strg = ""
    for counter in main_str:
        rev_strg = counter + rev_strg
    print(f"Reverse of main string is -> {rev_strg}")
    return main_str


# main calling part and takes return
main_str = str.lower(input("Enter a string to check Palindrome -> "))
rev_str = palindrome_checker(main_str)

if rev_str == main_str:
    print(f"{rev_str} and {main_str} are Palindrome")
else:
    print(f"{rev_str} and {main_str} are not a Palindrome")

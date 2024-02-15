# fibonaci series by input number

fibonaci_lmit = int(input("Enter limit for fibonaci series -> "))  # 7

ans = 0
print(ans)
n1 = 0
n2 = 1
# print(n1, end=" ")
# print(n2, end=" ")
for i in range(fibonaci_lmit):
    ans = n1 + n2
    print(ans)
    n1 = n2
    n2 = ans

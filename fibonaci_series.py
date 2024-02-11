# fibonaci series by input number

fibonaci_lmit = int(input("Enter limit for fibonaci series -> "))  # 7

fibo = 0
print(fibo)
n1 = 0
n2 = 1

for i in range(fibonaci_lmit):
    ans = i + n2 #1 3
    fibo = n2 + ans #2 5
    print(f"ans = {ans}")
    print((f"fibo = {fibo}"))
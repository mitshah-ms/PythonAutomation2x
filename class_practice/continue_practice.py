for num in range(1, 10):
    if num % 2 == 0:
        print(f"\tfound even number {num}")
        continue
    print(f"found odd number {num}")
    print("this is 'for loop' continued")

print("\t\twhole program executed, you are out of 'for' loop now.")

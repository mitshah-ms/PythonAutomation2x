def say_hello():
    print("Hello")


say_hello()


# for i in range(1, 10):
#     if i % 2 != 0:
#         say_hellO()
#         print(i)
#     pass


def say_hello_arg(name):
    print(name)


say_hello_arg("mit")


def say_hello_2args(name, age):
    print(f"Hello {name}, You are now {age} years old")
    print(name, age)


say_hello_2args("mit", 34)
say_hello_2args(22.06, True)


def say_hello_args_default(name="Hey, Mit Shah", age=33):
    print(name, age)


say_hello_args_default()
say_hello_args_default("Hare Krishna", 5000)
say_hello_args_default(3000)
say_hello_args_default(None, 34)
say_hello_args_default(name="meera bai", age=22)
say_hello_args_default(12, 21)
say_hello_args_default(108.25456465456465456456465, 2.234644685484721)


def sum_with_arg_with_return(a, b):
    result = a + b
    return result


r1 = sum_with_arg_with_return(a=5, b=10)
print(r1)
r2 = sum_with_arg_with_return(True, False)
print(r2)
r3 = sum_with_arg_with_return("My Name is\t", "Mit Shah\n")
print(r3)

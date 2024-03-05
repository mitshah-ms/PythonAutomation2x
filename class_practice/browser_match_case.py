browser = str(input("Enter a browser for automation\t"))
browser = browser.lower()

match browser:
    case "chrome":
        print(f"You have entered {browser} for automation")
    case "mozilla":
        print(f"You have entered {browser} for automation")
    case "safari":
        print(f"You have entered {browser} for automation")
    case "opera":
        print(f"You have entered {browser} for automation")
    case _:
        print(f"You have entered {browser} for automation")

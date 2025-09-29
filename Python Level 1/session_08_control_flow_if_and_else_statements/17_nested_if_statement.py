age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
    if age >= 65:
        print("You are also a senior citizen.")
    else:
        print("You are not a senior citizen yet.")
else:
    print("You are a minor.")

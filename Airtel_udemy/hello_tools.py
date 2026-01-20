def greet(name):
    return f"Hello, {name}! Welcome to Python."

def add(a, b):
    return a + b

def main():
    user = input("Enter your name: ")
    print(greet(user))

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Sum is:", add(x, y))

    print("Program executed successfully!")

if __name__ == "__main__":
    main()

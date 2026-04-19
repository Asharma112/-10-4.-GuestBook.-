filename = "guest_book.txt"

while True:
    name = input("What's your name? ")
    print(f"Hello, {name}!")

    with open(filename, "a") as file:
        file.write(name + "\n")
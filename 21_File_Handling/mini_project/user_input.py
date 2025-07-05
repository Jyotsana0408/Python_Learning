# user_input = input("Enter your message: ")

# with open("user_data.txt", "w") as file:
#     file.write(user_input)


with open("user_data.txt", "w") as file:
    while True:
        line = input("Type something (or 'exit' to finish): ")
        if line.lower() == "exit":
            break
        file.write(line + "\n")

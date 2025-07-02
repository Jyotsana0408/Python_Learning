# a = input("Enetr a Number: ")
# for i in range(1,11):
#     print(f"{a} X {i} = {int(a)*i}")

# print("Some imp lines of code")
# print("End of program")


#  if you give value of a = Harry , it will throw an error, and it will not execute next line code
# using try except will not hault your program


try:
    a = input("Enter a Number: ") # give a = Harry or any other string
    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")
except Exception as e:
    print("Invalid input") 
    print(e)

print("Some imp lines of code")
print("End of program")


# Handle Specific error

try:
    num = int(input("Enter an integer: "))
    a = [3,4]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")
def Calc_Factorial(a):
    if a < 0:
        return "Factorial is not defined for negative numbers."
    elif a == 0 or a == 1:
        return 1
    else:
        return a * Calc_Factorial(a-1)
a = int(input("Enter a number: "))

result = Calc_Factorial(a)
print(result)
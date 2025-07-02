def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    # print("The avg is ",sum/len(numbers))
    return sum/len(numbers)

c = average(1,2,3)
print(c)
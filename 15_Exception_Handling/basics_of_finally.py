#  The finally block will always executed

try:
    l = [1,3,5,7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occured")
finally:
    print("I will always execute")


# with function but without finally

# def func1():
#     try:
#         l1 = [1,3,5,7]
#         i1 = int(input("Enter the index: "))
#         print(l1[i1])
#         return 1
#     except:
#         print("Some error occured")
#         return 2
#     print("I will always execute")

# x = func1()
# print(x)


# with function but with finally
# imp use case is in a function which returns a value

def func2():
    try:
        l2 = [1,3,5,7]
        i2 = int(input("Enter the index: "))
        print(l2[i2])
        return 1
    except:
        print("Some error occured")
        return 2
    finally:
        print("I will always execute")

y = func2()
print(y)
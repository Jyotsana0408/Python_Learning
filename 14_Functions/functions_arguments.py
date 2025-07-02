# required arguments

def average(a,b):
    print("The average is ",(a+b)/2)

average(4,6)

# default arguments
def average(a=9,b=5):
    print("The average is ",(a+b)/2)

average()

def average(a=9,b=5):
    print("The average is ",(a+b)/2)

average(5)

def average(a=9,b=5):
    print("The average is ",(a+b)/2)

average(b=3)

# keyword arguments - can change order

def average(a=9,b=5):
    print("The average is ",(a+b)/2)

average(b=3, a=6)

# variable-length arguments


def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    print("The avg is ",sum/len(numbers))

average(1,2,3)

# keyword arbitary arguments -- want arguments as dictinaries

def name(**name):
    print("Hello,", name["fname"],
          name["mname"], name["lname"])
    
name(mname="Raj" , lname = "Kumar", fname="Aditya")




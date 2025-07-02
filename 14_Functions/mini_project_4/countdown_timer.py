import time

def Countdown_Timer(n):
    if n <= 0:
        print("Times up!!!!!!!")
    else:
        print(n)
        time.sleep(1)
        return Countdown_Timer(n-1)

t = int(input("Enter time for timer: "))
Countdown_Timer(t)
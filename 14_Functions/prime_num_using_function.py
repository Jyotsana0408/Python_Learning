def isPrime(a):
    if a > 1:
        for i in range(2,a):
            if a%i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
    else:
        print("Not Prime")

isPrime(7)
isPrime(2)
isPrime(4)
isPrime(12)
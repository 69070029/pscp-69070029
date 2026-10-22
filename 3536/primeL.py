"""isPrime_large"""
num = int(input())

if num < 2:
    print("NO")
else:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            prime = False
            break

    if not prime:
        print("NO")
    else:
        print("YES")

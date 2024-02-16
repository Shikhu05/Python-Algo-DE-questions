def largestPrimeFactor (N):
    primes = []
    n = int (N ** 0.5) 


    for i in range( 2, n+1) :
        while N % i == 0:
            N //= i
            primes.append(i)

    return (N if N != 1 else primes[-1])

print(largestPrimeFactor (24))

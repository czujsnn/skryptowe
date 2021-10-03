import sys

n = len(sys.argv) - 1
list_of_primes  = [int(x) for x in sys.argv[1:]]
max_occurence = max(list_of_primes)

def sieve(number):

    if number <2:
        print("Enter argumetns greater than 1.")

    prime = [True] * number
    prime[0],prime[1] = False,False
    
    for i in range(2, int(number**0.5)+1):

        j = i*i

        while j < number:

            prime[j] = False
            j +=  i

    return [x for x in range(number) if prime[x] == True]

check_prime = sieve(max_occurence + 1)
primes_from_argv = [x for x in list_of_primes if x in check_prime]

#printowanie
for _ in primes_from_argv:
    print(_,end="\n")

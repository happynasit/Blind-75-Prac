class Solution:
    def countPrimes(self, n: int) -> int:
        """
        SOLUTION FOUND IN SOLUTIONS PART
        1. Create a list: Write down all the natural numbers from 2 to n.
        2. Start with 2: Since 2 is the smallest prime number, circle it.
        3. Cross out multiples: Now, go through the list and cross out all the 
           multiples of 2 (4, 6, 8, etc.)
        4. Find the next prime: Look for the next unmarked number greater than 2 
           (which will be 3). Circle it as it's prime.
        5. Repeat: Cross out all the multiples of the newly found prime (3) greater 
           than its square (which is 9 in this case). So you'd cross out 9, 12, 15, etc.
        6. Continue the process: Keep repeating steps 4 and 5. Find the next unmarked 
           number (which will be 5), circle it (prime), and cross out its multiples greater 
           than its square (25).
        7. Stop at the square root: There's an optimization here. You only need to iterate 
           up to the square root of n because any composite number greater than that will have 
           already been marked by a smaller prime.
        """
        # Sieve method
        # It is an optimised way of finding the number of primes that is there before n

        # This includes cases like 0, 1 and 2. 2 won't count in the number of primes since 
        # we are finding the number of primes LESS THAN n.
        if n < 3:
            return 0

        # This is just for counting the number of prime numbers using this lise
        # like if any number is a MULTIPLE, then we put it as FALSE, as in it is not a prime
        # number.
        primes=[True] * n

        # We will start from 2 since 0 and 1 are not prime numbers, and we want to reduce time
        # 2 is the first prime number so we start with that.
        i=2

        # First, in the notebook, mark and traverse.
        # like if n = 10, [T T T T T T T T T T]
        # Here we include 0 and 1 to but we will remove that by - 2

        # we circle 2, cuz that's what we will start with first.
        # now since 2 is true, we will go through the loop from its SQUARE TO N,
        # since before squares, the value must have been cut off by its previous prime numbers
        ### ITERATE USING I ** 2, N, I . It goes from i**2 to n jumping by i, whick indicates
        # that only the factors of i greater than its square is turned false, which means that
        # only multiples of i is false now. 

        # now next, if we go to three, then we don't have to worry about the values less than 
        # the square cuz that was all cut off during the loop when i = 2. 

        # and the better part, we iterate only till the square root of n, since all composite
        # numbers after the square root must have been cut off already, so we don't have to 
        # worry about it.
        while (i**2)<n:
            if primes[i]:
                for j in range(i**2,n,i):
                    primes[j]=False
            i+=1
        return primes.count(True)-2

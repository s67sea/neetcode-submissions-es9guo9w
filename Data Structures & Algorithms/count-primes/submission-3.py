class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        sieve = [1]*(n)
        sieve[0] = 0 #don't use the zero index
        sieve[1] = 0


        currptr = 2
        while currptr*currptr <= n:
            for i in range(currptr*currptr,n,currptr):
                sieve[i] = 0
            currptr += 1
            while currptr < n and sieve[currptr]==0:
                currptr += 1
        return sum(sieve)



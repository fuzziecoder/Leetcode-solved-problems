from collections import Counter

MOD = 10**9 + 7

MAX_N = 2 * 10**4
fact = [1] * (MAX_N + 1)
inv_fact = [1] * (MAX_N + 1)

for i in range(2, MAX_N + 1):
    fact[i] = fact[i - 1] * i % MOD

def mod_inv(x, mod=MOD):
    return pow(x, mod - 2, mod)

inv_fact[MAX_N] = mod_inv(fact[MAX_N])
for i in range(MAX_N - 1, 0, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def binomial(n, k):
    if k > n or k < 0:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def prime_factorization(x):
    factors = Counter()
    d = 2
    while d * d <= x:
        while x % d == 0:
            factors[d] += 1
            x //= d
        d += 1
    if x > 1:
        factors[x] += 1
    return factors

def count_ways(n, k):
    factors = prime_factorization(k)
    result = 1
    for exponent in factors.values():
        result = (result * binomial(n + exponent - 1, exponent)) % MOD
    return result

class Solution(object):
    def waysToFillArray(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        return [count_ways(n, k) for n, k in queries]
def staircase(n):
    if n <= 1:
        return 1
    return staircase(n - 1) + staircase(n - 2)

# Of course, this is really slow (O(2N)) — we are doing a lot of repeated computations! We can do it a lot faster by just computing iteratively:

def staircase(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# Now, let's try to generalize what we've learned so that it works if you can take a number of steps from the set X. Similar reasoning tells us that if X = {1, 3, 5}, then our algorithm should be f(n) = f(n - 1) + f(n - 3) + f(n - 5). If n < 0, then we should return 0 since we can't start from a negative number of steps.

def staircase(n, X):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return sum(staircase(n - x, X) for x in X)

# This is again, very slow (O(|X|N)) since we are repeating computations again. We can use dynamic programming to speed it up.

# Each entry cache[i] will contain the number of ways we can get to step i with the set X. Then, we'll build up the array from zero using the same recurrence as before:

def staircase(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]

# This now takes O(N * |X|) time and O(N) space.


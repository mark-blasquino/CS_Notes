""" 
In a city-state of n people, there is a rumor going around that 
one of the n people is a spy for the neighboring city-state.

The spy, if it exists:

Does not trust anyone else.
Is trusted by everyone else (he's good at his job).
Works alone; there are no other spies in the city-state.
You are given a list of pairs, trust. Each trust[i] = [a, b] 
represents the fact that person a trusts person b.

If the spy exists and can be found, return their identifier. 
Otherwise, return -1.

Example 1:

Input: n = 2, trust = [[1, 2]]
Output: 2
Explanation: Person 1 trusts Person 2, but Person 2 does not 
trust Person 1, so Person 2 is the spy.
"""

def uncover_spy(n, trust):
    trusted = [0 for i in range(n + 1)]
    for i, j in trust:
        trusted[i] -= 1
        trusted[j] += 1
    for i in range(1, len(trusted)):
        if trusted[i] == n-1:
            return i
    
    return -1
def createHash(fib_seq, maxElement):
    prev, curr = 0, 1
    fib_seq.add(prev)
    fib_seq.add(curr)
    
    while (curr < maxElement):
        temp = curr + prev
        fib_seq.add(temp)
        prev = curr
        curr = temp

def fibonacciSimpleSum2(n):
    fib_seq = set()
    createHash(fib_seq, n)
    
    for i in range(n):
        if (i in fib_seq and (n-i) in fib_seq):
            # return (i, ", ", (n-i))
            return True
        else:
            return False

n = 11
print(fibonacciSimpleSum2(n))
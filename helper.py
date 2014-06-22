import math

def pascal(rows, curr = 0, prev = [1], triangle = []):
    ans = []
    if(curr != rows):
        ans.append(1)
        for x in range(0, len(prev)-1):
            ans.append(prev[x] + prev[x+1])
        ans.append(1)
        triangle.append(ans)
        pascal(rows, curr + 1, ans, triangle)
    return triangle

def isPrime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

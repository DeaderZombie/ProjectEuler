def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def Prob2(max):
    answer = 0
    currentFib = 1
    while int(fib(currentFib)) < max:
        if int(fib(currentFib))%2 == 0:
            answer += int(fib(currentFib))
        currentFib += 1
    return answer

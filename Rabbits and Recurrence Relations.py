def fib(n, k):
    s = [0, 1]
    if n == 2:
        return (1)
    else:
        for i in range(2, n + 1):
            s.append(s[i - 1] + k * s[i - 2])
            print(s)
        return (s[-1])


n, k = map(int, input().split())
print(fib(n, k))

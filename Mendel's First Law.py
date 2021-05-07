k, m, n = map(int, input().split())
s = k + m + n
print(k / (k + m + n) + k * m / ((k + m + n) * (k + m + n - 1)) + 3 * m * (m - 1) / (
            (4 * k + 4 * m + 4 * n) * (k + m + n - 1)) + 2 * m * n / (
                  (2 * k + 2 * m + 2 * n) * (k + m + n - 1)) + n * k / ((k + m + n) * (k + m + n - 1)))

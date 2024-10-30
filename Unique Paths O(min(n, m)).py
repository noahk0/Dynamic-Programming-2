def uniquePaths(self, m: int, n: int) -> int:
    path = 1

    for i in range(max(m, n), m + n - 1):
        path *= i

    for i in range(2, min(m, n)):
        path //= i

    return path

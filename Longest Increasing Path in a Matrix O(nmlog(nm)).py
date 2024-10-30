def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    longest, idx, path = 1, defaultdict(list), [[1] * len(matrix[0]) for _ in range(len(matrix))]

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            idx[matrix[x][y]].append((x, y))

    for i in sorted(idx.keys())[1:]:
        for x, y in idx[i]:
            sub = 0

            if x and matrix[x - 1][y] < matrix[x][y]:
                sub = max(sub, path[x - 1][y])

            if y and matrix[x][y - 1] < matrix[x][y]:
                sub = max(sub, path[x][y - 1])

            if x + 1 < len(matrix) and matrix[x + 1][y] < matrix[x][y]:
                sub = max(sub, path[x + 1][y])
                
            if y + 1 < len(matrix[0]) and matrix[x][y + 1] < matrix[x][y]:
                sub = max(sub, path[x][y + 1])

            path[x][y] += sub
            longest = max(longest, path[x][y])

    return longest

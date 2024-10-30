def numDistinct(self, s: str, t: str) -> int:
    start, count_t = '', Counter(t)

    for c in s:
        if c in count_t:
            start += c

    if t == start:
        return 1

    if not count_t <= Counter(start):
        return 0

    pre = [1] * len(start)

    for target in t:
        new = [0]

        for i in range(len(start)):
            new.append(new[-1])

            if target == start[i]:
                new[-1] += pre[i]

        pre = new

    return new[-1]

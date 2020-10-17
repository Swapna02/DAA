def optimal_summands(n):
    summands = []
    for i in range(1, n + 1):
        n -= i
        if n <= i:
            summands.append(n + i)
            break
        elif n == 0:
            summands.append(i)
            break
        else:
            summands.append(i)
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    a=len(summands)
    print(a)
    print(summands[a-2],summands[a-1])

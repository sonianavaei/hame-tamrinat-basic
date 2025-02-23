n = int(input())
for i in range(n):
    if i < n // 2 + 1:
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1) + ' ' * (n // 2) + ' ' * (n // 2 - i) + '*' * (2 * i + 1))
    else:
        print(' ' * (i - n // 2) + '*' * (2 * (n - i) - 1) + ' ' * (n // 2) + ' ' * (i - n // 2) + '*' * (2 * (n - i) - 1))

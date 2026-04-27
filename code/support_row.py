def support_row(n):
    row = [0] * (n * n)
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            row[a * b - 1] = 1
    return row


if __name__ == "__main__":
    for n in range(1, 7):
        print(n, support_row(n))

def support_row(n):
    """
    Return row n of the support triangle.

    T(n,k) = 1 iff k = a*b for some 1 <= a,b <= n,
    for 1 <= k <= n^2.
    """
    row = [0] * (n * n)

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            row[a * b - 1] = 1

    return row


if __name__ == "__main__":
    for n in range(1, 7):
        print(f"n={n}: {support_row(n)}")

def colored_support_row(n):
    """
    Return row n of the colored support / multiplicity triangle.

    T(n,k) counts ordered pairs (a,b) with 1 <= a,b <= n
    such that a*b = k, for 1 <= k <= n^2.
    """
    row = [0] * (n * n)

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            row[a * b - 1] += 1

    return row


if __name__ == "__main__":
    for n in range(1, 7):
        print(f"n={n}: {colored_support_row(n)}")

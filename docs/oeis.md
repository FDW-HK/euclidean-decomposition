# OEIS Sequences

This page collects OEIS entries related to the Euclidean decomposition of the multiplication table.

The common language is the master array

    A(n,q,r) = #{(i,j) : i*j = q*n + r},

with the precise indexing convention depending on the sequence.

## Accepted sequences

| OEIS | Description | Role |
|---|---|---|
| [A393470](https://oeis.org/A393470) | Triangle read by rows: T(n,k) is the number of ordered pairs (i,j) with 0 <= i,j < n such that floor((i*j)/n) = k. | Carry / quotient marginal of the zero-based master array. |
| [A393746](https://oeis.org/A393746) | Triangle read by rows: T(n,k) is the number of ordered pairs (i,j) with 0 <= i,j < n such that i*j = k*n. | r = 0 slice of the zero-based master array. |
| [A394016](https://oeis.org/A394016) | Triangle read by rows: T(n,k) = 1 if k appears in the n X n multiplication table, otherwise 0. | Positive-indexed support triangle. |
| [A395373](https://oeis.org/A395373) | Triangle read by rows: T(n,k) is the number of ordered pairs (x,y) with 1 <= x,y <= n such that x*y = k. | Positive-indexed multiplicity triangle / colored support. |
| [A395409](https://oeis.org/A395409) | a(n) = A033677(n) - A135034(n); excess of the smallest divisor of n >= sqrt(n) over ceiling(sqrt(n)). | This measures the gap between the square-root threshold and the least k such that n appears in the k X k multiplication table. |

## Allocated / in review

| OEIS | Status | Notes |
|---|---|---|
| - | Allocated | Reserved for a related sequence. |

## Relationship to the master array

For the positive-indexed version,

    A(n,q,r) = #{(i,j) : 1 <= i,j <= n and i*j = q*n + r}, 0 <= r < n.

Then the support triangle satisfies

    T(n,k) = 1 iff A(n, floor(k/n), k mod n) > 0,

and the colored support / multiplicity triangle satisfies

    T(n,k) = A(n, floor(k/n), k mod n).

For the zero-based version,

    A(n,q,r) = #{(i,j) : 0 <= i,j < n and i*j = q*n + r}, 0 <= r < n.

Then A393470 records the carry marginal

    T(n,k) = Sum_{r=0..n-1} A(n,k,r),

while A393746 records the r = 0 slice

    T(n,k) = A(n,k,0).

[Back to home](./)

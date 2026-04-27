# Euclidean Decomposition

This site is a public junction for the Euclidean decomposition of the multiplication table, its OEIS sequences, Zenodo papers, reproducibility code, and support visualizations.

For a fixed integer \(n\), multiplication table entries may be written as

    i*j = q*n + r,

where \(q\) is the quotient and \(r\) is the remainder. This gives rise to the master array

    A(n,q,r) = #{(i,j) : i*j = q*n + r}.

Different projections, slices, supports, and multiplicities of this array are recorded in OEIS and discussed in the linked papers.

## Sections

- [OEIS sequences](oeis.md)
- [Zenodo papers](papers.md)
- [Cloud chambers](cloud-chambers.md)
- [Code](code.md)
- [Notes](notes.md)

## Interactive visualizations

- [Memory stride visualization](widgets/stride.html)
- [Divisor window visualization](widgets/divisor-window.html)
- [Moving frame visualization](widgets/moving-frame.html)

## Repository

The source repository is available at [github.com/FDW-HK/euclidean-decomposition](https://github.com/FDW-HK/euclidean-decomposition).

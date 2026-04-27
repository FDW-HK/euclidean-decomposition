# Euclidean Decomposition

This repository collects code, visualizations, OEIS links, and notes related to the Euclidean decomposition of multiplication table entries.

## Website

Public site: [fdw-hk.github.io/euclidean-decomposition](https://fdw-hk.github.io/euclidean-decomposition/)

## Project links

- [OEIS sequences](oeis/sequences.md)
- [Zenodo papers](papers/zenodo.md)
- [Images](images/README.md)
- [Code](code/README.md)

For a fixed integer \(n\), multiplication table entries may be written in the form

    i*j = q*n + r,

where \(q\) is the quotient and \(r\) is the remainder. This gives rise to the master array

    A(n,q,r) = #{(i,j) : i*j = q*n + r}.

Different projections, slices, supports, and multiplicities of this array are recorded in the OEIS and discussed in the linked papers.

## Contents

- [OEIS sequences](oeis/sequences.md)
- [Zenodo papers](papers/zenodo.md)

## Visualizations

The support of the multiplication table can be arranged as a square-grid bitmap. These visualizations are informally called *cloud chambers* in this project.

## Status

This repository is an open junction for reproducibility code, visualizations, OEIS links, and notes connected to the study of the Euclidean decomposition of the multiplication table.

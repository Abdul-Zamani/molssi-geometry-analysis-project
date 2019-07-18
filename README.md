# MolSSI | Geometry Analysis Project + Testing

## geom_analysis.py

This program takes the molecular coordinates from an input file and calculates the bond distances between all atoms. There is a built-in conditional that performs a soft bond check using specific distance cutoff criteria (0-1.5 $\mathring A$).

```
3
Water xyz file
O        0.000000     -0.007156      0.965491
H1      -0.000000      0.001486     -0.003471
H2       0.000000      0.931026      1.207929
```

The code writes the calculated data into text file called water_distance_file.txt

## test_geom_analysis.py

This program contains unit tests on the functions defined in geom_analysis.py

```
collected 2 items

test_geom_analysis.py::test_calculate_distance PASSED                    [ 50%]
test_geom_analysis.py::test_bond_check PASSED                            [100%]
```

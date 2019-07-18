# MolSSI | Geometry Analysis Project + Testing

## geom_analysis.py

This program takes the molecular coordinates from an input file and calculates the bond distances between all atoms. There is a built-in conditional that performs a soft bond check using specific distance cutoff criteria (0-1.5 $\mathring A$).

## test_geom_analysis.py

This program contains unit tests on the functions defined in geom_analysis.py

```
collected 2 items

test_geom_analysis.py::test_calculate_distance PASSED                    [ 50%]
test_geom_analysis.py::test_bond_check PASSED                            [100%]
```

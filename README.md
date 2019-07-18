# MolSSI Summer School 2019
## Geometry Analysis Project + Testing

### geom_analysis.py

This program takes the molecular coordinates from an input file and calculates the bond distances between all atoms. There is a built-in conditional that performs a soft bond check using specific distance cutoff criteria (0-1.5 Angstroms).

The following is the contents of a water geometry input file:
```
3
Water xyz file
O        0.000000     -0.007156      0.965491
H1      -0.000000      0.001486     -0.003471
H2       0.000000      0.931026      1.207929
```

The code formats and writes the calculated bond lengths to a text file called distance_file.txt

Here are the results:

```
O - H1 | Atom Distance: 0.96900 Angstroms
O - H2 | Atom Distance: 0.96900 Angstroms
```

### test_geom_analysis.py

This program contains unit tests on the functions defined in geom_analysis.py

```
collected 2 items

test_geom_analysis.py::test_calculate_distance PASSED                    [ 50%]
test_geom_analysis.py::test_bond_check PASSED                            [100%]
```

The functions are determined to be stable.

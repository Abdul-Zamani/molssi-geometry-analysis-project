# MolSSI Summer School 2019
# Python Workshop
# Geometry Analysis Project | Unit Tests for Functions
# Updated: 7/18/19
# A.Zamani


# importing libraries

import pytest

# import program to test 
import geom_analysis as ga #abbreviate

# test bond distance function
def test_calculate_distance():
    
# provide coordinates    
    coord1 = [0, 0, 0]
    coord2 = [1, 0, 0]

# declare expected value
    expected = 1.0
#   expected = 1.5

# declare observed value
    observed = ga.calculate_distance(coord1,coord2)

# define assertion condition

    assert observed == expected

#
# to make the above test fail, change the expected value of calculate_distance (ex; expected = 1.5)
#

# test bond check function
def test_bond_check():
    expected = True   
    observed = ga.bond_check(5, min_d=3, max_d=6) #changing fxn arguments
    assert observed == expected
    
# Misc. Notes   
# Run pytest -v
# The “-v” flag stands for verbose. It tells pytest to print more information when it runs the tests.
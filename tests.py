import math

# Define factorial function as in the original code
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Define the permutation and combination functions
def calc_permutations(n, r):
    return factorial(n) // factorial(n - r)

def calc_combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# Test cases
def test_case_1():
    # Normal test case 1: n = 5, r = 3
    assert calc_permutations(5, 3) == 60, "Test Case 1 Permutations Failed"
    assert calc_combinations(5, 3) == 10, "Test Case 1 Combinations Failed"

def test_case_2():
    # Normal test case 2: n = 6, r = 2
    assert calc_permutations(6, 2) == 30, "Test Case 2 Permutations Failed"
    assert calc_combinations(6, 2) == 15, "Test Case 2 Combinations Failed"

def test_case_3():
    # Normal test case 3: n = 7, r = 5
    assert calc_permutations(7, 5) == 2520, "Test Case 3 Permutations Failed"
    assert calc_combinations(7, 5) == 21, "Test Case 3 Combinations Failed"

def test_edge_case_1():
    # Edge test case 1: n = 0, r = 0
    assert calc_permutations(0, 0) == 1, "Edge Test Case 1 Permutations Failed"
    assert calc_combinations(0, 0) == 1, "Edge Test Case 1 Combinations Failed"

def test_edge_case_2():
    # Edge test case 2: n = 1, r = 1
    assert calc_permutations(1, 1) == 1, "Edge Test Case 2 Permutations Failed"
    assert calc_combinations(1, 1) == 1, "Edge Test Case 2 Combinations Failed"

def test_edge_case_3():
    # Edge test case 3: n = 20, r = 0
    assert calc_permutations(20, 0) == 1, "Edge Test Case 3 Permutations Failed"
    assert calc_combinations(20, 0) == 1, "Edge Test Case 3 Combinations Failed"

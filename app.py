import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def calc_permutations(n, r):
    return (factorial)(n) // (factorial)((n - r))


def calc_combinations(n, r):
    return (factorial)(n) // ((factorial)(r) * (factorial)(n - r))

def main():
    while True:
        try:
            n = int(input("Enter the total number of items (n): "))
            if n < 0:
                raise ValueError("Please enter a non-negative integer for n.")
            break 
        except ValueError as e:
            print(e)  

    while True:
        try:
            r = int(input("Enter the items to be chosen or arranged (r): "))
            if r < 0:
                raise ValueError("Please enter a non-negative integer for r.")
            if r > n:
                raise ValueError("r cannot be greater than n.")
            break  
        except ValueError as e:
            print(e)  

    permutations = calc_permutations(n, r)
    combinations = calc_combinations(n, r)

    print(f"Permutations: {permutations}")
    print(f"Combinations: {combinations}")

if __name__ == "__main__":
    main()


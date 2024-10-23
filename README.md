# Calculateing Permutations and Combinations

## Author: Katrina Hill

## Description
This is an application that calculates permutations and combinations based on user input. The application allows the user to enter the values for n (total items) and r (items to be chosen or arranged) and then displays the results to the terminal.

## Features
- Factorial Calculation: Computes the factorial of a non-negative integer using a recursive approach.
- Permutations Calculation: Calculates the number of permutations for a given set of items, providing the total arrangements possible when selecting a subset of items.
- Combinations Calculation: Computes the number of combinations for selecting items from a larger set without regard to order.
- User Input: Allows users to easily input the total number of items and the number of items to choose or arrange through a simple command-line interface.
- Results Display: Outputs the calculated permutations and combinations in a clear and formatted manner for user understanding.

## Files
- `app.py`: The main program that performs the base conversions.
- `tests.py`: A suite of tests for validating the functionality of the logical operations.

## Requirements
- Python 3.11

## How to Run
1. **Clone the repository** (or download the files):
   - git clone https://github.com/katrina-l-hill/calc_permutations_combinations.git
   - cd into the repository directory
2. **Run the Main program**:
   - run python app.py to run the program
   - The first prompt will be to enter the total number of items (n)
     - Press enter after entering the number
   - The second prompt will be to enter the items to be chosen or arranged (r)
    - Press enter after entering the number
3. **Run the tests**:
   - run python -m pytest tests.py to run the tests
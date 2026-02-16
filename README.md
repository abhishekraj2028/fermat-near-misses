# Fermat's Last Theorem - Near Misses

## What it does
Searches for near misses to Fermat's Last Theorem. Finds x, y, z where x^n + y^n is really close to z^n but not exactly equal. The program asks for n (exponent) and k (upper limit), then checks all combinations and prints the smallest misses it finds.

## How to run

### Option 1: Run with Python
Make sure you have Python 3 installed. No extra libraries needed.
```
python fermat_near_misses.py
```

### Option 2: Run the executable
```
./fermat_near_misses.exe
```

## What to expect
1. Program asks you to enter n (between 3 and 11)
2. Program asks you to enter k (greater than 10)
3. It searches through all x, y combos from 10 to k
4. Prints each new smallest near miss as it finds them
5. Shows the overall smallest miss at the end
6. Press Enter to exit

## Example
```
Enter n (3 to 11): 3
Enter k (must be greater than 10): 20

Searching with n=3, k=20
x and y range: 10 to 20
-------------------------------------------

New best miss found!
  x=10, y=10, z=13
  x^n + y^n = 2000
  z^n = 2197
  Miss: 197
  Relative miss: 9.850000%

...

FINAL RESULT (smallest miss found):
-------------------------------------------
  x = 18
  y = 20
  z = 24
  n = 3
  Actual miss = 8
  Relative miss = 0.057837%
```

## Files
- `fermat_near_misses.py` - source code
- `fermat_near_misses.exe` - executable
- `README.md` - this file

## Author
Abhishek - abhishekrajanandma@lewisu.edu

Software Engineering (CRN: 11178) - Lewis University

# ============================================================
# Title: Fermat's Last Theorem - Near Misses
# File: fermat_near_misses.py
# External files needed: None
# External files created: None
# Programmer: Abhishek
# Email: abhishekrajanandma@lewisu.edu
# Course: Software Engineering (CRN: 11178)
# Date: 02/15/2026
# Description: This program finds near misses for Fermat's
#   Last Theorem. User gives n and k, then it checks all
#   x,y combos from 10 to k and finds z where x^n + y^n
#   is closest to z^n. Prints smallest misses as it finds them.
# Resources: Assignment description, Python docs
# ============================================================

import math

# getting n and k from user with validation
def get_input():
    print("Fermat's Last Theorem - Near Misses Finder")
    print("-------------------------------------------")
    print()

    # keep asking until valid n
    while True:
        try:
            n = int(input("Enter n (3 to 11): "))
            if n >= 3 and n <= 11:
                break
            print("n has to be between 3 and 11")
        except:
            print("please enter a number")

    # keep asking until valid k
    while True:
        try:
            k = int(input("Enter k (must be greater than 10): "))
            if k > 10:
                break
            print("k has to be more than 10")
        except:
            print("please enter a number")

    return n, k


# finds z where z^n is just below the target
def get_z(target, n):
    # use nth root to estimate z
    z = int(target ** (1.0 / n))

    # fix floating point errors
    while (z + 1) ** n <= target:
        z = z + 1
    while z ** n > target:
        z = z - 1

    return z


# calculates how close x^n + y^n is to z^n
def calc_miss(x, y, z, n):
    total = x**n + y**n  # x^n + y^n
    lower = z**n         # z^n
    upper = (z+1)**n     # (z+1)^n

    # difference from both sides
    miss1 = total - lower   # how far above z^n
    miss2 = upper - total   # how far below (z+1)^n

    # pick the closer one
    if miss1 <= miss2:
        miss = miss1
        closest_z = z
    else:
        miss = miss2
        closest_z = z + 1

    # relative miss = miss divided by total
    rel_miss = miss / total
    return miss, rel_miss, closest_z


# main search - goes through all x,y combos
def search(n, k):
    best_rel_miss = float('inf')  # starts as infinity
    best = None  # stores best result

    print()
    print(f"Searching with n={n}, k={k}")
    print(f"x and y range: 10 to {k}")
    print("-------------------------------------------")
    print()

    # loop through all x values
    for x in range(10, k + 1):
        # loop through all y values
        for y in range(10, k + 1):

            total = x**n + y**n

            # find z that brackets the total
            z = get_z(total, n)

            if z <= 0:
                continue

            # get the miss for this combo
            miss, rel_miss, closest_z = calc_miss(x, y, z, n)

            # if this is better than what we had, print it
            if rel_miss < best_rel_miss:
                best_rel_miss = rel_miss
                best = (x, y, closest_z, miss, rel_miss)

                print(f"New best miss found!")
                print(f"  x={x}, y={y}, z={closest_z}")
                print(f"  x^n + y^n = {total}")
                print(f"  z^n = {closest_z**n}")
                print(f"  Miss: {miss}")
                print(f"  Relative miss: {rel_miss*100:.6f}%")
                print()

    # done searching, print final result
    print("-------------------------------------------")
    print("FINAL RESULT (smallest miss found):")
    print("-------------------------------------------")
    if best:
        x, y, z, miss, rel_miss = best
        print(f"  x = {x}")
        print(f"  y = {y}")
        print(f"  z = {z}")
        print(f"  n = {n}")
        print(f"  Actual miss = {miss}")
        print(f"  Relative miss = {rel_miss*100:.6f}%")
    else:
        print("  No near misses found")
    print("-------------------------------------------")


# run the program
def main():
    n, k = get_input()
    search(n, k)
    print()
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

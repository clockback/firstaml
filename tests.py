"""
Test scripts in parcel.py.
Licensed under the GPLv3.0
Author: Elliot Ilya Simpson
"""

import parcel

test_parcels = [
    parcel.Parcel(4, 7, 9.5, 0.5),
    parcel.Parcel(10, 7, 9.5, 4),
    parcel.Parcel(40, 56, 9.5, 5),
    parcel.Parcel(40, 56, 100, 60)
]

# Testing that the task 1 function for testing parcel costs works.
test_results = parcel.generate_billing_t1(test_parcels)

assert test_results[test_parcels[0]] == 3
assert test_results[test_parcels[1]] == 8
assert test_results[test_parcels[2]] == 15
assert test_results[test_parcels[3]] == 25

# Testing that the task 2 function for testing parcel costs works.
test_results = parcel.generate_billing_t2(test_parcels, True)

assert test_results[test_parcels[0]] == 3
assert test_results[test_parcels[1]] == 8
assert test_results[test_parcels[2]] == 15
assert test_results[test_parcels[3]] == 25
assert test_results["Speedy delivery"] == 3 + 8 + 15 + 25  # 51

# Testing that the task 3 function for testing parcel costs works.
test_results = parcel.generate_billing_t3(test_parcels, True)

assert test_results[test_parcels[0]] == 3
assert test_results[test_parcels[1]] == 10
assert test_results[test_parcels[2]] == 15
assert test_results[test_parcels[3]] == 125
assert test_results["Speedy delivery"] == 3 + 10 + 15 + 125  # 153

# Testing that the task 4 function for testing parcel costs works.
test_parcels.append(parcel.Parcel(40, 56, 100, 45))
test_results = parcel.generate_billing_t4(test_parcels, True)

assert test_results[test_parcels[0]] == (3, False)
assert test_results[test_parcels[1]] == (10, False)
assert test_results[test_parcels[2]] == (15, False)
assert test_results[test_parcels[3]] == (60, True)
assert test_results[test_parcels[4]] == (50, True)
assert test_results["Speedy delivery"] == 3 + 10 + 15 + 60 + 50  # 138

print("Tests completed.")

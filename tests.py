"""
Test scripts in parcel.py.
Licensed under the GPLv3.0
Author: Elliot Ilya Simpson
"""

import parcel

test_parcels = [
    parcel.Parcel(4, 7, 9.5),
    parcel.Parcel(10, 7, 9.5),
    parcel.Parcel(40, 56, 9.5),
    parcel.Parcel(40, 56, 100)
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

print("Tests completed.")

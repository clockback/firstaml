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

test_results = parcel.generate_billing(test_parcels)

# Testing that the function for testing parcel costs works.
assert test_results[test_parcels[0]] == 3
assert test_results[test_parcels[1]] == 8
assert test_results[test_parcels[2]] == 15
assert test_results[test_parcels[3]] == 25


print("Tests completed.")

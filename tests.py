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

assert test_results[test_parcels[0]] == (3, 'Small')
assert test_results[test_parcels[1]] == (8, 'Medium')
assert test_results[test_parcels[2]] == (15, 'Large')
assert test_results[test_parcels[3]] == (25, 'XL')

# Testing that the task 2 function for testing parcel costs works.
test_results = parcel.generate_billing_t2(test_parcels, True)

assert test_results[test_parcels[0]] == (3, 'Small')
assert test_results[test_parcels[1]] == (8, 'Medium')
assert test_results[test_parcels[2]] == (15, 'Large')
assert test_results[test_parcels[3]] == (25, 'XL')
assert test_results["Speedy delivery"] == 3 + 8 + 15 + 25  # 51

# Testing that the task 3 function for testing parcel costs works.
test_results = parcel.generate_billing_t3(test_parcels, True)

assert test_results[test_parcels[0]] == (3, 'Small')
assert test_results[test_parcels[1]] == (10, 'Medium')
assert test_results[test_parcels[2]] == (15, 'Large')
assert test_results[test_parcels[3]] == (125, 'XL')
assert test_results["Speedy delivery"] == 3 + 10 + 15 + 125  # 153

# Testing that the task 4 function for testing parcel costs works.
test_parcels.append(parcel.Parcel(40, 56, 100, 45))
test_results = parcel.generate_billing_t4(test_parcels, True)

assert test_results[test_parcels[0]] == (3, 'Small')
assert test_results[test_parcels[1]] == (10, 'Medium')
assert test_results[test_parcels[2]] == (15, 'Large')
assert test_results[test_parcels[3]] == (60, 'Heavy')
assert test_results[test_parcels[4]] == (50, 'Heavy')
assert test_results["Speedy delivery"] == 3 + 10 + 15 + 60 + 50  # 138

print("Tests completed.")

# Testing that the task 5 function for testing parcel costs works.
test_results = parcel.generate_billing_t5(test_parcels, True)

assert test_results[test_parcels[0]] == (3, 'Small')
assert test_results[test_parcels[1]] == (10, 'Medium')
assert test_results[test_parcels[2]] == (15, 'Large')
assert test_results[test_parcels[3]] == (60, 'Heavy')
assert test_results[test_parcels[4]] == (50, 'Heavy')
assert test_results["Speedy delivery"] == 3 + 10 + 15 + 60 + 50  # 138

print("Tests completed.")

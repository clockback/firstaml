"""
Test scripts in parcel.py.
Licensed under the GPLv3.0
Author: Elliot Ilya Simpson
"""

import parcel

# Testing that the function for testing parcel costs works.
assert parcel.parcel_cost(4, 7, 9.5) == 3
assert parcel.parcel_cost(10, 7, 9.5) == 8
assert parcel.parcel_cost(40, 56, 9.5) == 15
assert parcel.parcel_cost(40, 56, 100) == 25

print("Tests completed.")

"""FirstAML parcel project for calculating parcel postage.
Licensed under the GPLv3.0
Author: Elliot Ilya Simpson
"""


from typing import Dict, List, NamedTuple, Union


__all__ = [
    'Parcel',
    'parcel_cost',
    'generate_billing_t1',
    'generate_billing_t2'
]


class Parcel(NamedTuple):
    width: float
    length: float
    height: float


def parcel_cost(p: Parcel) -> int:
    """Calculates the cost to send a parcel according to the parcel's
    size.
    :param Parcel p: The parcel for which the cost is being
        calculated.
    :return: The cost in New Zealand dollars to send the parcel.
    :rtype: int
    """
    # Finds the largest dimension of the given parcel.
    max_dimension = max((p.width, p.length, p.height))

    if max_dimension < 10:
        return 3
    elif max_dimension < 50:
        return 8
    elif max_dimension < 100:
        return 15
    else:
        return 25


def generate_billing_t1(parcels: List[Parcel]) -> Dict[Parcel, int]:
    """Calculates the cost of each parcel within a list of parcels.
    Used for Task 1 of FirstAML assignment.
    :param List[Parcel] parcels: A list of parcels to be posted.
    :return: A dictionary mapping each parcel to its postage cost.
    :rtype: Dict[Parcel, int]
    """
    return {p: parcel_cost(p) for p in parcels}


def generate_billing_t2(
        parcels: List[Parcel], speedy: bool = False
) -> Dict[Union[Parcel, str], int]:
    """Calculates the cost of each parcel within a list of parcels,
    allowing for speedy delivery at a doubled cost.
    Used for Task 2 of FirstAML assignment.
    :param List[Parcel] parcels: A list of parcels to be posted.
    :param bool speedy: Whether or not extra is being spent for faster
        delivery.
    :return: A dictionary mapping each parcel to its postage cost.
    :rtype: Dict[Parcel, int]
    """
    # Calculates the cost of sending the individual parcels normally.
    initial_billing = generate_billing_t1(parcels)

    # If speedy billing is requested, returns the cost thereof as being
    # equal to the cost of all other parcel postage total, thus
    # doubling the price.
    if speedy:
        return {
            **initial_billing, "Speedy delivery": sum(initial_billing.values())
        }

    # Returns the same billing as specified in task one if speedy
    # delivery not requested.
    else:
        return initial_billing

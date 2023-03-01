"""FirstAML parcel project for calculating parcel postage.
Licensed under the GPLv3.0
Author: Elliot Ilya Simpson
"""


from typing import Dict, List, NamedTuple


__all__ = [
    'Parcel',
    'parcel_cost',
    'generate_billing'
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
    max_dimension = max((p.width, p.length, p.height))

    if max_dimension < 10:
        return 3
    elif max_dimension < 50:
        return 8
    elif max_dimension < 100:
        return 15
    else:
        return 25


def generate_billing(parcels: List[Parcel]) -> Dict[Parcel, int]:
    """Calculates the cost of each parcel within a list of parcels.
    :param List[Parcel] parcels: A list of parcels to be posted.
    :return: A dictionary mapping each parcel to its postage cost.
    :rtype: Dict[Parcel, int]
    """
    return {p: parcel_cost(p) for p in parcels}


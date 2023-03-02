"""FirstAML parcel project for calculating parcel postage.
Licensed under the GPLv3.0
Author: Elliot Ilya Simpson
"""


from typing import Dict, List, NamedTuple, Union


__all__ = [
    'Parcel',
    'parcel_cost',
    'generate_billing_t1',
    'generate_billing_t2',
    'generate_billing_t3'
]


class Parcel(NamedTuple):
    """Parcel properties:
    width: cm
    length: cm
    height: cm
    weight: kg
    """
    width: float
    length: float
    height: float
    weight: float


def parcel_cost(p: Parcel, consider_weight: bool = True) -> float:
    """Calculates the cost to send a parcel according to the parcel's
    size.
    :param Parcel p: The parcel for which the cost is being
        calculated.
    :param bool consider_weight: Whether to penalize a heavy parcel
        with an increased cost.
    :return: The cost in New Zealand dollars to send the parcel.
    :rtype: float
    """
    # Finds the largest dimension of the given parcel.
    max_dimension = max((p.width, p.length, p.height))

    # Considers if the parcel is Small.
    if max_dimension < 10:
        excess_weight = max((p.weight - 1, 0)) if consider_weight else 0
        return 3 + excess_weight * 2

    # Considers if the parcel is Medium.
    elif max_dimension < 50:
        excess_weight = max((p.weight - 3, 0)) if consider_weight else 0
        return 8 + excess_weight * 2

    # Considers if the parcel is Large.
    elif max_dimension < 100:
        excess_weight = max((p.weight - 6, 0)) if consider_weight else 0
        return 15 + excess_weight * 2

    # Considers if the parcel is XL.
    else:
        excess_weight = max((p.weight - 10, 0)) if consider_weight else 0
        return 25 + excess_weight * 2


def generate_billing_t1(parcels: List[Parcel]) -> Dict[Parcel, float]:
    """Calculates the cost of each parcel within a list of parcels.
    Used for Task 1 of FirstAML assignment.
    :param List[Parcel] parcels: A list of parcels to be posted.
    :return: A dictionary mapping each parcel to its postage cost.
    :rtype: Dict[Parcel, float]
    """
    return {p: parcel_cost(p, consider_weight=False) for p in parcels}


def generate_billing_t2(
        parcels: List[Parcel], speedy: bool = False
) -> Dict[Union[Parcel, str], float]:
    """Calculates the cost of each parcel within a list of parcels,
    allowing for speedy delivery at a doubled cost.
    Used for Task 2 of FirstAML assignment.
    :param List[Parcel] parcels: A list of parcels to be posted.
    :param bool speedy: Whether or not extra is being spent for faster
        delivery.
    :return: A dictionary mapping each parcel to its postage cost.
    :rtype: Dict[Parcel, float]
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


def generate_billing_t3(
        parcels: List[Parcel], speedy: bool = False
) -> Dict[Union[Parcel, str], float]:
    """Calculates the cost of each parcel within a list of parcels,
    allowing for speedy delivery at a doubled cost, and also weight
    penalties.
    Used for Task 3 of FirstAML assignment.
    :param List[Parcel] parcels: A list of parcels to be posted.
    :param bool speedy: Whether or not extra is being spent for faster
        delivery.
    :return: A dictionary mapping each parcel to its postage cost.
    :rtype: Dict[Parcel, float]
    """
    # Calculates the cost of sending the individual parcels normally.
    initial_billing = {p: parcel_cost(p) for p in parcels}

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

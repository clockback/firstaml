"""FirstAML parcel project for calculating parcel postage.
Licensed under the GPLv3.0
Author: Elliot Ilya Simpson
"""


from typing import Dict, List, NamedTuple, Tuple, Union


__all__ = [
    'Parcel',
    'parcel_cost_default',
    'parcel_cost',
    'generate_billing_t1',
    'generate_billing_t2',
    'generate_billing_t3',
    'generate_billing_t5'
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


def parcel_cost_default(
        p: Parcel, consider_weight: bool = True
) -> Tuple[float, str]:
    """Calculates the cost to send a parcel according to the parcel's
    size, provided a Heavy parcel is not used.
    :param Parcel p: The parcel for which the cost is being
        calculated.
    :param bool consider_weight: Whether to penalize a heavy parcel
        with an increased cost.
    :return: The cost in New Zealand dollars to send the parcel and a
        code for the size.
    :rtype: Tuple[float, str]
    """
    # Finds the largest dimension of the given parcel.
    max_dimension = max((p.width, p.length, p.height))

    # Considers if the parcel is Small.
    if max_dimension < 10:
        excess_weight = max((p.weight - 1, 0)) if consider_weight else 0
        return 3 + excess_weight * 2, 'Small'

    # Considers if the parcel is Medium.
    elif max_dimension < 50:
        excess_weight = max((p.weight - 3, 0)) if consider_weight else 0
        return 8 + excess_weight * 2, 'Medium'

    # Considers if the parcel is Large.
    elif max_dimension < 100:
        excess_weight = max((p.weight - 6, 0)) if consider_weight else 0
        return 15 + excess_weight * 2, 'Large'

    # Considers if the parcel is XL.
    else:
        excess_weight = max((p.weight - 10, 0)) if consider_weight else 0
        return 25 + excess_weight * 2, 'XL'


def parcel_cost(p: Parcel) -> Tuple[float, str]:
    """Calculates the cost to send a parcel according to the parcel's
    size.
    :param Parcel p: The parcel for which the cost is being
        calculated.
    :return: The cost in New Zealand dollars to send the parcel, and
        whether or not the parcel should be sent as a heavy parcel.
    :rtype: Tuple[float, str]
    """
    # Calculates how much it would cost to post the parcel without
    # using a heavy parcel.
    default_cost_and_type = parcel_cost_default(p, True)

    # Calculates how much it would cost to post the parcel with a heavy
    # parcel.
    heavy_cost = max((50, p.weight))

    # Returns the optimal cost for the parcel, and whether or not it is
    # heavy.
    if default_cost_and_type[0] <= heavy_cost:
        return default_cost_and_type
    else:
        return heavy_cost, 'Heavy'


def generate_billing_t1(parcels: List[Parcel]) -> Dict[
    Parcel, Tuple[float, str]
]:
    """Calculates the cost of each parcel within a list of parcels.
    Used for Task 1 of FirstAML assignment.
    :param List[Parcel] parcels: A list of parcels to be posted.
    :return: A dictionary mapping each parcel to its postage cost.
    :rtype: Dict[Parcel, Tuple[float, str]]
    """
    return {
        p: parcel_cost_default(p, consider_weight=False) for p in parcels
    }


def generate_billing_t2(
        parcels: List[Parcel], speedy: bool = False
) -> Dict[Union[Parcel, str], Union[Tuple[float, str], float]]:
    """Calculates the cost of each parcel within a list of parcels,
    allowing for speedy delivery at a doubled cost.
    Used for Task 2 of FirstAML assignment.
    :param List[Parcel] parcels: A list of parcels to be posted.
    :param bool speedy: Whether or not extra is being spent for faster
        delivery.
    :return: A dictionary mapping each parcel to its postage cost and
        its parcel type.
    :rtype: Dict[Union[Parcel, str], Union[Tuple[float, str], float]]
    """
    # Calculates the cost of sending the individual parcels normally.
    initial_billing = generate_billing_t1(parcels)

    # If speedy billing is requested, returns the cost thereof as being
    # equal to the cost of all other parcel postage total, thus
    # doubling the price.
    if speedy:
        return {**initial_billing, "Speedy delivery": sum(
            map(lambda v: v[0], initial_billing.values())
        )}


    # Returns the same billing as specified in task one if speedy
    # delivery not requested.
    else:
        return initial_billing


def generate_billing_t3(
        parcels: List[Parcel], speedy: bool = False
) -> Dict[Union[Parcel, str], Union[Tuple[float, str], float]]:
    """Calculates the cost of each parcel within a list of parcels,
    allowing for speedy delivery at a doubled cost, and also weight
    penalties.
    Used for Task 3 of FirstAML assignment.
    :param List[Parcel] parcels: A list of parcels to be posted.
    :param bool speedy: Whether or not extra is being spent for faster
        delivery.
    :return: A dictionary mapping each parcel to its postage cost and
        parcel type.
    :rtype: Dict[Union[Parcel, str], Union[Tuple[float, str], float]]
    """
    # Calculates the cost of sending the individual parcels normally.
    initial_billing = {p: parcel_cost_default(p) for p in parcels}

    # If speedy billing is requested, returns the cost thereof as being
    # equal to the cost of all other parcel postage total, thus
    # doubling the price.
    if speedy:
        return {**initial_billing, "Speedy delivery": sum(
            map(lambda v: v[0], initial_billing.values())
        )}


    # Returns the same billing as specified in task one if speedy
    # delivery not requested.
    else:
        return initial_billing


def generate_billing_t4(
        parcels: List[Parcel], speedy: bool = False
) -> Dict[Union[Parcel, str], Union[Tuple[float, str], float]]:
    """Calculates the cost of each parcel within a list of parcels,
    allowing for speedy delivery at a doubled cost, and also weight
    penalties.
    Used for Task 4 of FirstAML assignment.
    :param List[Parcel] parcels: A list of parcels to be posted.
    :param bool speedy: Whether or not extra is being spent for faster
        delivery.
    :return: A dictionary mapping each parcel to its postage cost and
        parcel type.
    :rtype: Dict[Union[Parcel, str], Union[Tuple[float, str], float]]
    """
    # Calculates the cost of sending the individual parcels normally.
    initial_billing = {p: parcel_cost(p) for p in parcels}

    # If speedy billing is requested, returns the cost thereof as being
    # equal to the cost of all other parcel postage total, thus
    # doubling the price.
    if speedy:
        return {**initial_billing, "Speedy delivery": sum(
            map(lambda v: v[0], initial_billing.values())
        )}

    # Returns the same billing as specified in task one if speedy
    # delivery not requested.
    else:
        return initial_billing


def generate_billing_t5(
        parcels: List[Parcel], speedy: bool = False
) -> Dict[Union[Parcel, str], Union[Tuple[float, bool], float]]:
    """Calculates the cost of each parcel within a list of parcels,
    allowing for speedy delivery at a doubled cost, weight penalties,
    Heavy packages, and discounts.
    TODO: Improve so that heavy package not chosen if it results in
        inferior discount results.
    Used for Task 5 of FirstAML assignment.
    :param List[Parcel] parcels: A list of parcels to be posted.
    :param bool speedy: Whether or not extra is being spent for faster
        delivery.
    :return: A dictionary mapping each parcel to its postage cost and
        parcel type.
    :rtype: Dict[Union[Parcel, str], Union[Tuple[float, str], float]]
    """
    # Calculates the cost of sending the individual parcels normally.
    initial_billing = {p: parcel_cost(p) for p in parcels}

    for billing_section, (cost, parcel_type) in initial_billing.items():
        print(billing_section, cost, parcel_type)

    # Prepares to assess the billing in order.
    ordered_billing = []
    item_pos = 0

    # Order the parcels as optimally as possible.
    while initial_billing:
        if (item_pos + 1) % (4 * 3) == 0:
            ordered_billing.append(
                get_cheapest_small_or_medium(initial_billing)
            )

        elif (item_pos + 1) % 4 == 0:
            ordered_billing.append(get_cheapest_small(initial_billing))

        elif (item_pos + 1) % 3 == 0:
            ordered_billing.append(get_cheapest_medium(initial_billing))

        elif (item_pos + 1) % 5 == 0:
            ordered_billing.append(get_cheapest(initial_billing))

        else:
            ordered_billing.append(
                initial_billing.pop(next(iter(initial_billing)))
            )

    # Generates an intermediate billing record.
    intermediate_billing = {}

    # TODO: Fill in the ordered billing section.
    for billing_section in ordered_billing:
        pass

    # If speedy billing is requested, returns the cost thereof as being
    # equal to the cost of all other parcel postage total, thus
    # doubling the price.
    if speedy:
        return {**intermediate_billing, "Speedy delivery": sum(
            map(lambda v: v[0], intermediate_billing.values())
        )}

    # Returns the same billing as specified in task one if speedy
    # delivery not requested.
    else:
        return intermediate_billing

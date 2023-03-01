"""
FirstAML parcel project for calculating parcel postage.
Licensed under the GPLv3.0
Author: Elliot Ilya Simpson
"""


def parcel_cost(width: float, length: float, height: float) -> int:
    """
    Calculates the cost to send a parcel according to the parcel's
    size.
    :param float width: The width of the parcel in centimetres.
    :param float length: The length of the parcel in centimetres.
    :param float height: The height of the parcel in centimetres.
    :return: The cost in New Zealand dollars to send the parcel.
    :rtype: int
    """
    max_dimension = max((width, length, height))

    if max_dimension < 10:
        return 3
    elif max_dimension < 50:
        return 8
    elif max_dimension < 100:
        return 15
    else:
        return 25


__all__ = [
    parcel_cost
]

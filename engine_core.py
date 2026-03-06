# engine_core.py

VERSION = "1.0.0"

POINT_RATE = 25  # 25 THB = 1 point


def get_version():
    return VERSION


def calculate_points(amount_thb):
    """
    Calculate reward points from purchase amount (THB)
    """
    base_points = amount_thb // POINT_RATE
    bonus = 0

    if amount_thb >= 10000:
        bonus = 150
    elif amount_thb >= 5000:
        bonus = 50

    return int(base_points + bonus)
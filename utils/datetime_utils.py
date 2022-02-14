from datetime import datetime

# Initializes the season intervals (closed on left, open on right):
#   [ start date, end date )   =>   start date <= x < end date
CURRENT_YEAR = datetime.now().year

SPRING_START_DATE = datetime(CURRENT_YEAR, 3, 19)
SPRING_END_DATE = datetime(CURRENT_YEAR, 6, 20)

SUMMER_START_DATE = SPRING_END_DATE
SUMMER_END_DATE = datetime(CURRENT_YEAR, 9, 22)

FALL_START_DATE = SUMMER_END_DATE
FALL_END_DATE = datetime(CURRENT_YEAR, 12, 20)

WINTER_START_DATE = FALL_END_DATE
WINTER_END_DATE = SPRING_START_DATE


def datetime_to_season(datetime_obj: datetime) -> str:
    """ Transforms a datetime object into a season.

    If `datetime_obj` is not an instance of `datetime`,
    it raises a `TypeError`.

    :param datetime_obj: The datetime to transform.
    :return: The season in a string.
    """
    if not isinstance(datetime_obj, datetime):
        raise TypeError("Invalid parameter: it must be a `datetime` object.")

    datetime_obj = datetime.fromtimestamp(datetime_obj.timestamp()) \
        .replace(year=CURRENT_YEAR)

    if SPRING_START_DATE <= datetime_obj < SPRING_END_DATE:
        return "Spring"
    elif SUMMER_START_DATE <= datetime_obj < SUMMER_END_DATE:
        return "Summer"
    elif FALL_START_DATE <= datetime_obj < FALL_END_DATE:
        return "Fall"
    # The only option left is winter, return directly without
    # doing the comparison.
    return "Winter"

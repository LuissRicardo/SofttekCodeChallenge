from datetime import datetime
from unittest import TestCase

import utils.datetime_utils as du


class DatetimeUtilsTestcase(TestCase):
    """ Unit testing for the file `utils/datetime_utils.py` """

    def test_CURRENT_YEAR(self):
        self.assertEqual(du.CURRENT_YEAR, datetime.now().year)

    def test_SPRING_START_DATE(self):
        self.assertEqual(du.SPRING_START_DATE,
                         datetime(datetime.now().year, 3, 19))

    def test_SPRING_END_DATE(self):
        self.assertEqual(du.SPRING_END_DATE,
                         datetime(datetime.now().year, 6, 20))

    def test_SUMMER_START_DATE(self):
        self.assertEqual(du.SUMMER_START_DATE,
                         datetime(datetime.now().year, 6, 20))

    def test_SUMMER_END_DATE(self):
        self.assertEqual(du.SUMMER_END_DATE,
                         datetime(datetime.now().year, 9, 22))

    def test_FALL_START_DATE(self):
        self.assertEqual(du.FALL_START_DATE,
                         datetime(datetime.now().year, 9, 22))

    def test_FALL_END_DATE(self):
        self.assertEqual(du.FALL_END_DATE,
                         datetime(datetime.now().year, 12, 20))

    def test_WINTER_START_DATE(self):
        self.assertEqual(du.WINTER_START_DATE,
                         datetime(datetime.now().year, 12, 20))

    def test_WINTER_END_DATE(self):
        self.assertEqual(du.WINTER_END_DATE,
                         datetime(datetime.now().year, 3, 19))

    def test_date_to_season(self):
        # Spring season
        self.assertEqual(du.datetime_to_season(datetime(1980, 3, 19)),
                         "Spring")
        self.assertEqual(du.datetime_to_season(datetime(2050, 6, 19)),
                         "Spring")
        self.assertEqual(du.datetime_to_season(datetime(2022, 4, 19)),
                         "Spring")

        # Summer season
        self.assertEqual(du.datetime_to_season(datetime(1980, 6, 20)),
                         "Summer")
        self.assertEqual(du.datetime_to_season(datetime(2050, 9, 21)),
                         "Summer")
        self.assertEqual(du.datetime_to_season(datetime(2022, 8, 5)),
                         "Summer")

        # Fall season
        self.assertEqual(du.datetime_to_season(datetime(1980, 9, 22)),
                         "Fall")
        self.assertEqual(du.datetime_to_season(datetime(2050, 12, 19)),
                         "Fall")
        self.assertEqual(du.datetime_to_season(datetime(2022, 11, 5)),
                         "Fall")

        # Winter season
        self.assertEqual(du.datetime_to_season(datetime(1980, 12, 20)),
                         "Winter")
        self.assertEqual(du.datetime_to_season(datetime(2050, 3, 18)),
                         "Winter")
        self.assertEqual(du.datetime_to_season(datetime(2022, 3, 5)),
                         "Winter")

    def test_date_to_season_must_fail(self):
        self.assertRaises(TypeError, du.datetime_to_season, "must fail")
        self.assertRaises(TypeError, du.datetime_to_season, 123)
        self.assertRaises(TypeError, du.datetime_to_season, True)

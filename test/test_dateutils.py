from unittest import TestCase
from datetime import date
from dateutils import DateInterval, get_last_friday


class DateIntervalTest(TestCase):
    def test_lclose_rclose(self):
        date_interval = DateInterval('2017-07-01', '2017-07-02')

        self.assertEqual(date_interval.days_between(lclose=False, rclose=False), 0)
        self.assertEqual(date_interval.days_between(lclose=True, rclose=False), 1)
        self.assertEqual(date_interval.days_between(lclose=True, rclose=True), 2)
        self.assertEqual(date_interval.days_between(lclose=False, rclose=True), 1)


class GetLastFriday(TestCase):

    def test_last_friday(self):
        day = date(2017, 8, 1)
        self.assertEqual(get_last_friday(day), date(2017, 7, 28))

        day = date(2017, 8, 4)
        self.assertEqual(get_last_friday(day), date(2017, 7, 28))



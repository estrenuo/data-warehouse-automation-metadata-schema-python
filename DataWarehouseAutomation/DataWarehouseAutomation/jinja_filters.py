""" Extend jinja with filters to support the DataWarehouseAutomation
"""
import datetime
import random
#from typing import List

class JinjaFilters:
    """_summary_
    """

    def wrap(self, before_string: str, after_string: str) -> str:
        """_summary_

        Args:
            string_to_wrap (str): _description_
            before_string (str): _description_
            after_string (str): _description_

        Returns:
            str: _description_
        """
        return before_string + self + after_string

    def get_random_number(self, max_number: int) -> int:
        """_summary_

        Args:
            max_number (int): _description_

        Raises:
            ValueError: _description_

        Returns:
            int: _description_
        """
        if max_number < 1:
            raise ValueError("The maximum number value should be greater than 1")

        seed = random.randint(1, 2**31 - 1)
        r = random.Random(seed)
        return r.randint(1, max_number)

    def get_random_date(self, start_year: int = 1995) -> datetime.date:
        """_summary_

        Args:
            start_year (int, optional): _description_. Defaults to 1995.

        Returns:
            datetime.date: _description_
        """
        start = datetime.date(start_year, 1, 1)
        end = datetime.date.today()
        days_range = (end - start).days
        seed = random.randint(1, 2**31 - 1)
        random_days = random.Random(seed).randint(1, days_range)
        random_seconds = random.Random(seed).randint(1, 86400)
        random_date = start + datetime.timedelta(days=random_days, seconds=random_seconds)
        return random_date.date()

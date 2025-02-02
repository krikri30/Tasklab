class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

        self.is_valid_date(self._day, self._month, self._year)

    # TODO какой декоратор следует применить?
    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        leap_condition = ((year % 4) == 0 and (year % 100) != 0) or ((year % 400) == 0)
        return leap_condition
        # TODO записать условие проверки високосного года

    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        year_months_index = 0 if not self.is_leap_year(year) else 1
        year_months = self.DAY_OF_MONTH[year_months_index]

        return year_months[month - 1]
        # TODO вернуть количество дней указанного месяца

    def is_valid_date(self, day: int, month: int, year: int) -> None:
        """Проверяет, является ли дата корректной"""
        if day > self.get_max_day(month, year):
            raise ValueError

    @property
    def day(self) -> int:
        return self._day
        # TODO если указанный набор день, месяц и год неверны, то вызвать ошибку ValueError

    # TODO записать getter и setter для дня
    @day.setter
    def day(self, day: int) -> None:
        if not isinstance(day, int):
            raise TypeError
        if not 1 <= day <= 31:
            raise ValueError
        self._day = day

    @property
    def month(self) -> int:
        return self._month

    # TODO записать getter и setter для месяца
    @month.setter
    def month(self, month: int) -> None:
        if not isinstance(month, int):
            raise TypeError
        if not 1 <= month <= 12:
            raise ValueError
        self._month = month

    @property
    def year(self) -> int:
        return self._year

    # TODO записать getter и setter для года
    @year.setter
    def year(self, year: int) -> None:
        if not isinstance(year, int):
            raise TypeError
        if year <= 0:
            raise ValueError
        self._year = year

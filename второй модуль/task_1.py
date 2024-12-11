# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Chest:
    def __int__(self, capacity_volume: float, occupied_volume: float):
        """
        :param capacity_volume: Объем сундука
        :param occupied_volume: Объем занемаемого места в сундуке
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем сундука должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем сундука должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Занимаемый объем должен быть int или float")
        if occupied_volume <= 0:
            raise ValueError("Занимаемый объем не может быть отрицательным числом")
        self.occupied_volume = occupied_volume
    def is_empty_chest(self) -> bool:
        """
        Функция которая проверяет, является ли сундук пустым
        :return: Является ли сундук пустым

        Примеры:
        >>>chest = Chest(202, 0)
        >>>chest.is_empty_chest()
        """

    def add_item_to_chest(self,item:float) -> None:
        """
        Добавление вещи в сундук
        :param item: Объем добавляемой вещи

        :raise ValueError: Если объём добавляемой вещи превышает свободное место в сундуке, то вызываем ошибку

        Примеры:
        >>> chest = Chest(500, 0)
        >>> chest.add_item_to_chest(200)
        """
    def remove_item_from_chest(self, estimate_item: float) -> None:
        """
        Извлечение вещи из сундука

        :param estimate_item: Объем извлекаемой вещи
        :raise ValueError: Если объем извлекаемой вещи превышает занимаемый объем в сундуке, то возвращается ошибка

        :return: Объем реально извлеченной вещи

        Примеры:
        >>> chest = Chest(500,500)
        >>> chest.remove_item_from_chest(200)
        """

class Box:
    def __int__(self, capacity_volume: float, occupied_volume: float):
        """
        :param capacity_volume: Объем коробки
        :param occupied_volume: Объем занемаемого места в коробке
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем коробки должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем коробки должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Занимаемый объем должен быть int или float")
        if occupied_volume <= 0:
            raise ValueError("Занимаемый объем не может быть отрицательным числом")
        self.occupied_volume = occupied_volume
    def is_empty_box(self) -> bool:
        """
        Функция которая проверяет, является ли коробка пустой
        :return: Является ли коробка пустой

        Примеры:
        >>>box = Box(301, 0)
        >>>box.is_empty_box()
        """

    def add_item_to_box(self, item: float) -> None:
        """
        Добавление вещи в коробку
        :param item: Объем добавляемой вещи

        :raise ValueError: Если объём добавляемой вещи превышает свободное место в коробке, то вызываем ошибку

        Примеры:
        >>> box = Box(800, 0)
        >>> box.add_item_to_box(500)
        """
    def remove_item_from_box(self, estimate_item: float) -> None:
        """
        Извлечение вещи из коробки

        :param estimate_item: Объем извлекаемой вещи
        :raise ValueError: Если объем извлекаемой вещи превышает занимаемый объем в коробке, то возвращается ошибка

        :return: Объем реально извлеченной вещи

        Примеры:
        >>> box = Box(700,700)
        >>> box.remove_item_from_box(500)
        """

class Case:
    def __int__(self, capacity_volume: float, occupied_volume: float):
        """
        :param capacity_volume: Объем кейса
        :param occupied_volume: Объем занемаемого места в кейсе
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем кейса должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем кейса должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Занимаемый объем должен быть int или float")
        if occupied_volume <= 0:
            raise ValueError("Занимаемый объем не может быть отрицательным числом")
        self.occupied_volume = occupied_volume
    def is_empty_case(self) -> bool:
        """
        Функция которая проверяет, является ли кейс пустым
        :return: Является ли кейс пустым

        Примеры:
        >>>case = Case(202, 0)
        >>>case.is_empty_case()
        """

    def add_item_to_case(self,item: float) -> None:
        """
        Добавление вещи в кейс
        :param item: Объем добавляемой вещи

        :raise ValueError: Если объём добавляемой вещи превышает свободное место в кейсе, то вызываем ошибку

        Примеры:
        >>> case = Case(500, 0)
        >>> case.add_item_to_case(200)
        """
    def remove_item_from_case(self, estimate_item: float) -> None:
        """
        Извлечение вещи из кейса

        :param estimate_item: Объем извлекаемой вещи
        :raise ValueError: Если объем извлекаемой вещи превышает занимаемый объем в кейсе, то возвращается ошибка

        :return: Объем реально извлеченной вещи

        Примеры:
        >>> case = Case(500,500)
        >>> case.remove_item_from_case(200)
        """
if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

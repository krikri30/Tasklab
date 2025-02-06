if __name__ == "__main__":
    class Animal:
        """
        Базовый класс для всех животных.
        """

        def __init__(self, name: str, age: int) -> None:
            """
            Инициализация объекта Animal.

            :param name: Имя животного.
            :param age: Возраст животного.
            """
            self._name = name  # Защищенный атрибут
            self._age = age  # Защищенный атрибут

        def speak(self) -> str:
            """
            Метод, который возвращает звук, издаваемый животным.
            Этот метод будет переопределен в дочерних классах.

            :return: Звук животного.
            """
            return "Some sound"

        def __str__(self) -> str:
            """
            Строковое представление объекта Animal.

            :return: Строка с информацией о животном.
            """
            return f"Animal(name={self._name}, age={self._age})"

        def __repr__(self) -> str:
            """
            Официальное строковое представление объекта Animal.

            :return: Официальная строка с информацией о животном.
            """
            return f"Animal('{self._name}', {self._age})"


    class Tiger(Animal):
        """
        Класс для тигров, наследуется от класса Animal.
        """

        def __init__(self, name: str, age: int, breed: str) -> None:
            """
            Инициализация объекта Tiger.

            :param name: Имя тигра.
            :param age: Возраст тигра.
            :param breed: Порода тигра.
            """
            super().__init__(name, age)  # Вызов конструктора базового класса
            self._breed = breed  # Защищенный атрибут для породы тигра

        def speak(self) -> str:
            """
            Переопределение метода speak для тигров.

            :return: Звук, который издает тигр.
            """
            return "ARRR!"

        def __str__(self) -> str:
            """
            Строковое представление объекта Tiger.

            :return: Строка с информацией о тигре.
            """
            return f"Tiger(name={self._name}, age={self._age}, breed={self._breed})"

        def __repr__(self) -> str:
            """
            Официальное строковое представление объекта Tiger.

            :return: Официальная строка с информацией о тигре.
            """
            return f"Tiger('{self._name}', {self._age}, '{self._breed}')"


    class Cat(Animal):
        """
        Класс для кошек, наследуется от класса Animal.
        """

        def __init__(self, name: str, age: int, color: str) -> None:
            """
            Инициализация объекта Cat.

            :param name: Имя кошки.
            :param age: Возраст кошки.
            :param color: Цвет кошки.
            """
            super().__init__(name, age)  # Вызов конструктора базового класса
            self._color = color  # Защищенный атрибут для цвета кошки

        def speak(self) -> str:
            """
            Переопределение метода speak для кошек.

            :return: Звук, который издает кошка.
            """
            return "Meow!"

        def __str__(self) -> str:
            """
            Строковое представление объекта Cat.

            :return: Строка с информацией о кошке.
            """
            return f"Cat(name={self._name}, age={self._age}, color={self._color})"

        def __repr__(self) -> str:
            """
            Официальное строковое представление объекта Cat.

            :return: Официальная строка с информацией о кошке.
            """
            return f"Cat('{self._name}', {self._age}, '{self._color}')"


    # Пример использования классов
    tiger = Tiger("Buddy", 3, "Amur")
    cat = Cat("Whiskers", 2, "Black")

    print(tiger)  # Выводит информацию о тигре
    print(cat)  # Выводит информацию о кошке
    print(tiger.speak())  # Выводит звук тигра
    print(cat.speak())  # Выводит звук кошки

    # Write your solution here
    pass

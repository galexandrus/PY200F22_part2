from abc import abstractmethod
from typing import Union


class Turbine:
    @abstractmethod
    def __init__(self, power: Union[int, float], pressure: Union[int, float]):
        """
        Конструктор турбины
        :param power: мощность турбины, МВт
        :param pressure: давление среды на входе в турбину, МПа
        """
        self.check_power(power)
        self.check_pressure(pressure)
        self._power = power
        self._pressure = pressure

    @abstractmethod
    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        return str(f"Турбина мощностью {self.power} МВт с давлением на входе {self.pressure} МПа")

    @property
    def power(self) -> Union[int, float]:
        return self._power

    @property
    def pressure(self) -> Union[int, float]:
        return self._pressure

    @staticmethod
    def check_power(power: Union[int, float]):
        """
        Проверка значения мощности
        :param power: мощность, МВт
        """
        if not (isinstance(power, int) or isinstance(power, float)):
            raise TypeError("мощность должна быть числом")

    @staticmethod
    def check_pressure(pressure: Union[int, float]):
        """
        Проверка значения давления
        :param pressure: давление, МПа
        """
        if not (isinstance(pressure, int) or isinstance(pressure, float)):
            raise TypeError("давление должно быть числом")


class SteamTurbine(Turbine):
    def __init__(self, power: Union[int, float], pressure: Union[int, float], type_: str, pk: Union[int, float]):
        """
        Конструктор паровой турбины
        :param power: мощность, МВт
        :param pressure: давление, МПа
        :param pk: давление в конденсаторе, кПа (для турбин типа "Р" бар)
        :param type_: тип
        """
        super().__init__(power, pressure)
        self.check_type(type_)
        self._type = type_
        self.check_pk(pk)
        self.pk = pk

    def __repr__(self):
        return f'{self.__class__.__name__}({self._power}, {self._pressure}, "{self._type}", {self._pk})'

    @property
    def type_(self) -> str:
        return self._type

    @property
    def pk(self) -> Union[int, float]:
        return self._pk

    @pk.setter
    def pk(self, new_pk):
        self.check_pk(new_pk)
        self._pk = new_pk

    @staticmethod
    def check_type(type_: str):
        types = ["П", "Т", "ПТ", "Р"]
        if type_ not in types:
            raise ValueError("здесь можно использовать следующие типы паровых турбин: П, Т, ПТ, Р")

    def check_pk(self, pk: Union[int, float]):
        if not (isinstance(pk, int) or isinstance(pk, float)):
            raise TypeError("давление в конденсаторе должно быть числом")
        if self._type != "Р" and pk > 20:
            raise ValueError("слишком высокое давление в конденсаторе")

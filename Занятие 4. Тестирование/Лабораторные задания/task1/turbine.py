from typing import Union
from abc import ABC, abstractmethod


class Turbine:
    @abstractmethod
    def __init__(self, power: Union[int, float], pressure: Union[int, float]):
        """
        Конструктор турбины
        :param power: мощность турбины
        :param pressure: давление среды на входе в турбину
        """
        self.check_power(power)
        self.power = power
        self.check_pressure(pressure)
        self.pressure = pressure

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.power}, {self.pressure})"

    def __str__(self) -> str:
        return str(f"Турбина мощностью {self.power} с давлением на входе {self.pressure}")

    @staticmethod
    def check_power(power: Union[int, float]):
        """
        Проверка значения мощности
        :param power: мощность
        """
        if not (isinstance(power, int) or isinstance(power, float)):
            raise TypeError("мощность должны быть int или float")

    @staticmethod
    def check_pressure(pressure: Union[int, float]):
        """
        Проверка значения давления
        :param pressure: давление
        """
        if not (isinstance(pressure, int) or isinstance(pressure, float)):
            raise TypeError("давление должно быть float")


class SteamTurbine(Turbine):
    def __init__(self, power: Union[int, float], pressure: Union[int, float], type_: str):
        """
        Конструктор паровой турбины
        :param power: мощность
        :param pressure: давление
        :param type_: тип
        """
        self.check_power(power)
        self.power = power
        self.check_pressure(pressure)
        self.pressure = pressure
        self.check_type(type_)
        self.type = type_

    @staticmethod
    def check_type(type_: str):
        types = ["П", "Т", "ПТ", "Р"]
        if type_ not in types:
            raise ValueError("возможные типы паровых турбин: П, Т, ПТ, Р")

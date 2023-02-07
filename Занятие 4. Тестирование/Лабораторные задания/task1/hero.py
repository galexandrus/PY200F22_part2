from abc import abstractmethod


class Hero:
    hero_count = 0

    @classmethod
    def increment_hero_count(cls):
        cls.hero_count += 1

    def __init__(self, name: str):
        self.check_name(name)
        self._name = name
        self.increment_hero_count()

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name})"

    def __str__(self):
        return f"{self._name} - герой базового класса, он не разговаривает"

    @property
    def name(self):
        return self._name

    @staticmethod
    def check_name(name: str):
        if not isinstance(name, str):
            raise TypeError("имя должно быть типа str")

    @abstractmethod
    def phrase(self):
        pass


class NormalHero(Hero):
    def __init__(self, name: str, phrase: str = "нормальные герои всегда идут в обход"):
        super().__init__(name)
        self.phrase = phrase

    def __str__(self):
        return f"{self._name} - нормальный герой, он всегда идёт в обход"

    @property
    def phrase(self):
        return self._phrase

    @phrase.setter
    def phrase(self, new_phrase):
        if not isinstance(new_phrase, str):
            raise TypeError("фраза должна быть типа str")
        self._phrase = new_phrase


class StraightHero(Hero):
    def __init__(self, name: str, phrase: str = "я хожу прямо"):
        super().__init__(name)
        self.phrase = phrase

    def __str__(self):
        return f"{self._name} всегда ходит прямо"

    @property
    def phrase(self):
        return self._phrase

    @phrase.setter
    def phrase(self, new_phrase):
        if not isinstance(new_phrase, str):
            raise TypeError("фраза должна быть типа str")
        self._phrase = new_phrase

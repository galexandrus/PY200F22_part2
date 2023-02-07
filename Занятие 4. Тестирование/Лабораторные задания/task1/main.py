from turbine import SteamTurbine
from hero import Hero, NormalHero, StraightHero


if __name__ == "__main__":
    T150 = SteamTurbine(150, 127.5, "Т", 18)
    print(T150)
    print(repr(T150))
    T150.pk = 12
    R100 = SteamTurbine(100, 127.5, "Р", 3)
    print(R100)
    print(repr(R100))

    print("")

    print(Hero.hero_count)
    Simpleton = Hero("Simpleton")
    print(Simpleton)
    print(repr(Simpleton))
    print(Hero.hero_count)

    print(NormalHero.hero_count)
    John = NormalHero("John")
    print(John)
    print(repr(John))
    John.phrase = "мы идём по кругу"
    print(John.phrase)
    print(NormalHero.hero_count)
    Ben = NormalHero("Ben", "я тоже нормальный")
    print(Ben.phrase)
    print(NormalHero.hero_count)

    Boris = StraightHero("Boris")
    print(Boris)
    print(repr(Boris))
    Boris.phrase = "пришло время свернуть"
    print(Boris.phrase)
    print(Hero.hero_count)

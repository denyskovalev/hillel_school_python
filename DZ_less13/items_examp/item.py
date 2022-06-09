
class Item:

    def __init__(self, name: str, key: str, rank: 1 or 2 or 3, bonus_value: int or float, price: int or float):

        self.__name = None
        self.name = name
        self.__key = None
        self.key = key
        self.__rank = None
        self.rank = rank
        self.__bonus_value = None
        self.bonus_value = bonus_value
        self.__price = None
        self.price = price
        # setup basic characteristic item

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if type(value) is not str:
            raise TypeError("Name item must be string!")
        elif not 3 <= len(value) <= 25:
            raise ValueError("Too long item name! Must be between 3 and 25!")
        elif self.__name is None:
            self.__name = value
        else:
            raise ValueError(f"You can`t rename item! - {self.name}")
        # Type check, len name check, name immutable

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value: str):
        if value not in ("sword", "shield", "protective  kit"):
            raise ValueError("'Weapon key must be 'sword', 'shield' or 'protective  kit'")
        elif self.key is None:
            self.__key = value
        else:
            raise ValueError(f"You cant rename item key - '{self.key}'")
        # Type check, check if weapon not correct key, key item immutable

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, value: 1 or 2 or 3):
        if value not in (1, 2, 3):
            raise ValueError("Rank may be 1, 2 or 3!")
        elif self.rank is None:
            self.__rank = value
        else:
            raise ValueError(f"You cant change rank item - '{self.name}', rank - '{self.rank}'")
        # item may have only 1,2,3 rank, items rank immutable

    @property
    def bonus_value(self):
        return self.__bonus_value

    @bonus_value.setter
    def bonus_value(self, value: int or float):
        if type(value) is not (int or float):
            raise ValueError("Rank may be 1, 2 or 3!")
        elif value < 0:
            self.__bonus_value = 0
            print("Bonus value of item cant be above 0!")
        elif self.bonus_value is None:
            self.__bonus_value = value
        else:
            raise ValueError(f"You cant change bonus value - '{self.bonus_value}'")
        # type check, bonus may be up characteristics, value immutable

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: int or float):
        if type(value) is not (int or float):
            raise ValueError("Rank may be 1, 2 or 3!")
        elif value <= 0:
            print(f"Price must cost 1 and more money!")
        elif self.__price is None:
            self.__price = value
        else:
            raise ValueError(f"You cant change price!")
        # immutable, type check, price must be 1 and more


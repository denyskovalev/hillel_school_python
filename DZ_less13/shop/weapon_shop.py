
class WeaponShop:

    def __init__(self, name: str):

        self.__name = None
        self.name = name
        self.money = 9999
        self.bag = {
            "swords": [],
            "shields": []
        }

    def __str__(self):
        return f"{self.name}\n{str(self.bag)}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if type(value) is not str:
            raise TypeError("Name arena must be string!")
        elif not 3 <= len(value) <= 20:
            raise ValueError("Too long arena name! Must be between 3 and 20!")
        elif self.__name is None:
            self.__name = value
        else:
            raise ValueError(f"You can`t rename arena! - {self.name}")
        # Type check, len name check, name immutable

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if type(value) is not int or not float:
            raise TypeError("Add money only integer or float numbers!")
        else:
            self.__money = value

        if self.money < 0:
            self.__money = 0
            print(f"{self.name} have no money!")

    def add_item(self, item):
        if item.key == "sword":
            self.bag["swords"].append(item.name)
        elif item.key == "shield":
            self.bag["shields"].append(item.name)
        else:
            print(f"{item.name} - have invalid key: {item.key}")


from DZ_less13.shop import WeaponShop


class Hero:

    def __init__(self, name: str):
        self.__name = None
        self.name = name
        self.health = 100
        self.rank = 3
        self.power = 6
        self.sword_bonus = 0
        self.money = 200
        self.defence = 0
        self.shield_bonus = 0
        self.__bag = []
        self.__weapon_slots = {
            "sword": None,
            "shield": None
        }
        print(f"***Start with basic characteristics:***\nName: {self.name}\nHealth: {self.health}\n"
              f"Rank: {self.rank}\nPower: {self.power}\nMoney: {self.money}\nDefence: {self.defence}\n"
              f"Bag: {self.bag}")

        # create some basic characteristic, name immutable,
        # characteristics are basic, but there is a function to specify custom characteristics
        # "custom_characteristics"

    def custom_characteristics(self, name, health, rank, power, money, defence):
        self.__name = name
        self.__health = health
        self.__rank = rank
        self.__power = power
        self.__money = money
        self.__defence = defence
        print(f"***Characteristics changed:***\nName: {self.name}\nHealth: {self.health}\n"
              f"Rank: {self.rank}\nPower: {self.power}\nMoney: {self.money}\nDefence: {self.defence}")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if type(value) is not str:
            raise TypeError("Name must be string!")
        elif not 3 <= len(value) <= 12:
            raise ValueError("Too long name! Must be between 3 and 12!")
        elif self.__name is None:
            self.__name = value
        else:
            raise ValueError("You cant rename player!")
        # name len check, name immutable, type name check

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value: int or float):
        if type(value) is not (int or float):
            print(type(value))
            raise TypeError("Cant add words to health player!")
        else:
            self.__health = value

        if self.health < 0:
            self.health = 1
            print(f"{self.name} at the death door, please heal!")
        if self.health > 100:
            self.health = 100
            print(f"{self.name} have maximum heal point!")
        # health may be between 0-100, int or float

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, value: 1 or 2 or 3):
        if value in (1, 2, 3):
            self.__rank = value
        else:
            raise ValueError("Rank may be 1, 2 or 3!")
        # rank may be in available range

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value: int or float):
        max_power = self.__health // 10
        if type(value) is not (int or float):
            raise TypeError("Power may be integer or float!")
        elif value > max_power:
            self.__power = max_power
            return
        elif value <= 0:
            self.__power = 1
            return
        else:
            self.__power = value
        # max power check, type check, power may be in available range

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value: int or float):
        if type(value) is not (int or float):
            raise TypeError("Add money only integer or float numbers!")
        else:
            self.__money = value

        if self.money < 0:
            self.__money = 0
            print("The value of money cannot be negative in the wallet!")
            return
        # type check, cannot have negative range

    @property
    def defence(self):
        return self.__defence

    @defence.setter
    def defence(self, value: int or float):
        if type(value) is not (int or float):
            raise TypeError("Defence must be integer or float!")
        elif value < 0:
            self.__defence = 0
            print("Defence cannot be in negative values!")
            return
        elif value > 10:
            self.__defence = 10
            print("Defence cannot be over 10")
            return
        else:
            self.__defence = value
        # type check, defence may be in available range "0-100"

    @property
    def bag(self):
        return self.__bag

    @bag.setter
    def bag(self, item):
        if item.name not in self.bag:
            self.__bag.append(item.name)
        else:
            print(f"'{item.name}' - is already in bag!")
        # Bottomless bag, cannot contain duplicates

    def dress_item(self, item):
        if item.name not in self.bag:
            print("Cant dress item out of range!")
            return
        elif item.rank > self.rank:
            print(f"{item.name} have to high rank!")
            return
        # rank check, check if item out of bag

        if item.key == "sword":
            self.__weapon_slots["sword"] = item.name
            self.sword_bonus = item.bonus_value
            print(f"{item.name} successful eqip on {self.name}")
        elif item.key == "shield":
            self.__weapon_slots["shield"] = item.name
            self.shield_bonus = item.bonus_value
            print(f"{item.name} successful eqip on {self.name}")
        else:
            print(f"{item.name} - have invalid key: {item.key}")
        # check shield or sword, rank check, key check

    def damage_target(self, target):
        if target is self:  # self target check
            print("Can`t hit myself, change target!")
            return
        elif self.rank != target.rank:  # check available rank
            print(f"{self.name} and {target.name} do not have the same rank!")
            return
        elif target.health < 5:  # target hp check
            print(f"{target.name} - HP is too low, hes can`t fight!")
            return
        elif self.health < 5:  # Self hp check
            print(f"{self.name}: Im have too low HP, now i`m cant fight!")
            return

        targ_def_bonus = (target.shield_bonus + target.defence) // 10
        if (self.power + self.sword_bonus) - targ_def_bonus > self.health // 10:
            damage = self.health // 10
        else:
            damage = (self.power + self.sword_bonus) - targ_def_bonus
        target.health -= damage
        # correct damage

        # winner check
        if target.health < 5:
            self.money += target.money
            target.money = 0
            print(f"'{self.name}' fight with '{target.name}'\nWinner: '{self.name}'")

    def buy_item(self, shop: WeaponShop, item):
        if self.money >= item.price:
            self.bag = item
            self.money -= item.price
            shop.money += item.price
            print(f"Successful trade {item.name} from {shop.name} to {self.name}")
        else:
            print(f"No money for buy item")


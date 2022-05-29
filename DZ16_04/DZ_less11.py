# Реалізувати клас Герой що має мати наступні атрибути: ім‘я, здоров‘я, ранг, сила і метод вдарити.
# Метод вдарити повинен наносити шкоду противнику в розмірі сили героя. Герой має мати наступні
# обмеження: здоров‘я від 0 до 100, ранг 1,2,3. Сила не більше 10% теперішнього здоров‘я героя.
# Не можна бити героїв здоров‘я яких менше 5.
#
# Реалізувати клас маг, який може відновлювати здоров'я інших героїв, також він має ранг як герой і
# може наносити удари. За відновлення здоров'я він бере гроші. ( Вам потрібно реалізувати цей функціонал ).
# Герой заробляє гроші за перемогу у бою з іншим героєм, також при перемозі він забирає всі гроші суперника.
# Скільки герой отримує грошей за перемогу і скільки коштує відновити здоров'я, на ваш розсуд)

class Hero:

    def __init__(self, name, health, rang, power):
        self.__name = name

        if health <= 0:
            self.__health = 1
        elif health >= 101:
            self.__health = 100
        else:
            self.__health = health

        if rang < 1:
            self.__rang = 1
        elif rang > 3:
            self.__rang = 3
        else:
            self.__rang = rang

        if power < 0:
            self.__power = 1
        elif power > self.__health // 10:
            self.__power = self.health // 10
        else:
            self.__power = power

        self.__money = 20
        print(f"***Start with:***\nName: '{self.__name}' Health: {self.health}\n"
              f"Rang: {self.__rang}           Power: {self.__power}"
              f"     And {self.__money} money!\n")

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_health(self):
        return self.__health

    def set_health(self, value):
        if value <= 0:
            self.__health = 1
            print(f"{self.__name} - at death's door! Please heal!")
        elif value >= 101:
            self.__health = 100
            print(f"{self.__name} - have a maximum health!")
        else:
            self.__health = value
        if self.health > 100:
            self.health = 100
            print(f"{self.__name} - have a maximum health!")

    def get_rang(self):
        return self.__rang

    def set_rang(self, value):
        if value < 1:
            self.__rang = 1
            print(f"Hero {self.__name} - play with min rang!")
        elif value > 3:
            self.__rang = 3
            print(f"Hero {self.__name} - play with max rang!")
        else:
            self.__rang = value

    def get_power(self):
        return self.__power

    def set_power(self, value):
        if value < 0:
            self.__power = 1
            print(f"Hero {self.__name} - have low power, be careful!")
        elif value > (self.__health // 10):
            self.__power = (self.__health // 10)
            print(f"Hero {self.__name} - have max power!")
        else:
            self.__power = value

    def get_money(self):
        return self.__money

    def set_money(self, value):
        if value < 0:
            self.__money = 0
            print(f"Hero {self.__name} - have no money! Go fight!")
        else:
            self.__money = value

    name = property(get_name, set_name)
    health = property(get_health, set_health)
    rang = property(get_rang, set_rang)
    power = property(get_power, set_power)
    money = property(get_money, set_money)

    def damage(self, target):

        if target.health < 5:
            print("You can`t attack unit with low HP!")
            return

        if self.__power < self.health // 10:
            target.health -= self.__power
            print(f"{self.__name} attacked {target.name}, dealing {self.__power} damage to him")
        else:
            target.health -= self.__health // 10
            print(f"{self.__name} attacked {target.name}, dealing {(self.__health // 10)} damage to him")

        if target.health < 5:
            winner_reward = 10
            self.__money += winner_reward + target.money
            print(f"{self.__name} vs {target.name}: -> win: {self.__name}\n"
                  f"And take {winner_reward} monet. Plus {target.money} from the "
                  f"{target.name} poket")
            target.money = 0


class Mage(Hero):

    def heal_target(self, target):
        if target.money < 10:
            print(f"{target.name} have {target.money} money, need min 10 for heal!")
        else:
            target.money -= 10
            self.money += 10
            target.health += 10
            print(f"{self.name} heal {target.name} 10 HP")

#  # test
# apolo = Hero("Apolon", 40, 40, 7)
#
# aphro = Mage("Aphrodite", 222, 9, 8)
#
# print(apolo.health)
# aphro.damage(apolo)
# print(apolo.health)
# aphro.damage(apolo)
# print(apolo.health)
# aphro.damage(apolo)
# aphro.damage(apolo)
# aphro.damage(apolo)
# aphro.heal_target(apolo)
# aphro.heal_target(apolo)
# aphro.heal_target(apolo)

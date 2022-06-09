
from DZ_less13.players_examp.hero import Hero


class Mage(Hero):

    def heal_hp(self, target: Hero):
        if target is self:
            print(f"{self.name} can heal only another player!")
            return
        elif target.health >= 100:
            print(f"{target.name} have maximum HP!")
            return
        elif target.health < 100 and target.money >= (100 - target.health):
            heal_value = (100 - target.health)
            target.health += heal_value
            target.power = target.health * 0.1
            target.money -= heal_value
            self.money += heal_value
        # can`t heal myself, max hp target check, target money check

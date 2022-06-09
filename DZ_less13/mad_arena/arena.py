from DZ_less13.players_examp import Hero, Mage


class Arena:

    def __init__(self, name: str, winner_reward: int or float):

        self.__name = None
        self.name = name
        self.__winner_reward = 0
        self.winner_reward = winner_reward

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if type(value) is not str:
            raise TypeError("Name item must be string!")
        elif not 3 <= len(value) <= 20:
            raise ValueError("Too long item name! Must be between 3 and 20!")
        elif self.__name is None:
            self.__name = value
        else:
            raise ValueError(f"You can`t rename arena! - {self.name}")
        # Type check, len check, name immutable

    @property
    def winner_reward(self):
        return self.__winner_reward

    @winner_reward.setter
    def winner_reward(self, value: int or float):
        if type(value) is not (int or float):
            raise TypeError("Winner reward may be number!")
        elif value < 100:
            print("Winner reward may be 100 and more!")
        else:
            self.__winner_reward = value

    def tournament_automatic(self, player1: Hero or Mage, player2: Hero or Mage):
        winner = None
        turn_count = 2

        while winner is None:
            if turn_count % 2 == 0:
                turn_count += 1
                player1.damage_target(player2)
                print(player2.health, player2.name)
                if player2.health < 5:
                    winner = player1.name
                    player1.money += self.winner_reward
                    print(f"{player1.name} win! And hes grab {self.winner_reward} money!")
            else:
                turn_count += 1
                player2.damage_target(player1)
                print(player1.health, player1.name)
                if player1.health < 5:
                    winner = player2.name
                    player2.money += self.winner_reward
                    print(f"{player2.name} win! And hes grab {self.winner_reward} money!")
            # my tournament is automatic just for example
            # I know, I don`t add healing to arena, to hard at now !)

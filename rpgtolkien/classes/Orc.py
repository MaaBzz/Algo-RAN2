from classes.Character import Character


class Orc(Character):

    def __init__(self, pseudo: str) -> None:
        super().__init__(pseudo)
        self.strengh = 7
        self.mana = 0
        self.defense = 8
        self.speed = 3
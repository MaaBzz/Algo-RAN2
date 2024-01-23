from classes.Character import Character


class Elf(Character):

    def __init__(self, pseudo: str) -> None:
        super().__init__(pseudo)
        self.strengh = 5
        self.mana = 100
        self.defense = 5
        self.speed = 7
class Character:

    def __init__(self, pseudo:str) -> None:
        self.pseudo = pseudo
        self.health = 100
        self.mana = None
        self.strengh = None
        self.stamina = 100
        self.defense = None
        self.speed = None
        self.levele = 1

    def attack(self, character) -> None:
        print(f"--- {self.pseudo} attaque {self.pseudo} ---")
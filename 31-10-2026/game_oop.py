class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health-=amount
        # self.health = self.health - amount

    def stats(self):
        print(f"{self.name} has {self.health} HP/Points left.")


player_1 = Character("Jadhav", 100)
player_1.take_damage(20)
player_1.stats()


player_2 = Character("Kiran", 100)
player_2.take_damage(70)
player_2.stats()
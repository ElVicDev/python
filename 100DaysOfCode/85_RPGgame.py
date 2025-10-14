""" Día 85: Juego de rol basado en texto.
Desarrolla un juego de rol simple basado en texto. """

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0
    def display_status(self):
        print(f"{self.name} - Health: {self.health}, Attack Power: {self.attack_power}")
def main():
    hero = Character("Hero", 100, 20)
    monster = Character("Monster", 80, 15)

    print("A wild monster appears!")
    hero.display_status()
    monster.display_status()

    while hero.is_alive() and monster.is_alive():
        hero.attack(monster)
        if monster.is_alive():
            monster.attack(hero)
        hero.display_status()
        monster.display_status()
        print("-" * 20)

    if hero.is_alive():
        print("The hero has defeated the monster!")
    else:
        print("The monster has defeated the hero!")
if __name__ == "__main__":
    main()

""" Resultados esperados:
A wild monster appears!
Hero - Health: 100, Attack Power: 20
Monster - Health: 80, Attack Power: 15
Hero attacks Monster for 20 damage!
Monster attacks Hero for 15 damage!
Hero - Health: 85, Attack Power: 20
Monster - Health: 60, Attack Power: 15
------------------------
Hero attacks Monster for 20 damage!
Monster attacks Hero for 15 damage!
Hero - Health: 70, Attack Power: 20
Monster - Health: 40, Attack Power: 15
------------------------
Hero attacks Monster for 20 damage!
Monster attacks Hero for 15 damage!
Hero - Health: 55, Attack Power: 20
Monster - Health: 20, Attack Power: 15
------------------------
Hero attacks Monster for 20 damage!
Hero - Health: 55, Attack Power: 20
The hero has defeated the monster!
"""
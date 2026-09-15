from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Big Cheese"
def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} won the battle!")
    else:
        print(f"{enemy} won the battle!")


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gorble")
    goblinTwo = Goblin("Scribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")
    print("But no hero has answered the call... yet.")

    jo = Hero("Jo")
    print(f"{jo.name} enteres the arena with {jo.health} health.")
    battle(jo, goblin)
    joAttackNumber = jo.attack()
    
    goblin.take_damage(joAttackNumber)

if __name__ == "__main__":
    main()
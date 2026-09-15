from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Big Cheese"


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
    joAttackNumber = jo.attack()
    
    goblin.take_damage(joAttackNumber)

if __name__ == "__main__":
    main()
    

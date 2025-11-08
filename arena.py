from blacksmith import showCurrentArmor

class Enemy:
    def __init__(self, name, health, damage, extraDamage, extraChance, attackSpeed, defense, loot):
        self.name = name
        self.health = health
        self.damage = damage
        self.extraDamage = extraDamage
        self.extraChance = extraChance
        self.attackSpeed = attackSpeed
        self.defense = defense
        self.loot = loot

# LEVEL 1-5: Začátečníci
rat = Enemy("Rat", 15, 3, 2, 3, 0.8, 0, 5)
spider = Enemy("Spider", 20, 5, 3, 5, 1.0, 1, 8)
snake = Enemy("Snake", 25, 6, 4, 7, 1.1, 1, 12)
wolf = Enemy("Wolf", 30, 8, 5, 9, 1.3, 2, 15)
bandit = Enemy("Bandit", 35, 10, 6, 11, 1.2, 3, 20)

# LEVEL 6-10: Lehcí
goblin = Enemy("Goblin", 40, 12, 7, 12, 1.4, 4, 25)
skeleton = Enemy("Skeleton", 45, 14, 8, 13, 1.3, 5, 30)
zombie = Enemy("Zombie", 50, 15, 9, 14, 1.0, 6, 35)
wild_boar = Enemy("Wild Boar", 55, 16, 10, 13, 1.5, 5, 40)
dark_cultist = Enemy("Dark Cultist", 60, 18, 11, 15, 1.4, 6, 50)

# LEVEL 11-15: Střední
orc = Enemy("Orc", 70, 20, 12, 16, 1.6, 8, 60)
ghoul = Enemy("Ghoul", 75, 22, 13, 17, 1.5, 7, 70)
harpy = Enemy("Harpy", 80, 24, 14, 18, 1.8, 6, 80)
troll = Enemy("Troll", 90, 26, 15, 17, 1.4, 10, 95)
wraith = Enemy("Wraith", 85, 28, 16, 19, 1.7, 8, 100)

# LEVEL 16-20: Pokročilí
werewolf = Enemy("Werewolf", 100, 30, 18, 20, 1.9, 10, 120)
minotaur = Enemy("Minotaur", 110, 32, 20, 19, 1.6, 12, 140)
vampire = Enemy("Vampire", 105, 35, 22, 21, 1.8, 11, 160)
ogre = Enemy("Ogre", 130, 38, 24, 18, 1.5, 15, 180)
dark_knight = Enemy("Dark Knight", 120, 40, 25, 20, 1.7, 14, 200)

# LEVEL 21-25: Těžcí
demon = Enemy("Demon", 150, 45, 28, 22, 1.9, 16, 250)
chimera = Enemy("Chimera", 160, 48, 30, 23, 1.8, 17, 280)
frost_giant = Enemy("Frost Giant", 180, 50, 32, 21, 1.6, 20, 320)
lich = Enemy("Lich", 140, 55, 35, 24, 1.7, 15, 350)
hydra = Enemy("Hydra", 200, 52, 34, 22, 1.8, 18, 400)

# LEVEL 26-30: BOSSES
dragon = Enemy("Dragon", 250, 60, 40, 25, 2.0, 22, 500)
ancient_demon = Enemy("Ancient Demon", 280, 65, 45, 25, 2.1, 24, 600)
death_knight = Enemy("Death Knight", 300, 70, 48, 24, 1.9, 28, 700)
archdemon = Enemy("Archdemon", 320, 75, 50, 25, 2.2, 26, 850)
dark_lord = Enemy("Dark Lord", 400, 80, 60, 25, 2.0, 30, 1000)


# Seznam všech nepřátel pro snadný přístup
enemies_list = [
    # Level 1-5
    rat, spider, snake, wolf, bandit,
    # Level 6-10
    goblin, skeleton, zombie, wild_boar, dark_cultist,
    # Level 11-15
    orc, ghoul, harpy, troll, wraith,
    # Level 16-20
    werewolf, minotaur, vampire, ogre, dark_knight,
    # Level 21-25
    demon, chimera, frost_giant, lich, hydra,
    # Level 26-30
    dragon, ancient_demon, death_knight, archdemon, dark_lord
]


def showAllEnemies():
    print("\n" + "=" * 85)
    print("ALL ENEMIES".center(85))
    print("=" * 85)
    print(f"{'#':<4} {'Name':<20} {'HP':<8} {'DMG':<8} {'Crit%':<8} {'Speed':<8} {'DEF':<8} {'Loot':<8}")
    print("-" * 85)
    print(f"{"0":<4} {"to exit":<20}")

    for i, enemy in enumerate(enemies_list, 1):
        print(f"{i:<4} {enemy.name:<20} {enemy.health:<8} {enemy.damage:<8} {enemy.extraChance:<8} "
              f"{enemy.attackSpeed:<8} {enemy.defense:<8} {enemy.loot:<8}")
    print("=" * 85)

    number =  int(input("Enter yours enemy number: "))
    if number == 0 :
        return None
    if 1 <= number <= len(enemies_list):
        return enemies_list[number - 1]
    showAllEnemies()
    return None


def loadArena(player):
    print("\n\n"
          "⚔️  WELCOME TO THE ARENA ⚔️\n")
    print("=" * 50)
    print(f" HP: {player['HP']}")
    print(f" Money: {player['money']} golds")
    showCurrentArmor(player['armor'], player['weapon'])

    print("\n" + "=" * 50)
    print("Choose your action:\n"
          "1. choose enemy\n"
          "2. exit the arena\n")
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        input("Press Enter to continue...")
        return loadArena(player)
    match(choice):
        case 1:
            yourEnemy = showAllEnemies()
            player = fightEnemy(yourEnemy, player)
            return loadArena(player)
        case 2:
            return player
        case _:
            print("Invalid input! Please enter a number.")
            return loadArena(player)

def calculateDefense(player):
    totalDefense = 0
    for armor in player['armor']:
        totalDefense += armor['defense']
    return player


def fightEnemy(enemy, player):
    print("\n" + "=" * 50)
    print("⚔️  Fight starts! ⚔️")
    print("=" * 50)
    print(f"Your stats: (HP: {player["HP"]}, DMG: {player["weapon"]["stats"]["dmg"]}, DEF: {player['totalDefense']})")
    print("VS")
    print(f"Enemy (HP: {enemy.health}, DMG: {enemy.damage}, DEF: {enemy.defense})")

    try :
        input("\nStiskni ENTER pro start...")
    except KeyboardInterrupt:
        print("\n" + "-" * 85)
    return player


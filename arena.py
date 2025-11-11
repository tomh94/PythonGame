import random

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
rat = Enemy("Rat", 15, 3, 2, 5, 2.5, 0, 5)  # Rychlý, slabý útok
spider = Enemy("Spider", 18, 4, 6, 15, 1.8, 2, 8)  # Rychlý s jedem (vyšší crit)
snake = Enemy("Snake", 22, 5, 8, 20, 1.6, 1, 12)  # Střední rychlost, jedovaté údery
wolf = Enemy("Wolf", 28, 7, 5, 12, 2.2, 3, 15)  # Rychlý predátor
bandit = Enemy("Bandit", 35, 9, 7, 10, 1.4, 5, 20)  # Vyvážený s lehkou zbrojí

# LEVEL 6-10: Lehcí
goblin = Enemy("Goblin", 38, 10, 6, 18, 2.0, 4, 25)  # Rychlý, zákeřný
skeleton = Enemy("Skeleton", 42, 11, 9, 8, 1.2, 8, 30)  # Pomalý, odolný
zombie = Enemy("Zombie", 55, 13, 5, 5, 0.8, 10, 35)  # Velmi pomalý tank
wild_boar = Enemy("Wild Boar", 50, 15, 10, 15, 1.9, 6, 40)  # Agresivní útočník
dark_cultist = Enemy("Dark Cultist", 45, 16, 12, 20, 1.3, 7, 50)  # Magické útoky

# LEVEL 11-15: Střední
orc = Enemy("Orc", 75, 18, 12, 14, 1.5, 12, 60)  # Silný válečník
ghoul = Enemy("Ghoul", 65, 20, 15, 22, 1.7, 9, 70)  # Rychlý s vysokým critem
harpy = Enemy("Harpy", 60, 17, 10, 25, 2.3, 5, 80)  # Velmi rychlá, křehká
troll = Enemy("Troll", 100, 22, 8, 10, 1.1, 18, 95)  # Pomalý tank s regenerací
wraith = Enemy("Wraith", 70, 24, 18, 28, 1.6, 8, 100)  # Rychlý assassin

# LEVEL 16-20: Pokročilí
werewolf = Enemy("Werewolf", 95, 26, 16, 24, 2.1, 11, 120)  # Agresivní bestie
minotaur = Enemy("Minotaur", 120, 30, 20, 18, 1.4, 16, 140)  # Silný, pomalý berserk
vampire = Enemy("Vampire", 90, 28, 22, 30, 1.9, 10, 160)  # Rychlý s life stealem
ogre = Enemy("Ogre", 140, 32, 15, 12, 1.2, 22, 180)  # Masivní tank
dark_knight = Enemy("Dark Knight", 110, 35, 25, 20, 1.6, 20, 200)  # Těžká zbroj

# LEVEL 21-25: Těžcí
demon = Enemy("Demon", 130, 38, 28, 26, 1.8, 15, 250)  # Rychlý démontický útočník
chimera = Enemy("Chimera", 150, 40, 30, 22, 1.7, 18, 280)  # Vícehlavá bestie
frost_giant = Enemy("Frost Giant", 180, 42, 25, 16, 1.3, 28, 320)  # Obrovský tank
lich = Enemy("Lich", 110, 48, 35, 32, 1.5, 12, 350)  # Nekromant - vysoký damage
hydra = Enemy("Hydra", 200, 36, 28, 20, 2.0, 25, 400)  # Mnoho útoků, odolná

# LEVEL 26-30: BOSSES
dragon = Enemy("Dragon", 250, 50, 40, 28, 1.8, 30, 500)  # Legendární drak
ancient_demon = Enemy("Ancient Demon", 220, 58, 45, 30, 2.0, 25, 600)  # Rychlý démon lord
death_knight = Enemy("Death Knight", 280, 55, 38, 22, 1.4, 35, 700)  # Nemrtvý válečník
archdemon = Enemy("Archdemon", 260, 62, 48, 32, 1.9, 28, 850)  # Nejvyšší démon
dark_lord = Enemy("Dark Lord", 350, 65, 55, 26, 1.5, 40, 1000)

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

    try :
        number =  int(input("Enter yours enemy number: "))
    except ValueError:
        print("neplatná hodnota")
        return None
    if number == 0 :
        return None
    if 1 <= number <= len(enemies_list):
        return enemies_list[number - 1]
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
            if yourEnemy is not None : player = fightEnemy(yourEnemy, player)
            return loadArena(player)
        case 2:
            return player
        case _:
            print("Invalid input! Please enter a number.")
            return loadArena(player)

def calculateDefense(player):
    totalDefense = 0
    for slot, armor in player['armor'].items():
        if armor is not None:
            totalDefense += armor['stats']['defense']
    player["totalDefense"] = totalDefense
    return player


def fightEnemy(enemy, player):
    reward = enemy.loot
    player = calculateDefense(player)


    player_hp = player['HP']
    enemy_hp = enemy.health

    if player["weapon"]["type"] is not None:
        player_dmg = player["weapon"]["stats"]["dmg"]
        player_crit_dmg = player_dmg * 1.3
        player_crit_chance = player["weapon"]["stats"]["crit_chance"]
        player_speed = player["weapon"]["stats"]["attack_speed"]
    else:
        player_dmg = 5
        player_crit_dmg = 7
        player_crit_chance = 5
        player_speed = 1.0

    player_def = player['totalDefense']

    print("\n" + "=" * 60)
    print("⚔️  FIGHT STARTS! ⚔️".center(60))
    print("=" * 60)
    print(f"YOU: HP={player_hp}, DMG={player_dmg}, DEF={player_def}, SPEED={player_speed}")
    print(f"{enemy.name.upper()}: HP={enemy_hp}, DMG={enemy.damage}, DEF={enemy.defense}, SPEED={enemy.attackSpeed}")
    print("=" * 60)
    input("\nPress ENTER to start...\n")

    if player["weapon"]["stats"]["attack_speed"] is not None :
        player_time = 1/player["weapon"]["stats"]["attack_speed"]
    else:
        player_time = 1/player_speed
    enemy_time = 1/enemy.attackSpeed
    round_num = 1

    while player_hp > 0 and enemy_hp > 0:
        print(f"\n--- Round {round_num} ---")

        if player_time <= enemy_time:
            print(f"⚔️  YOUR TURN (time: {player_time:.2f}s)")

            is_crit = random.randint(1, 100) <= player_crit_chance
            base_dmg = player_dmg + (player_crit_dmg if is_crit else 0)

            final_dmg = max(1, base_dmg * (1-(enemy.defense/100)))
            enemy_hp -= final_dmg

            if is_crit:
                print(f"   💥 CRITICAL HIT! Dealt {final_dmg} damage!")
            else:
                print(f"   Hit! Dealt {final_dmg} damage")
            print(f"   {enemy.name} HP: {max(0, enemy_hp)}/{enemy.health}")

            player_time += 1.0 / player_speed

        else:
            print(f"🗡️  {enemy.name.upper()}'S TURN (time: {enemy_time:.2f}s)")

            is_crit = random.randint(1, 100) <= enemy.extraChance
            base_dmg = enemy.damage + (enemy.extraDamage if is_crit else 0)

            final_dmg = max(1, base_dmg * (1-(player_def/100)))
            player_hp -= final_dmg

            if is_crit:
                print(f"   💥 CRITICAL HIT! Took {final_dmg} damage!")
            else:
                print(f"   Hit! Took {final_dmg} damage")
            print(f"   Your HP: {max(0, player_hp)}/{player['HP']}")

            enemy_time += 1.0 / enemy.attackSpeed

        round_num += 1

        if player_hp > 0 and enemy_hp > 0:
            input("Press ENTER for next action...")

    print("\n" + "=" * 60)
    if player_hp > 0:
        print("🎉 VICTORY! 🎉".center(60))
        print(f"You won with {player_hp} HP remaining!")
        print(f"💰 Earned {reward} gold!")
        player['money'] += reward
        player['HP'] = player_hp
    else:
        print("💀 DEFEAT 💀".center(60))
        print(f"{enemy.name} defeated you!")
        player['HP'] = 20
        print("You respawned with 20 HP")
    print("=" * 60)

    input("\nPress ENTER to continue...")
    return player


import random
from random import choice

armorList = {
    "helmets": {
        "bronze": {"defense": 2, "price": 30},
        "iron": {"defense": 3, "price": 50},
        "golden": {"defense": 4, "price": 120},
        "diamond": {"defense": 6, "price": 200}
    },
    "chestplates": {
        "bronze": {"defense": 4, "price": 50},
        "iron": {"defense": 6, "price": 80},
        "golden": {"defense": 8, "price": 180},
        "diamond": {"defense": 10, "price": 300}
    },
    "legins": {
        "bronze": {"defense": 3, "price": 40},
        "iron": {"defense": 5, "price": 70},
        "golden": {"defense": 6, "price": 150},
        "diamond": {"defense": 8, "price": 250}
    },
    "boots": {
        "bronze": {"defense": 2, "price": 25},
        "iron": {"defense": 3, "price": 45},
        "golden": {"defense": 4, "price": 100},
        "diamond": {"defense": 5, "price": 180}
    }
}
weaponsList = {
    "sword": {
        "bronze": {"dmg": 8, "crit_chance": 5, "attack_speed": 1.6, "price": 40},
        "iron": {"dmg": 10, "crit_chance": 8, "attack_speed": 1.6, "price": 70},
        "golden": {"dmg": 12, "crit_chance": 12, "attack_speed": 1.8, "price": 150},
        "diamond": {"dmg": 15, "crit_chance": 15, "attack_speed": 1.6, "price": 250}
    },
    "waraxe": {
        "bronze": {"dmg": 10, "crit_chance": 3, "attack_speed": 0.9, "price": 50},
        "iron": {"dmg": 13, "crit_chance": 5, "attack_speed": 0.9, "price": 85},
        "golden": {"dmg": 15, "crit_chance": 10, "attack_speed": 1.0, "price": 180},
        "diamond": {"dmg": 18, "crit_chance": 12, "attack_speed": 1.0, "price": 300}
    }
}
weapon_list = []
blacksmith_sayings = [
    "Another dead hero's equipment for sale. Business is good.",
    "Your sword is dull. Just like your survival instincts.",
    "I'll sharpen your blade. Can't sharpen your brain though.",
    "Come back when you can afford the good stuff. Or don't.",
    "That dent? That's where the goblin won.",
    "My apprentice swings better than you. He's eight.",
    "Quality costs coin. You seem short on both.",
    "I've seen scarecrows with better armor maintenance.",
    "Your gear survives more fights than you will.",
    "I fix armor. I can't fix poor life choices."
]
todaysQuote = random.choice(blacksmith_sayings)

def showArmor(armor):
    for key, name, in armor.items():
        print(f"{key}: {name}")

def showWeapons(weapons):
    for key, name, in weapons.items():
        print(f"{key}: {name}")

def showWeaponsList(weaponsList):
    print("\n=== BLACKSMITH'S WEAPONS ===\n")
    print(f"{'No.':<5} {'Weapon':<25} {'DMG':>5} {'Crit':>8} {'Speed':>8} {'Price':>10}")
    print("-" * 70)

    counter = 1
    for weapon_type, materials in weaponsList.items():
        for material, stats in materials.items():
            weapon_list.append({
                "type": weapon_type,
                "material": material,
                "stats": stats
            })
            weapon_name = f"{material.capitalize()} {weapon_type}"
            crit = f"{stats['crit_chance']}%"
            price = f"{stats['price']} golds"
            print(f"{counter:<5} {weapon_name:<25} {stats['dmg']:>5} {crit:>8} {stats['attack_speed']:>8} {price:>15}")
            counter += 1
    chosenWeapon = int(input(f"\n your chose: "))
    print(weapon_list[chosenWeapon])

def loadBlacksmith(money, armor, weapons):
    print("\n\n\n\n"
          " you are in blacksmith\n"
          " ********* you have", money, " golds\n"
          " ********* your armor :", showArmor(armor))

    print("chose options: \n"
          "1. Weapons\n"
          "2. Armor\n"
          "3. Talk with blacksmith\n"
          "4. Back to lobby\n")

    choice = int(input("\n"))
    match choice:
        case 1:
            showWeaponsList(weaponsList)
            return loadBlacksmith(money, armor, weapons)
        case 2:
            return loadBlacksmith(money, armor, weapons)
        case 3:
            print("\nBlack smith: 'Welcome little guy! Need me?'")
            print("today's quote: ", todaysQuote)
            input("\nPress Enter to continue...")
            return loadBlacksmith(money, armor, weapons)
        case 4:
            return money, armor, weapons
        case _:
            print("Invalid option!")
            input("Press Enter to continue...")
            return loadBlacksmith(money, armor, weapons)

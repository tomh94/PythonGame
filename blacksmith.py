import random

armorList = {
    "helmet": {
        "bronze": {"defense": 3, "price": 30},
        "iron": {"defense": 5, "price": 50},
        "steel": {"defense": 7, "price": 90},
        "golden": {"defense": 9, "price": 120},
        "diamond": {"defense": 12, "price": 200},
        "legendary": {"defense": 15, "price": 350}
    },
    "chestplate": {
        "bronze": {"defense": 5, "price": 50},
        "iron": {"defense": 8, "price": 80},
        "steel": {"defense": 11, "price": 130},
        "golden": {"defense": 14, "price": 180},
        "diamond": {"defense": 18, "price": 300},
        "legendary": {"defense": 22, "price": 500}
    },
    "legins": {
        "bronze": {"defense": 4, "price": 40},
        "iron": {"defense": 7, "price": 70},
        "steel": {"defense": 9, "price": 110},
        "golden": {"defense": 11, "price": 150},
        "diamond": {"defense": 14, "price": 250},
        "legendary": {"defense": 18, "price": 400}
    },
    "boots": {
        "bronze": {"defense": 3, "price": 25},
        "iron": {"defense": 5, "price": 45},
        "steel": {"defense": 7, "price": 75},
        "golden": {"defense": 9, "price": 100},
        "diamond": {"defense": 11, "price": 180},
        "legendary": {"defense": 14, "price": 300}
    }
}

weaponsList = {
    "sword": {
        "bronze": {"dmg": 12, "crit_chance": 10, "attack_speed": 1.7, "price": 40},
        "iron": {"dmg": 20, "crit_chance": 15, "attack_speed": 1.8, "price": 70},
        "steel": {"dmg": 30, "crit_chance": 18, "attack_speed": 1.9, "price": 120},
        "golden": {"dmg": 42, "crit_chance": 22, "attack_speed": 2.0, "price": 150},
        "diamond": {"dmg": 55, "crit_chance": 26, "attack_speed": 2.2, "price": 250},
        "legendary": {"dmg": 75, "crit_chance": 30, "attack_speed": 2.5, "price": 450}
    },
    "waraxe": {
        "bronze": {"dmg": 16, "crit_chance": 7, "attack_speed": 1.2, "price": 50},
        "iron": {"dmg": 26, "crit_chance": 12, "attack_speed": 1.3, "price": 85},
        "steel": {"dmg": 38, "crit_chance": 15, "attack_speed": 1.4, "price": 140},
        "golden": {"dmg": 52, "crit_chance": 18, "attack_speed": 1.5, "price": 180},
        "diamond": {"dmg": 68, "crit_chance": 22, "attack_speed": 1.7, "price": 300},
        "legendary": {"dmg": 90, "crit_chance": 26, "attack_speed": 1.9, "price": 500}
    },
    "spear": {
        "bronze": {"dmg": 14, "crit_chance": 12, "attack_speed": 1.5, "price": 45},
        "iron": {"dmg": 23, "crit_chance": 17, "attack_speed": 1.6, "price": 75},
        "steel": {"dmg": 34, "crit_chance": 20, "attack_speed": 1.7, "price": 130},
        "golden": {"dmg": 47, "crit_chance": 24, "attack_speed": 1.9, "price": 170},
        "diamond": {"dmg": 62, "crit_chance": 28, "attack_speed": 2.1, "price": 280},
        "legendary": {"dmg": 82, "crit_chance": 32, "attack_speed": 2.3, "price": 480}
    },
    "dagger": {
        "bronze": {"dmg": 8, "crit_chance": 18, "attack_speed": 2.2, "price": 35},
        "iron": {"dmg": 14, "crit_chance": 24, "attack_speed": 2.4, "price": 65},
        "steel": {"dmg": 22, "crit_chance": 28, "attack_speed": 2.6, "price": 115},
        "golden": {"dmg": 32, "crit_chance": 32, "attack_speed": 2.8, "price": 145},
        "diamond": {"dmg": 44, "crit_chance": 36, "attack_speed": 3.0, "price": 240},
        "legendary": {"dmg": 60, "crit_chance": 40, "attack_speed": 3.3, "price": 420}
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

def showWeaponsList(weaponsList, money, weapon, armor):
    print("\n=== BLACKSMITH'S WEAPONS ===\n")
    print(" ********* you have", money, " golds\n")
    print(f"{'No.':<5} {'Weapon':<25} {'DMG':>5} {'Crit':>8} {'Speed':>8} {'Price':>10}")
    print("-" * 70)
    print(f"{"0":<5} {"To exit":<25}")

    counter = 1
    weapon_list = []
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

    chosenWeapon = int(input(f"\n Which one you take?: "))

    if chosenWeapon == 0:
        return money, armor, weapon

    chosenWeapon -= 1

    if money >= weapon_list[chosenWeapon]["stats"]["price"]:
        money -= weapon_list[chosenWeapon]["stats"]["price"]
        weapon = weapon_list[chosenWeapon]
        print("Your weapon is: ", weapon["material"], "", weapon["type"])
        input("Press Enter to continue...")
        return money, armor, weapon
    else:
        print("You don't have enough golds.")
        input("Press Enter to continue...")
        return showWeaponsList(weaponsList, money, weapon, armor)


def showCurrentArmor(armor, weapon):
    print("\n=== YOUR CURRENT ARMOR ===\n")
    print(f"{'Slot':<15} {'Item':<25} {'Defense':>10}")
    print("-" * 50)

    total_defense = 0
    for slot, item in armor.items():
        if item is not None:
            item_name = f"{item['material'].capitalize()} {item['type']}"
            defense = item['stats']['defense']
            total_defense += defense
            print(f"{slot.capitalize():<15} {item_name:<25} {defense:>10}")
        else:
            print(f"{slot.capitalize():<15} {'Empty':<25} {0:>10}")

    print("-" * 50)
    print(f"{'TOTAL DEFENSE:':<40} {total_defense:>10}")
    print("\n" + "=" * 50)
    print(f"{'Weapon':<15}")

    if weapon["type"] is not None:
        weapon_name = f"{weapon['material'].capitalize()} {weapon['type']}"
        print(f" {weapon_name:<35}")
        print(f"  • Damage: {weapon['stats']['dmg']}")
        print(f"  • Crit chance: {weapon['stats']['crit_chance']}%")
        print(f"  • Attack speed: {weapon['stats']['attack_speed']}")
    else:
        print(f"  • No weapon equipped")
    print("-" * 50)
    print()

def showArmorList(armorList, money, weapon, armor):
    print("\n=== BLACKSMITH'S ARMOR ===\n")
    print(" ********* you have", money, " golds\n")
    print(f"{'No.':<5} {'Armor':<25} {'Defense':>10} {'Price':>10}")
    print("-" * 70)
    print(f"{"0":<5} {"To exit":<25}")

    counter = 1
    armor_list = []

    for armor_type, materials in armorList.items():
        print("\n")
        for material, stats in materials.items():
            armor_list.append({
                "type": armor_type,
                "material": material,
                "stats": stats
            })
            armor_name = f"{material.capitalize()} {armor_type}"
            defense = stats['defense']
            price = f"{stats['price']} golds"
            print(f"{counter:<5} {armor_name:<25} {defense:>10} {price:>15}")
            counter += 1

    chosenArmor = int(input(f"\n Which one you take?: "))

    if chosenArmor == 0:
        return money, armor, weapon

    chosenArmor -= 1

    if money >= armor_list[chosenArmor]["stats"]["price"]:
        money -= armor_list[chosenArmor]["stats"]["price"]
        armorSlot = armor_list[chosenArmor]["type"]
        armor[armorSlot] = armor_list[chosenArmor]
        showCurrentArmor(armor, weapon)
        input("Press Enter to continue...")
        return money, armor, weapon
    else:
        print("You don't have enough golds.")
        input("Press Enter to continue...")
        return showArmorList(armorList, money, weapon, armor)


def loadBlacksmith(money, armor, weapon):
    print("\n\n\n\n"
          " you are in blacksmith\n"
          " ********* you have", money, " golds\n")
    showCurrentArmor(armor, weapon)


    if weapon["type"] is not None:
        print(" ********* your weapon is", weapon["material"], weapon["type"])
    else:
        print(" You don't have any weapon, go buy one!")

    print("chose options: \n"
          "1. Weapons\n"
          "2. Armor\n"
          "3. Talk with blacksmith\n"
          "4. Back to lobby\n")

    choice = int(input("\n"))
    match choice:
        case 1:
            money, armor, weapon = showWeaponsList(weaponsList, money, weapon, armor)
            return loadBlacksmith(money, armor, weapon)
        case 2:
            money, armor, weapon = showArmorList(armorList, money, weapon, armor)
            return loadBlacksmith(money, armor, weapon)
        case 3:
            print("\nBlack smith: 'Welcome little guy! Need me?'")
            print("today's quote: ", todaysQuote)
            input("\nPress Enter to continue...")
            return loadBlacksmith(money, armor, weapon)
        case 4:
            print("armor")
            return money, armor, weapon
        case _:
            print("Invalid option!")
            input("Press Enter to continue...")
            return loadBlacksmith(money, armor, weapon)
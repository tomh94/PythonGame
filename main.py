

HP = 100
money = 100
armor = {
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

weapons = {
    "swords": {
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


def loadLobby():
    global HP, money
    print("\n\n\n\n"
          " you are in lobby\n"
          " ********* your HP is: ", HP, "/100\n"
                                         " ********* your Money is: ", money, "\n")
    print("chose options: \n"
          "1. Pub\n"
          "2. Arena\n"
          "3. Blacksmith\n"
          "4. Exit")

    choice = int(input("\n"))
    if choice != 4:
        match choice:
            case 1:
                return loadPub()
            #case 2:
                return loadArena()
            #case 3:
                return loadBlacksmith()
            case _:
                return "Neplatná hodnota", loadLobby()
    else:
        exit()


def loadPub():
    global HP, money
    print("\n\n\n\n"
          " You are in Pub\n"
          " ********* Your HP is: ", HP, "/100\n"
          " ********* Your Money is: ", money, "\n")
    print("What do you want to do?\n"
          "1. Drink beer (restore 20 HP) - 10 gold\n"
          "2. Drink wine (restore 50 HP) - 25 gold\n"
          "3. Talk to bartender\n"
          "4. Back to Lobby")

    choice = int(input("\n"))
    match choice:
        case 1:
            if money >= 10:
                money -= 10
                HP += 20
                if HP > 100: HP = 100
                print("You drank a beer! +20 HP")
                input("Press Enter to continue...")
                return loadPub()
            else:
                print("Not enough money!")
                input("Press Enter to continue...")
                return loadPub()
        case 2:
            if money >= 25:
                money -= 25
                HP += 50
                if HP > 100: HP = 100
                print("You drank wine! +50 HP")
                input("Press Enter to continue...")
                return loadPub()
            else:
                print("Not enough money!")
                input("Press Enter to continue...")
                return loadPub()
        case 3:
            print("\nBartender: 'Welcome traveler! Need some rest?'")
            input("Press Enter to continue...")
            return loadPub()
        case 4:
            return loadLobby()
        case _:
            print("Invalid option!")
            input("Press Enter to continue...")
            return loadPub()

def main():
    print("Welcome in my python game")
    loadLobby()


main()

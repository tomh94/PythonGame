import random

from arena import loadArena
from pub import loadPub
from blacksmith import loadBlacksmith

armor = {
    "helmet": {
        "type": "helmet",
        "material": "legendary",
        "stats": {"defense": 15}
    },
    "chestplate": {
        "type": "chestplate",
        "material": "legendary",
        "stats": {"defense": 22}
    },
    "legins": {
        "type": "legins",
        "material": "legendary",
        "stats": {"defense": 18}
    },
    "boots": {
        "type": "boots",
        "material": "legendary",
        "stats": {"defense": 14}
    }
}

weapon = {
    "type": "waraxe",
    "material": "legendary",
    "stats": {
        "dmg": 90,
        "crit_chance": 26,
        "attack_speed": 1.9
    }
}

player = {
    "HP" : 100,
    "money" : 100,
    "armor" : armor,
    "weapon" : weapon,
    "totalDefense" : None,
}

def loadLobby():
    global armor, weapon, player
    print("\n\n\n\n"
          " ====== you are in lobby ======\n\n"
          " ====== your HP is: ", player["HP"], "/100 ======\n"
          " ====== your Money is: ", player["money"], " ======\n")
    print("chose options: \n"
          "1. Pub\n"
          "2. Arena\n"
          "3. Blacksmith\n"
          "4. Exit")
    choice = 0
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        input("Press Enter to continue...")
    if choice != 4:
        match choice:
            case 1:
                player["HP"], player["money"] = loadPub(player["HP"], player["money"])
                return loadLobby()
            case 2:
                player = loadArena(player)
                return loadLobby()
            case 3:
                player["money"], player["armor"], player["weapon"] = loadBlacksmith(player["money"], player["armor"], weapon)
                return loadLobby()
            case _:
                print("Neplatná hodnota")
                return loadLobby()
    else:
        exit()


def main():
    print("Welcome in my python game")
    loadLobby()


main()
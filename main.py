from arena import loadArena
from pub import loadPub
from blacksmith import loadBlacksmith

armor = {
    "helmet": None,
    "chestplate": None,
    "legins": None,
    "boots": None,
}

weapon = {
    "type": None,
    "material": None,
    "stats": {
        "dmg": None,
        "crit_chance": None,
        "attack_speed": None
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
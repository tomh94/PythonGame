import random
from pub import loadPub
from blacksmith import loadBlacksmith

HP = 50
money = 100
armor = {
    "helmet": None,
    "chestplate": None,
    "legins": None,
    "boots": None,
}
weapon = {
    "type": None,
    "material": None,
    "stats" : {"dmg": None, "crit_chance": None, "attack_speed": None,}
}


def loadLobby():
    global HP, money, armor, weapon
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
                HP, money = loadPub(HP, money)
                return loadLobby()
            #case 2:
            #    return loadArena()
            case 3:
                money, armor, weapon = loadBlacksmith(money, armor, weapon)
                print(money, armor, weapon)
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
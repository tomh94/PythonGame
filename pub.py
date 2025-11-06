import random


def loadPub(HP, money):
    tavern_sayings = [
        "Three heroes walked in yesterday. I'm selling their boots tomorrow.",
        "Your funeral is cheaper than your bar tab.",
        "That wound will heal. Unlike your reputation.",
        "I know you'll pay eventually. Dead men's friends always do.",
        "My cheapest ale costs more than your life insurance.",
        "You smell like failure. And goblin guts.",
        "Every scar tells a story. Yours say 'I barely survived'.",
        "The graveyard's full. But I'm sure they'll make room for you.",
        "Your party looks brave. So did the last one.",
        "I've cleaned bloodstains older than your adventure career."
    ]
    todaysQuote = tavern_sayings[random.randint(0, len(tavern_sayings) - 1)]

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
            if HP == 100:
                print("Your HP is full, you can't drink a beer")
                input("Press enter to continue...")
                return loadPub(HP, money)
            if money >= 10:
                money -= 10
                HP += 20
                if HP > 100: HP = 100
                print("You drank a beer! +20 HP")
                input("Press Enter to continue...")
                return loadPub(HP, money)
            else:
                print("Not enough money!")
                input("Press Enter to continue...")
                return loadPub(HP, money)
        case 2:
            if HP == 100:
                print("Your HP is full, you can't drink wine")
                input("Press enter to continue...")
                return loadPub(HP, money)

            if money >= 25:
                money -= 25
                HP += 50
                if HP > 100: HP = 100
                print("You drank wine! +50 HP")
                input("Press Enter to continue...")
                return loadPub(HP, money)
            else:
                print("Not enough money!")
                input("Press Enter to continue...")
                return loadPub(HP, money)
        case 3:
            print("\nBartender: 'Welcome traveler! Need some rest?'")
            print("today's quote: ", todaysQuote)
            input("\nPress Enter to continue...")
            return loadPub(HP, money)
        case 4:
            return HP, money
        case _:
            print("Invalid option!")
            input("Press Enter to continue...")
            return loadPub(HP, money)
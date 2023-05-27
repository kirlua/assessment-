# Monster card game that I can add monsters name or remove the monster name
# Check the monster from the list or make changes to the existing monster
import easygui

# dictionary for original monsters
# defines a dictionary called monster and in the dictionary there is stats
# each monster is represented as a key in dictionary
# inside the key there is also inner dictionary stats like strength, speed,
# stealth and cunning
monsters = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2},
}


# it is a function for adding monster into the original list
def add_monster():
    name = easygui.enterbox("Enter the name of the new monster: ")
    if name is None:
        easygui.msgbox("Please enter a name for the new monster.")
        return
    name = name.capitalize()

    # If user typed value below 1 and over 25 program prints value is to
    # big or to large
    strength = easygui.integerbox("Enter the strength value between 1 and 25: ", lowerbound=1, upperbound=25)
    # If user types wrong values don't go back to main routine ask them again
    # about the inner value for monster
    # If they press cancel program prints out please type the stat number and
    # goes back to main routine
    if strength is None:
        easygui.msgbox("Please type the stat number.")
        return

    # If user typed value below 1 and over 25 program prints value is to big
    # or to large
    speed = easygui.integerbox("Enter the speed value between 1 and 25: ", lowerbound=1, upperbound=25)
    # If user types wrong values don't go back to main routine ask them again
    # about the inner value for monster
    # If they press cancel program prints out please type the stat number and
    # goes back to main routine
    if speed is None:
        easygui.msgbox("Please type the stat number.")
        return

    # If user typed value below 1 and over 25 program prints value is to big or
    # to large
    stealth = easygui.integerbox("Enter the stealth value between 1 and 25: ", lowerbound=1, upperbound=25)
    # If user types wrong values don't go back to main routine ask them again
    # about the inner value for monster
    # If they press cancel program prints out please type the stat number and
    # goes back to main routine
    if stealth is None:
        easygui.msgbox("Please type the stat number.")
        return

    # If user typed value below 1 and over 25 program prints value is to big or
    # to large
    cunning = easygui.integerbox("Enter the cunning value between 1 and 25: ", lowerbound=1, upperbound=25)
    # If user types wrong values don't go back to main routine ask them again
    # about the inner value for monster
    # If they press cancel program prints out please type the stat number and
    # goes back to main routine
    if cunning is None:
        easygui.msgbox("Please type the stat number.")
        return

    monsters[name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}


# It is a function for displaying monsters as a list
def display_monsters():
    # It displays monsters and their stats in msg box using library
    msg = "List of Monster cards: \n"
    # It loops through monsters dictionary using items() method
    # By doing this the name and the stats comes out in one line
    for item, stat in monsters.items():
        msg += f"\n {item}: \n"
        # For new monsters function adds the stat name and it's value
        for monster_ability in stat:
            msg += f'   {monster_ability}: {stat[monster_ability]}'

    easygui.msgbox(msg, title="Monster cards")


# It is a function for removing monster / allowing user to remove monster from
# dictionary
def remove_monster():
    # It calls display monster to call the original lists of monster
    display_monsters()
    # Using enterbox user types the monster they want to remove
    monsters_to_remove = easygui.enterbox("Enter the monster name to remove: ")
    if monsters_to_remove is None:
        easygui.msgbox("Please enter a name of the monster to remove.")
        return
    # Making sure it doesn't make error because of lower case and capital case
    # letters
    monsters_to_remove = monsters_to_remove.capitalize()
    # If user enters name function checks the name if it is in the list and if
    # it is in the list it removes
    if monsters_to_remove in monsters:
        del monsters[monsters_to_remove]
        easygui.msgbox(f"{monsters_to_remove} has been removed from the list")
    # if not the function displays a message box saying the monster wasn't int
    # he list
    else:
        easygui.msgbox(f"{monsters_to_remove} wasn't in the list")


# It is a function called make changes that allows user to update the stats of
# a monster in dictionary
def make_changes():
    # It calls display monster to call the original lists of monster
    display_monsters()
    # Function asks user to enter the name of the monster to make changes using
    # enterbox
    # If user cancels or leave it blank function prints enter the name of the
    # monster to change
    # Then it goes back to main routine
    monster_to_change = easygui.enterbox("Enter the name of the monster\n"
                                         " to change: ")
    if monster_to_change is None:
        easygui.msgbox("Please enter a name of the monster to change.")
        return
    # If user enters the name of the monster function capitalize first letter
    # and check if it exist in dictionary using in
    monster_to_change = monster_to_change.capitalize()
    # If monster exists in dictionary function lets user to enter new value for
    # monster
    if monster_to_change in monsters:
        # The stat numbers should be over1 and below 25
        strength = easygui.integerbox("Enter the new strength value between \n"
                                      "1 and 25: ", lowerbound=1, upperbound=25)
        if strength is None:
            easygui.msgbox("Please type the stat number.")
            return

        speed = easygui.integerbox("Enter the new speed value between 1 and 25: ", lowerbound=1, upperbound=25)
        if speed is None:
            easygui.msgbox("Please type the stat number.")
            return

        stealth = easygui.integerbox("Enter the new stealth value between 1 and 25: ", lowerbound=1, upperbound=25)
        if stealth is None:
            easygui.msgbox("Please type the stat number.")
            return

        cunning = easygui.integerbox("Enter the new cunning value between 1 and 25: ", lowerbound=1, upperbound=25)
        if cunning is None:
            easygui.msgbox("Please type the stat number.")
            return
        # If name doesn't exist in dictionary function displays msg that the monster isn't in the list and go back main routine
        monsters[monster_to_change] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}
        easygui.msgbox(f"{monster_to_change} has been updated.")
    else:
        easygui.msgbox(f"{monster_to_change} is not in the list.")


# It is a function called search monsters from existing list that user types
# Allows user to typed the monster that they want to see
def search_monsters():
    # Using enterbox function lets user to type the name of the monster that they want to find
    monster_to_search = easygui.enterbox("Enter the name of the monster to search: ")
    # If user doesn't enter a name or cancels the function prints Please enter a name of the monster to search
    # Returns to main routine
    if monster_to_search is None:
        easygui.msgbox("Please enter a name of the monster to search.")
        return
    # If user enters a name in lower case letters Function capitalizes the name
    # It checks with the key in the dictionary if it is existing or not existing
    monster_to_search = monster_to_search.capitalize()
    # If it is existing in the dictionary function gets the stats and name and prints
    # the function prints it with msg string in msg box titled "Monster stats"
    if monster_to_search in monsters:
        monster_stats = monsters[monster_to_search]
        msg = f"{monster_to_search}: \n"
        for monster_ability in monster_stats:
            msg += f'   {monster_ability}: {monster_stats[monster_ability]}\n'
        easygui.msgbox(msg, title="Monster stats")
    # If name doesn't exist function prints msg box saying monster wasn't in the list
    else:
        easygui.msgbox(f"{monster_to_search} wasn't in the list")


# It is a while loop/ it lets user to choose what they wan out of 6 options
# This repeats until the user clicks exit
while True:
    choice = easygui.buttonbox("What would you like to do?",
                               choices=["Display monsters", "Add monster", "Remove monster", "Make changes to monster",
                                        "Search monster", "Exit"])
    # If user choose display monster the code calls the display_monster
    # function
    # User can see the existing list/ adjusted/ removed/ added list of the
    # monsters
    if choice == "Display monsters":
        display_monsters()
    # If user chooses add monster the code calls the add_monster function
    # It allows user to add a new monster dictionary
    elif choice == "Add monster":
        add_monster()
    # If user chooses remove monster the code calls the Remove_monster function
    # It allows user to remove monster from monsters dictionary
    elif choice == "Remove monster":
        remove_monster()
    # If user chooses Make changes to monster the code calls the
    # Make_changes_to_monster function
    # It allows user to make changes with from monster dictionary
    elif choice == "Make changes to monster":
        make_changes()
    # If user chooses Search monster the code calls the Search_monster function
    # It allows user to search existing monster from list from monster
    # dictionary
    elif choice == "Search monster":
        search_monsters()
    # If user chooses Exit the code breaks out of the loop and program ends
    elif choice == "Exit":
        break

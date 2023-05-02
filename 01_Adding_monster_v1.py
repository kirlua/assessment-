import easygui

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


# Define a function to add a new monster to the list
def add_monster():
    # Ask the user for the name of the new monster
    name = easygui.enterbox("Enter the name of the new monster:")

    # Ask the user for the strength, speed, stealth, and cunning values
    strength = int(easygui.enterbox("Enter the strength value (1-25):"))
    speed = int(easygui.enterbox("Enter the speed value (1-25):"))
    stealth = int(easygui.enterbox("Enter the stealth value (1-25):"))
    cunning = int(easygui.enterbox("Enter the cunning value (1-25):"))

    # Add the new monster and attributes to the dictionary
    monsters[name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}

    # Show a message box to confirm that the monster was added successfully
    easygui.msgbox(f"{name} was added to the list with attributes: Strength: {strength}, Speed: {speed}, Stealth: {stealth}, Cunning: {cunning}")

# Define a function to display the list of monsters
def display_monsters():
    msg = "List of Monster cards: \n"
    for item, stat in monsters.items():
        msg += f" {item}: \n"
        for monster_ability in stat:
            msg += f'  {monster_ability }: {stat[monster_ability]}\n'

    # Show the list of monsters in a message box
    easygui.msgbox(msg, title="Monster cards")

# Call the add_monster function to add a new monster to the list
add_monster()

# Call the display_monsters function to display the updated list of monsters
display_monsters()

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


def add_monster():
    name = easygui.enterbox("Enter the name of the new monster: ")

    strength = easygui.integerbox("Enter the strength value between 1 and 25: ", lowerbound=1, upperbound=25)
    speed = easygui.integerbox("Enter the speed value between 1 and 25: ", lowerbound=1, upperbound=25)
    stealth = easygui.integerbox("Enter the stealth value between 1 and 25: ", lowerbound=1, upperbound=25)
    cunning = easygui.integerbox("Enter the cunning value between 1 and 25: ", lowerbound=1, upperbound=25)
    monsters[name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}


def display_monsters():
    msg = "List of Monster cards: \n"
    for item, stat in monsters.items():
        msg += f"\n {item}: \n"
        for monster_ability in stat:
            msg += f'   {monster_ability }: {stat[monster_ability]}'

    easygui.msgbox(msg, title="Monster cards")


def get_monsters_as_string():
    msg = "List of Monster cards: \n"
    for item, stat in monsters.items():
        msg += f" {item}: \n"
        for monster_ability in stat:
            msg += f'  {monster_ability }: {stat[monster_ability]}\n'

    return msg


def remove_monsters_as_string():
    msg = "List of Monster cards: \n"
    for item, stat in monsters.items():
        msg += f" {item}: \n"
        for monster_ability in stat:
            msg += f'  {monster_ability }: {stat[monster_ability]}\n '

    return msg


def remove_monster():
    display_monsters()
    monsters_to_remove = easygui.enterbox("Enter the monster name to remove: ").capitalize()
    if monsters_to_remove in monsters:
        del monsters[monsters_to_remove]
        easygui.msgbox(f"{monsters_to_remove} has been removed from the list")
    else:
        easygui.msgbox(f"{monsters_to_remove} wasn't in the list")


def make_changes():
    display_monsters()
    monster_to_change = easygui.enterbox("Enter the name of the monster to change: ").capitalize()
    if monster_to_change in monsters:
        strength = easygui.integerbox("Enter the new strength value between 1 and 25: ", lowerbound=1, upperbound=25)
        speed = easygui.integerbox("Enter the new speed value between 1 and 25: ", lowerbound=1, upperbound=25)
        stealth = easygui.integerbox("Enter the new stealth value between 1 and 25: ", lowerbound=1, upperbound=25)
        cunning = easygui.integerbox("Enter the new cunning value between 1 and 25: ", lowerbound=1, upperbound=25)
        monsters[monster_to_change] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}
        easygui.msgbox(f"{monster_to_change} has been updated.")
    else:
        easygui.msgbox(f"{monster_to_change} is not in the list.")


while True:
    display_monsters()
    choice = easygui.buttonbox("What would you like to do?", choices=["Make changes to a monster", "Remove another monster", "Add a new monster", "End program"])
    if choice == "Make changes to a monster":
        make_changes()
    elif choice == "Remove another monster":
        remove_monster()
    elif choice == "Add a new monster":
        add_monster()
    else:
        break

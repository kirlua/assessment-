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

display_monsters()
#add_monster()
display_monsters()

monsters_string = get_monsters_as_string()
print(monsters_string)

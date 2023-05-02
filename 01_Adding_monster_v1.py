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
    name = easygui.enterbox("Enter the name of the new monster:")
    strength = int(easygui.enterbox("Enter the strength value (1-25):"))
    speed = int(easygui.enterbox("Enter the speed value (1-25):"))
    stealth = int(easygui.enterbox("Enter the stealth value (1-25):"))
    cunning = int(easygui.enterbox("Enter the cunning value (1-25):"))

    monsters[name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}

    easygui.msgbox(f"{name} was added to the list with attributes: Strength: {strength}, Speed: {speed}, Stealth: {stealth}, Cunning: {cunning}")


def display_monsters():
    msg = "List of Monster cards: \n"
    for item, stat in monsters.items():
        msg += f" {item}: \n"
        for monster_ability in stat:
            msg += f'  {monster_ability }: {stat[monster_ability]}\n'


    easygui.msgbox(msg, title="Monster cards")

add_monster()

display_monsters()

# this only lets us enter the name of the monster and typing in the stats of the monster
# It lets us type over 25 and lower then 1 need to fix

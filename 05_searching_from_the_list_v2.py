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



def search_monsters():
    monster_to_search = easygui.enterbox("Enter the name of the monster to search: ").capitalize()
    if monster_to_search in monsters:
        monster_stats = monsters[monster_to_search]
        msg = f"{monster_to_search}: \n"
        for monster_ability in monster_stats:
            msg += f'   {monster_ability }: {monster_stats[monster_ability]}\n'
        easygui.msgbox(msg, title="Monster stats")
    else:
        easygui.msgbox(f"{monster_to_search} wasn't in the list")


display_monsters()
search_monsters()
display_monsters()



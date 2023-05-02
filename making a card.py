import easygui
def add_monster():
    monster_name = easygui.enterbox("Enter the name of the monster that you want to make").upper()
    newmonster[monster_name] ={"items": {}}

    for i in range(4):
        if i == 0:
            monster_name = ()
        if i == 1:
            strength = 0<X<25
        elif i == 2:
            speed = 0<X<25
        elif i == 3:
            stealth = 0<X<25
        else:
            cunning = 0<X<25

        while True:
            monster_name = easygui.enterbox(f"Enter the card name: {monster_name}").capitalize()
            if monsters:
                break

















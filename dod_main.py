from Depths.dod_stat_and_item_selection import learning_to_select
import ast
from dod_savestate import create_savestate, return_too_save_state
from dod_combat_and_entity_class import Entity, Player, combat
from dod_stat_and_item_selection import read_lines, choose_stats

def calc_mod(score):
    if score < 9:
        return -1
    elif score % 2 == 0:
        return (score - 10)  // 2
    elif score % 2 != 0:
        return ((score - 1) - 10) // 2
    else:
        raise ValueError("Score cannot be computed")


def save_game(all_stat_values, map_values):
    response = input('Would you like to save your game?\n(1) Yes!\n(2) Nope\n\n ->')
    if response == "1":
        print(create_savestate(all_stat_values, map_values))
    else:
        input("\n\nPress ENTER to continue")


def main():

    save_data_tuple = []
    new_game = True

    while True:
        print("\n\n"
              "\n-----------------------------------------------------------------------------"
              "\n----------------| ! ! THE DEPTHS OF THE DUNGEON ! ! |------------------------"
              "\n-----------------------------------------------------------------------------")

        prev_save = input('\n\n\t\t\t\t\t   > > ENTER A NUMBER < < \n\n\n\t\t\t\t\t'
                          '    (1) Start New Game\n\t\t\t\t\t    (2) Enter Save File\n\n\t\t-> ')
        if prev_save == "2":
            print("\nWARNING --- Attempts to cheat WILL crash your computer and the code !"
                  "\n\nTo cancel, simply close the program - unless you think im bluffing of course"
                  "\nin which case.... go right ahead and find out why don't you ;)")

            save_code = input("Enter Save Code here:")
            if len(save_code) > 15:
                exact_save_code = ast.literal_eval(save_code)

                if return_too_save_state(exact_save_code):
                    new_game = False
                    print(exact_save_code)
                    save_data_tuple = exact_save_code[0][0]
                else:
                    while True:
                        print("\nLIAR\tLIAR\tLIAR\tLIAR\tLIAR\tLIAR\tLIAR\tLIAR\tLIAR\tLIAR")
            else:
                while True:
                    print("\nLIAR\tLIAR\tLIAR\tLIAR\tLIAR\tLIAR\tLIAR\tLIAR\tLIAR\tLIAR")
        elif prev_save == "1":
            break
        else:
            print('Input a valid number (either 1 or 2) and press enter\n\n\n\n\n\n')

    if new_game:
        read_lines("start_game_exp") # Overview of what D&D is, and a thank you for playing my game!!

        read_lines("learn_input")

        learning_to_select() # Ensures the user knows to input numbers rather than sentences

        all_stat_values = choose_stats() # Program stats for name, ab scores, weapons, items, spells, all found in the
                                        # "dod_stat_and_item_selection.py" file

        while all_stat_values is False:
            all_stat_values = choose_stats()

        print(all_stat_values)
        ab_score_stat_lst, weapons_stat_lst, items_stat_lst, spell_book_lst = all_stat_values #Create the Character!

    else:
        all_stat_values = save_data_tuple

    ab_score_stat_lst, weapons_stat_lst, items_stat_lst, spell_book_lst = all_stat_values

    ab_score_vals = ab_score_stat_lst #Ability scores unpacked
    weapon_vals = weapons_stat_lst #Weapons Unpacked
    item_vals = items_stat_lst  #Items Unpacked
    spell_book_vals = spell_book_lst #Spells Unpacked


    read_lines("intro") #Begining of the real game. Prefaces why you are where you are and what your mission is

    hero = Player(
        name=ab_score_vals[6],
        health=75 + calc_mod(ab_score_vals[2]) * 15,
        dmg_mod=10,
        armour_class=12,
        strength=ab_score_vals[0],
        constitution=ab_score_vals[1],
        dexterity=ab_score_vals[2],
        intelligence=ab_score_vals[3],
        wisdom=ab_score_vals[4],
        charisma=ab_score_vals[5],
        weapons=[
            [weapon_vals[0], "Punch", "1d4", "Strength"],
            [weapon_vals[1], "Sword of Adventure", "2d8", "Strength"],
            [weapon_vals[2], "Bow", "3d6", "Dexterity"],
            [weapon_vals[3], "Morning Star", "3d6", "Dexterity"],
            [weapon_vals[4], "Spear", "3d6", "Dexterity"],
            [weapon_vals[5], "PlaceHolderWeapon", "1d6", "Dexterity"]
        ],

        # Amount, name, dmg, ability mod

        # As long as the key word is in the title (ie sword,
        # bow, health, ect) the code desc will run

        items=[
            [item_vals[0], "Bomb", "2d12", "Dexterity"],
            [item_vals[1], "Arrow", "1d4", "Dexterity"],
            [item_vals[2], "Health Potion", "1d20", "Constitution"],
            [item_vals[3], "SPACE_HOLDER", "0d2", "Constitution"],
            [item_vals[4], "SPACE_HOLDER", "0d2", "Constitution"],
            [item_vals[5], "SPACE_HOLDER", "0d2", "Constitution"],
            [item_vals[6], "SPACE_HOLDER", "0d2", "Constitution"],
            #Bombs, arrows, Health Potions

        ],

        spell_book=[
            [spell_book_vals[0], "Firebolt", "1d6", "Charisma"],
            [spell_book_vals[1], "Heal", "1d20", "Wisdom"],
            [spell_book_vals[2], "SPACE_HOLDER", "0d20", "Charisma"],
            [spell_book_vals[3], "SPACE_HOLDER", "0d20", "Charisma"],
            [spell_book_vals[4], "SPACE_HOLDER", "0d20", "Charisma"],
            [spell_book_vals[5], "SPACE_HOLDER", "0d20", "Charisma"],

        ],
        dodge=1
        # Amount, name, numeric, ability mod
    )

    map_values = [0,0],[0,0],[0,0]

    #------------------------ Entity Health / Combat Data----------------------------------------------------------


    # Create an enemy (the dragon)
    dragon = Entity(
        name="Red Dragon",
        health=100,
        damage=35,
        dmg_mod=7,
        attack_dialogues=[
            ["The dragon breathes fire!", 7, 12, 8],
            ["The dragon swipes its claws!", 4, 6, 8],
            ["The dragon roars, shaking the ground!", 6, 6, 6],
            ["The dragon swipes with its tail!", 3, 8, 8]
        ],
        armour_class=15,
        dodge=1
    )


    save_game(all_stat_values, map_values)

    combat(dragon, hero)





if __name__ == "__main__":
    main()
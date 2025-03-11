from dod_random_dice import roll, advantage, disadvantage

def read_lines(input_file):
    ''' Takes in any file and reads it formatted line by line,
    gives the user a break at the double '??' prompting the user
    to input any key to continue. Possible dev exit available here?
    '''
    input_file = "textfiles/" + input_file
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()  # Strip newline characters
            if line == "??":
                skip = input("\n\n - - Press the Enter key to continue - - ")
                if skip == "skip":
                    return None
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            else:
                print(f"{line}")

def is_num(n):
    if n.isnumeric():
        return True
    else:
        return False


def learning_to_select():
    choice = False

    while not choice:
        learning_input = input("\n-> ")
        choice = True

        if learning_input == "1":
            input("\n\nWell done! Press ENTER to continue with the adventure!")
            choice = True

        elif learning_input == "2":
            input(
                "\n\nWell....I don't either it's black magic. So if you find out, send me an email please\n\nPress ENTER to continue")

        elif learning_input.lower() in ["one", "two", "three"]:
            input("Ha.\n\nHa\n\nHa.\n\nI NEVER saw that one coming\n\nBut in all reality, if you don't enter a "
                  "number, the game could explode. So comit tom-foolery at your own risk.\n\nPress ENTER to continue")

        else:
            print("Unrecognized Input: Please Try again")
            choice = False

    return None

def choose_stats():

    # str = 8
    # dex = 8
    # con = 8
    # intel = 8
    # wis = 8
    # chari = 8
    print("\n\n\n\n\n\n\tWELCOME to Character Creation!!")
    player_name = ""
    while player_name == "":
        player_name = input("\n\n\n To start, lets enter a name! What is your name adventurer?\n\n -> ")
        if player_name == "":
            print("Yea, your not just some nameless entity...yet."
                  "\nPlease input your name! You can even make it fancy with symbols and everything! but"
                  "\ndon't make it too long! You could be in trouble!")
        elif player_name.lower() in ["too long","your name","fancy","fancy with symbols","adventurer","cameron"]:
            input("You dirty little rapscallion. Fine. Two can play that game!\n\n->")
            player_name = " 'In Trouble' "
        elif len(player_name) > 16:
            input("Alright, easy on the sprinkles there, that's WAY too many characters")
        elif player_name == "Avarice":
            input("Well well well, if it isn't the return of the king himself. Best of luck out there Avarice, it's"
                  "\n a big world for such a small little bird ;)")
        elif player_name.lower() in ["in trouble", "amazing", "amazing <3"]:
            input("\nHonestly, I'm not even mad. That was pretty clever of you, I didn't think anyone would"
                  "\never reach this line tbh XD. ")
            input("\nSo ya know what? I'll tell ya a secret. The final boss"
                  "\n is something really cool, but he's also lore acurate for D&D, so he's gonna be tough...")
            input("\n\nbut...\nthere IS a secret item fired from a bow that can do T R E M E N D O U S damage to him!"
                  "\n\n Good luck! <3")
        else:
            response = input(f"Sweet! You have selected {player_name}. Does that work?\n(1) Yep!\n(2) Can I change it?\n\n->")
            if response == "1":
                print(f"Cool beans! Nice to meet ya {player_name}!")
            else:
                player_name = ""
                input("\n\nFiinneeee, only bc your amazing <3")
                input("\nGotta love the mixed messages huh ;)")

    ab_score_stat_lst = [8, 8, 8, 8, 8, 8, player_name]
    weapons_stat_lst = [0,0,0,0,0,0]
    items_stat_lst = [0,0,0,0,0]
    spell_book = [0,0,0,0,0,0]

    pre_built_ab_score_stat_lst = [
        [17,8,17,11,11,11, player_name],
        [8,17,11,17,11,11, player_name],
        [8,17,11,11,11,17,player_name]
    ]
    #

    pre_built_weapons_stat_lst = [
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0]
    ]
    # Punch, Sword, Bow, Morning Star, Spear, PlaceHolderWeapon

    pre_built_items_stat_lst = [
        [0, 0, 0, 0, 0, 0, 0],
        [5, 10, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    # Bombs, arrows, Health Potions

    pre_built_spell_book_stat_lst = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 3, 0, 0, 0, 0, 0]
    ]
    # Heal, Firebolt

    pre_built_key = [["Barbarian","classDesc/barbarianDesc"],
                     ["Rogue", "classDesc/rogueDesc"],
                     ["Bard","classDesc/bardDesc"]]

    ab_score_stat_lst_key = ["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]

    point_total = 27 #This means all stats start at 8 pts


    print(f"\nHowdy {player_name}! Would you like me to explain D&D stats and how they translate here? \n\n(1) Yes\n(2) No")

    while True:
        explain_stats = input("\n -> ")

        # For Dev Mode, input 3

        if explain_stats == "1":
            read_lines("pointBuyExplanation")
            break

        elif explain_stats == "2":
            input("Ay watch out everyone! Seasoned adventurer here!"
                  "\nPress Enter to continue")
            break

        elif explain_stats == "3":
            print("Dev Mode - Max Stats")
            ab_score_stat_lst = [20,20,20,20,20,20, player_name]
            weapons_stat_lst = [1,1,1,1,1,1]
            items_stat_lst = [100,100,1,1,1,1,1]
            spell_book = [1,1,1,1,1,1]

            return ab_score_stat_lst, weapons_stat_lst, items_stat_lst, spell_book
        else:
            print("Invalid input; Please type either 1 or 2")


    while True:
        preset_stats = input("\nWould you like to customize your own stats or use pre-set one's for convenience?\n"
                             "\n< NOTE - YOU CAN SAVE YOUR CUSTOM STATS VIA A CUSTOM LINK YOU GET AFTER THIS PROCESS"
                             "\nSO IF YOU PUT IN THE TIME TO CUSTOMIZE YOU WILL ONLY HAVE TO DO IT ONCE!"
                             "\n(1) Customize my own!\n(2) Preset sounds fun!\n\n-> ")
        if preset_stats == '1':
            break
        elif preset_stats == '2':
            preset_type = input("Selected Preset\n\nEach Preset focuses on two main categories:"
                                "\n\n(1) Barbarian Build (Strength, Constitution)   < Start with Sword, Spear >"
                                "\n(2) Rogue Build (Dexterity, Intelligence)   < Start with Bombs, Bow > "
                                "\n(3) Bard Build (Dexterity, Charisma)   < Start with Firebolt, Heal spells >"
                                "\n\nWhich build would you like?\n ->")
            if preset_type not in ['1','2','3']:
                input("\nPlease input a number between 1 - 3")
            else:
                opt = int(preset_type) - 1
                response = input(f"\nPerfect! You have selected the '{pre_built_key[opt][0]}' build!"
                      f"\nWould you like to learn a little about this class?"
                      f"\n(1) Certainly!\n(2) Nah, I'm good\n\n -> ")
                if response == "1":
                    input("\nWait, really?!?! WOw, everyone usually skips this part..."
                          f"\nAlas, thank you! Here's what I can tell ya about the {pre_built_key[opt][0]} class!"
                          f"\n\nPress ENTER to continue")

                    read_lines(pre_built_key[opt][1])
                else:
                    input("\nYea yea yea, reading isn't your thing huh. I bet you speed run games too :("
                          "\nWell, what are you reading this for!? Move along! Theres ObViOuSlY no adventure"
                          "\ntalking to ME now is there? And don't worry, I C E R T A I N L Y dont hold grudges"
                          "\nPress ENTER to continue")

                    input(f"\n\nConsole Msg: {player_name}s health has been permanently reduced by 70%"
                          "\n\nPress ENTER to continue")
                    input("\n\nJust Kidding!!")
                    input("\n\n....hopefully >:)\n\n")

                ab_score_stat_lst = pre_built_ab_score_stat_lst[int(preset_type)-1]
                weapons_stat_lst = pre_built_weapons_stat_lst[int(preset_type)-1]
                items_stat_lst = pre_built_items_stat_lst[int(preset_type) - 1]
                spell_book = pre_built_spell_book_stat_lst[int(preset_type) - 1]

                return ab_score_stat_lst, weapons_stat_lst, items_stat_lst, spell_book

        else:
            input("Please select one of the options!")


    while point_total > 0:
        print("-----------------------------------------------------------------------------------------------------")
        print("\n\n\n\nHere is the skill point chart:\n"
        "\n8 - 9 -> -1"                 
        "\n10 - 11 -> +0           Reminder: the 2 numbers on the left are"
        "\n12 - 13 -> +1            called the 'Ability Scores', and represent"
        "\n14 - 15 -> +2            the modifier on the right. They all start"
        "\n16 - 17 -> +3            at 8 (or -1) so make sure to invest wisely!"
        "\n18 - 19 -> +4"
        "\n20 -> +5")
        option = (input(f"\nWhich stat would you like to increase? Please type the option number\n< You currently have {point_total} points left >\n"
                        f"\n(1) Strength        ({ab_score_stat_lst[0]} -> {(ab_score_stat_lst[0] - 10) // 2})    (2) Dexterity       ({ab_score_stat_lst[1]} -> {(ab_score_stat_lst[1] - 10) // 2})"
                        f"\n(3) Constitution    ({ab_score_stat_lst[2]} -> {(ab_score_stat_lst[2] - 10) // 2})    (4) Intelligence    ({ab_score_stat_lst[3]} -> {(ab_score_stat_lst[3] - 10) // 2})"
                        f"\n(5) Wisdom          ({ab_score_stat_lst[4]} -> {(ab_score_stat_lst[4] - 10) // 2})    (6) Charisma        ({ab_score_stat_lst[5]} -> {(ab_score_stat_lst[5] - 10) // 2})"
                        f"\n\n -- IMPORTANT -- If you would like to reset your stats/name/items/ect., type 'reset' rather than one of these options\n\n->"))
        if is_num(option):
            if 1 <= int(option) <= 6:
                option = int(option)
                print(f"\nYou have selected {ab_score_stat_lst_key[(option-1)]}!"
                      f"\nThe current modifier for this stat is plus {(ab_score_stat_lst[(option-1)] - 10) // 2} ({ab_score_stat_lst[(option-1)]} points)"
                      f"\nYou currently have {point_total} points left")
                increase = input("\nHow many points would you like to allot to this skill? ->")
                if not is_num(increase):
                    input(f"\n'{increase}' was not recognized. Please input a number")
                else:
                    increase = int(increase)
                    confirm = input(f"\nYou have chosen to allot {increase} points to this skill (for a total of {increase + ab_score_stat_lst[(option-1)]} points)\nAre you sure?\n(1) Yes\n(2) No\n-> ")

                    if confirm == "1": # Confirm selection
                        if increase <= point_total and ((ab_score_stat_lst[(option - 1)] + increase) <= 20): # Checks to make sure that the desired point amount is available
                            ab_score_stat_lst[(option - 1)] += increase
                            point_total -= increase
                            input(f"\nThe new modifier for this stat is +{(ab_score_stat_lst[(option - 1)] - 10) // 2} ({ab_score_stat_lst[(option-1)]} points)"
                                  f"\nYou now have {point_total} points left")
                            print("\n\n\n")
                        elif increase > point_total:
                            input(f"\nYou don't have enough points for that!\nYou wanted to allot {increase} points but only have {point_total} left!")
                        elif (ab_score_stat_lst[(option - 1)] + increase) > 20:
                            input(f"\nWatch out!\nYou wanted to allot {increase} points (for a total of {ab_score_stat_lst[(option - 1)] + increase}) but can only have a Max Score of 20!")
                        else:
                            input(f"\nAn error occurred. {increase} was not recognized as a valid input. Please try again")
                    else:
                        input("\nUnderstood. Transaction cancelled. Returning to menu")
            else:
                input(f"\n'{option}' was not recognized. Please input a number 1 - 6")
        elif option == "reset":
            reset = input(
                "You have selected 'reset' - Would you like to restart your character?\n"
                "\n(1) I yearn to see the world turn back, to see it bathed in the fires of change....!"
                "\n(2) WRONG LEVAAAAAAAA....\n\n ->")
            if reset == "1":
                input("\nOk there drama queen, goodness gracious. Here"
                      "\nhttps://tinyurl.com/dtr6trj6"
                      "\n\nPop this in your browser really fast. You're going to need it before you continue")
                return False
            elif reset == "2":
                input("\nDang it Kronk! Why do we even HAVE that leva?")

        else:
            input(f"\n'{option}' was not recognized. Please input a number")

    (input(
        f"\n\nHere are all of you final stats!!\n"
        f"\n({ab_score_stat_lst[0]}) Strength        (+{(ab_score_stat_lst[0] - 10) // 2})"
        f"\n({ab_score_stat_lst[1]}) Dexterity       (+{(ab_score_stat_lst[1] - 10) // 2})"
        f"\n({ab_score_stat_lst[2]}) Constitution    (+{(ab_score_stat_lst[2] - 10) // 2})"
        f"\n({ab_score_stat_lst[3]}) Intelligence    (+{(ab_score_stat_lst[3] - 10) // 2})"
        f"\n({ab_score_stat_lst[4]}) Wisdom          (+{(ab_score_stat_lst[4] - 10) // 2})"
        f"\n({ab_score_stat_lst[5]}) Charisma        (+{(ab_score_stat_lst[5] - 10) // 2})\n\n-> "))


    while True:
        weapons_items_spells = (
            input("Weapon time! What weapons or abilities do you want? Remember, your success with them directly"
              "\ndepends on your skills and skill scores!"
              "\n\n(1) Barbarian Build (Strength, Constitution)   < Start with Sword, Spear >"
              "\n(2) Rogue Build (Dexterity, Intelligence)   < Start with Bombs, Bow > "
              "\n(3) Bard Build (Dexterity, Charisma)   < Start with Firebolt, Heal spells >"
              "\n\nWhich build would you like?\n ->"))

        if weapons_items_spells not in ['1', '2', '3']:
            input("\nPlease input a number between 1 - 3")
        else:
            opt = int(weapons_items_spells) - 1
            print(f"\nPerfect! You have selected the '{pre_built_key[opt][0]}' build!")

            read_lines(pre_built_key[opt][1])

            weapons_stat_lst = pre_built_weapons_stat_lst[int(weapons_items_spells) - 1]
            items_stat_lst = pre_built_items_stat_lst[int(weapons_items_spells) - 1]
            spell_book = pre_built_spell_book_stat_lst[int(weapons_items_spells) - 1]
            break


    return ab_score_stat_lst, weapons_stat_lst, items_stat_lst, spell_book


def main():
    learning_to_select()
    test = choose_stats()
    print("Main stats   ----   Weapons   ----   Items   ----   Spells")
    print(test)

if __name__ == "__main__":
    main()
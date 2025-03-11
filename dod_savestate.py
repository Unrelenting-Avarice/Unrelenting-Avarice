# (([8, 17, 11, 11, 11, 17, ''], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 3, 0, 0, 0, 0, 0]), ([0,0], [0,0], [0,0]))
# [ Str, Con, Dex, Int, Wis, Cha , Name] ,
# [ Punch, Sword, Bow, Morning Star, Spear, PlaceHolderWeapon ] ,
# [ Bombs, arrows, Health Potions ] ,
# [ Heal, Firebolt]
#[Map values...]
import ast

def create_savestate(all_stat_values, map_values):
    """This function generates a random code that, if modified by the player, will break the code and won't run. It is
    created by generating 3 distinct keys, all relying on the players name to be randomized"""
    key_1 = 13579
    for value in all_stat_values[0][:-1]:
        key_1 += value

    key_1 *= len(all_stat_values[0][6])

    #print(key_1) # Key 1

    name_upper = 0
    name_lower = 0
    name_num = 0
    name_ascii = 0

    for char in all_stat_values[0][6]:
        if char.isupper():
            name_upper += 1
        elif char.islower():
            name_lower += 1
        elif char.isnumeric():
            name_num += 1
        else:
            name_ascii += 1
    key_2 = (name_upper, name_lower, name_num, name_ascii)
    #print(key_2)

    key_3 = 12
    for number in all_stat_values[1]:
        key_3 += number
    for number in all_stat_values[2]:
        key_3 += number
    for number in all_stat_values[3]:
        key_3 += number

    #print(key_3)

    return f"(({all_stat_values},{map_values}),[{key_1},{key_2},{key_3}])"




def return_too_save_state(save_state_code):

    player_name = save_state_code[0][0][0][-1]

    key_1_validate = save_state_code[1][0]
    key_2_validate = save_state_code[1][1]
    key_3_validate = save_state_code[1][2]

    key_1_val = 0

    for value in save_state_code[0][0][0][:-1]:
        key_1_val += value

    key_1_val = (key_1_val + 13579) * len(player_name)

    correct_keys = 0

    if key_1_val == key_1_validate:
        # print("True Key 1")
        correct_keys +=  1

    name_upper = 0
    name_lower = 0
    name_num = 0
    name_ascii = 0

    for char in player_name:
        if char.isupper():
            name_upper += 1
        elif char.islower():
            name_lower += 1
        elif char.isnumeric():
            name_num += 1
        else:
            name_ascii += 1
    key_2_val = (name_upper, name_lower, name_num, name_ascii)

    if key_2_val == key_2_validate:
        # print("True Key 2")
        correct_keys += 1

    key_3 = 12

    for number in save_state_code[0][0][1]:
        key_3 += number
    for number in save_state_code[0][0][2]:
        key_3 += number
    for number in save_state_code[0][0][3]:
        key_3 += number

    if key_3 == key_3_validate:
        # print("True Key 3")
        correct_keys += 1

    if correct_keys == 3:
        return True
    else:
        return False


def main():
    prev_save = input('\n\nDo you have a save state you would like to enter?\n(1) Yes\n(2) No\n\n->')
    if prev_save == "1":
        print("\nWARNING --- Attempts to cheat WILL crash your computer and the code !"
              "\nTo cancel, simply close the program and select 'No' the next time."
              "\nPlease only use Ctrl+C / Ctrl+V to get the values, then press 'Enter' ")


        save_this_code = input("Enter Save Code here:")
        exact_save_code = ast.literal_eval(save_this_code)

        #save_code = ((([8, 17, 11, 11, 11, 17, 'Billy101'], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 3, 0, 0, 0, 0, 0]),([0, 0], [0, 0], [0, 0])),[109232,(1, 4, 3, 0),17])
                    #((([8, 17, 11, 11, 11, 17, 'Billy101'], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 3, 0, 0, 0, 0, 0]),([0, 0], [0, 0], [0, 0])),[109232,(1, 4, 3, 0),17])



        # keys = [191156,(2, 11, 0, 1),30]

        if return_too_save_state(exact_save_code):
            print("Yay!")
        else:
            print("\nLIAR")
    else:
        print("Let's make one!")
        ans = create_savestate(([8, 17, 11, 11, 11, 17, 'Ungarrrr!Bunga'], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 3, 0, 0, 0, 0, 0]),([0,0], [0,0], [0,0]))
        print(ans)
        new_ans = ast.literal_eval(ans)
        print(new_ans[0][0])


if __name__ == "__main__":
    main()

    """
    ((  ([8, 17, 11, 11, 11, 17, 'Ungarrrr!Bunga'], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 3, 0, 0, 0, 0, 0], [0,0], [0,0], [0,0]),([0,0], [0,0], [0,0]) ),[191156,(2, 11, 0, 1),17])
    ((  ([8, 17, 11, 11, 11, 17, 'Ungarrrr!Bunga'], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 3, 0, 0, 0, 0, 0], [0,0], [0,0], [0,0]),([0,0], [0,0], [0,0])),[191156,(2, 11, 0, 1),30])

    """
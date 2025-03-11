
#from dod_random_dice import roll, advantage, disadvantage
from dod_random_dice import roll
from dod_item_desc import selection


class Entity:
    def __init__(self, name, health, damage, dmg_mod, attack_dialogues, armour_class, dodge):
        self.name = name
        self.health = health
        self.damage = damage
        self.dmg_mod = dmg_mod
        self.attack_dialogues = attack_dialogues
        self.armour_class = armour_class
        self.dodge = dodge

    def attack(self):
        dialogue = self.attack_dialogues()
        return self.damage, f"{dialogue}"

    def take_damage(self, num_dice, amount, mod):
        dmg_die = 0
        for i in range(num_dice):
            # temp_dmg = 0
            temp_dmg = roll(amount)
            print(f"Rolled a {temp_dmg} on the d{amount}")
            dmg_die += temp_dmg
        print(f"\nRolled a total of {dmg_die} on {num_dice}d{amount}")
        self.health -= (dmg_die + mod)
        if self.health < 0:
            self.health = 0

    def is_defeated(self):
        return self.health == 0

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Damage: {self.damage})"


class Player(Entity):
    def __init__(self, name, health, dmg_mod, armour_class, strength, constitution, dexterity, intelligence, wisdom,
                 charisma, weapons, items, spell_book, dodge):
        # Initialize the parent class (Entity)
        super().__init__(name, health, 0, dmg_mod, None, armour_class, dodge)

        # Player specific attributes
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.weapons = weapons
        self.items = items
        self.spell_book = spell_book
        self.dodge = dodge

    def choose_attack(self):

        print("\nSelect your next move:")
        available_weapons = [weapons for weapons in self.weapons if weapons[0] > 0]

        for idx, weapons in enumerate(available_weapons):
            print(f"{idx + 1}. {weapons[1]} (Damage: {weapons[2]}, Ability: {weapons[3]})")


        choice = input("Select a move #: ")
        if not choice.isnumeric():
            input(f"Not numeric value; You fumbled, so now you've lost your turn")
            return None
        choice = int(choice) - 1
        selected_weapon = available_weapons[choice]
        if selected_weapon[3] == "Strength":
            selected_weapon[3] = calc_mod(self.strength)
        elif selected_weapon[3] == "Dexterity":
            selected_weapon[3] = calc_mod(self.dexterity)
        print(f"\nYou chose: {selected_weapon[1]}")
        return selected_weapon

    def choose_item(self):
        print("\nSelect your item:")
        available_items = [items for items in self.items if items[0] > 0]

        if len(available_items) == 0:
            input("You don't have any of these to use!"
                  "Press ENTER to continue")
            return None

        for idx, items in enumerate(available_items):
            print(f"{idx + 1}. {items[1]} ({items[2]}, Ability: {items[3]}, Amount: {items[0]})")

        choice = input("Select a move #: ")
        if not choice.isnumeric():
            input(f"Not numeric value; You fumbled, so now you've lost your turn")
            return None
        else:
            choice = int(choice) - 1
            selected_item = available_items[choice]
            if selected_item[3] == "Strength":
                selected_item[3] = calc_mod(self.strength)
            elif selected_item[3] == "Dexterity":
                selected_item[3] = calc_mod(self.dexterity)
            elif selected_item[3] == "Strength":
                selected_item[3] = calc_mod(self.strength)
            print(f"\nYou chose: {selected_item[1]}")

        return selected_item

    def choose_spell(self):



        available_spells = [spells for spells in self.spell_book if spells[0] > 0]

        if len(available_spells) == 0:
            input("You don't have any of these to use!\n"
                  "Press ENTER to continue")
            return None

        for idx, spells in enumerate(available_spells):
            print(f"{idx + 1}. {spells[1]} ({spells[2]}, Ability: {spells[3]}, Amount: {spells[0]})")

        choice = input("Select a spell!\n\n-> ")
        if not choice.isnumeric():
            input(f"Not numeric value; You fumbled, so now you've lost your turn")
            return None
        choice = int(choice) - 1
        selected_item = available_spells[choice]
        if selected_item[3] == "Charisma":
            selected_item[3] = calc_mod(self.charisma)
        elif selected_item[3] == "Wisdom":
            selected_item[3] = calc_mod(self.wisdom)
        print(f"\nYou chose: {selected_item[1]}")
        return selected_item

    def calculate_ac(self):

        return self.armour_class + calc_mod(self.dexterity)

def calc_mod(score):
    if score < 9:
        return -1
    elif score // 2 == 0:
        return (score - 10)  // 2
    elif score // 2 != 0:
        return ((score + 1) - 10) // 2
    else:
        raise ValueError("Score cannot be computed")

def combat(enemy_name, hero_name):
    #Adjust values
    hero_name.armour_class = hero_name.calculate_ac()

    while not (enemy_name.is_defeated() or hero_name.is_defeated()):

        print("\nHere are the current stats!\n\n"
              f"{enemy_name.name}:\n"
              f"Health: {enemy_name.health}     "
              f"AC: {enemy_name.armour_class}\n\n"

              f"{hero_name.name}:\n"
              f"Health: {hero_name.health}      "
              f"AC: {hero_name.armour_class * hero_name.dodge}")

        secret_dev_door = input("\n\n- - // - -")

        if secret_dev_door == "Power Word Kill":
            print(f"With a single, unyielding strike, the spell obliterates the {enemy_name.name}, leaving nothing\n"
                  f"but a void where they once stood. The very essence of their being is erased,\n"
                  f"their existence wiped from reality with an unstoppable force that crushes all\n"
                  f"resistance. As the spell lands, the {enemy_name.name} is consumed by a blinding surge\n"
                  f"of energy, their body and soul unraveling in an instant. No trace remains, \n"
                  f"as if they were never there, their final breath snuffed out by the sheer dominance\n"
                  f"of annihilation. No shield, no defense, no plea for mercy can withstand its\n"
                  f"grip — once the power word is spoken, nothing escapes its wrath. It is the end\n"
                  f"of all things, a perfect erasure that leaves behind only the cold silence of\n"
                  f"absolute destruction.")

            input("\n- - // - -")
            enemy_name.health = 0
            break

        # Enemy attack

        rand_rol = roll(len(enemy_name.attack_dialogues)) - 1
        en_attk = enemy_name.attack_dialogues[rand_rol]

        print(f"\n{en_attk[0]}")
        dice_result = roll(20)
        if dice_result != 20:
            input(f"\nThe {enemy_name.name} rolled a {dice_result} (+{enemy_name.dmg_mod}) to hit!\n")
            crit = False
        else:
            print(f"\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
                  f"\n         * * OH NO!! THE {enemy_name.name} ROLLED A NATURAL {dice_result}! THAT'S A CRITICAL HIT!! * * *"
                  f"\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
            crit = True
            dice_result += 900
        input("\n")

        if dice_result + enemy_name.dmg_mod >= hero_name.armour_class * hero_name.dodge:
            old_h = hero_name.health
            if crit:
                hero_name.take_damage((en_attk[1] * 2), en_attk[2], en_attk[3])
            else:
                hero_name.take_damage(en_attk[1], en_attk[2], en_attk[3])
            # (1)d(2) + (3)
            # hero_name.take_damage(en_attk[1], en_attk[2], en_attk[3])
            print(
                f"\n{enemy_name.name} deals {old_h - hero_name.health} damage! You now have {hero_name.health} health.")
        else:
            print(f"\n{enemy_name.name} missed you due to your AC of {hero_name.armour_class * hero_name.dodge}!")

        if hero_name.health <= 0:
            break

        input("\n\n- - // - -")

        # Player attack

        print("\nYour turn!")
        hero_name.dodge = 1

        while True:
            response = input("\nWhat would you like to do?"
                             "\n(1) View Stats"
                             "\n(2) ATTACK!"
                             "\n(3) Dodge!"
                             "\n(4) Use Item!"
                             "\n(5) Open Spellbook!"
                             "\n\n -> ")
            if response == "1":
                input(
                    f"\nFull Stat List!\n"
                    f"\n(1) Strength        ({hero_name.strength} -> +{calc_mod(hero_name.strength)})    (2) Dexterity       ({hero_name.dexterity} -> +{calc_mod(hero_name.dexterity)})"
                    f"\n(3) Constitution    ({hero_name.constitution} -> +{calc_mod(hero_name.constitution)})    (4) Intelligence    ({hero_name.intelligence} -> +{calc_mod(hero_name.intelligence)})"
                    f"\n(5) Wisdom          ({hero_name.wisdom} -> +{calc_mod(hero_name.wisdom)})    (6) Charisma        ({hero_name.charisma} -> +{calc_mod(hero_name.charisma)})\n\n "
                    f"< Prepare to attack, the {enemy_name.name} is coming!! >\nPress ENTER to continue\n")

            if response == "3":
                input("\nYou decide to dodge and weave, giving up your attack to become twice as hard to hit for a turn")
                hero_name.dodge = 2
                break

            elif response == "4":
                print(selection("Item"))
                chosen_item = hero_name.choose_item()

                # BOMB CODE

                if chosen_item[1] == "Bomb":
                    hero_name.items[0][0] -= 1
                    print(selection("Bomb"))
                    chance = roll(20) + chosen_item[3]
                    print(chance)

                    if chance > 10:
                        dmg_dice_val = int(chosen_item[2][2:])
                        num_dice = int(chosen_item[2][0])
                        old_h = enemy_name.health
                        enemy_name.take_damage(num_dice, dmg_dice_val, int(chosen_item[3]))
                        print(f"\n{enemy_name.name} takes {old_h - enemy_name.health} damage! The {enemy_name.name} now has {enemy_name.health} health.")
                    else:
                        dmg_dice_val = int(chosen_item[2][2:])
                        num_dice = int(chosen_item[2][0])
                        old_h = hero_name.health
                        hero_name.take_damage(num_dice, dmg_dice_val, int(chosen_item[3]))
                        print(
                            f"\nYou take {old_h - hero_name.health} damage as the bomb rolls back at you! You now have {hero_name.health} health.")
                    break

                # elif chosen_item[1] == "Cure Wounds":
                #     print('healed')
                #     continue
                #
                # elif chosen_item[1] == "Health Potion":
                #     print('healed')
                #     continue
                #
                # elif chosen_item[1] == "Arrows":
                #     print('healed')
                #     continue
                #
                # elif chosen_item[1] == "Teleportation Staff":
                #     print('healed')
                #     continue

            elif response == "5":
                chosen_spell = hero_name.choose_spell()

                #

                if chosen_spell[1] == "Bomb":
                    hero_name.items[0][0] -= 1
                    print(selection("Bomb"))
                    chance = roll(20) + chosen_spell[3]
                    print(chance)

                    if chance > 10:
                        dmg_dice_val = int(chosen_spell[2][2:])
                        num_dice = int(chosen_spell[2][0])
                        old_h = enemy_name.health
                        enemy_name.take_damage(num_dice, dmg_dice_val, int(chosen_spell[3]))
                        print(
                            f"\n{enemy_name.name} takes {old_h - enemy_name.health} damage! The {enemy_name.name} now has {enemy_name.health} health.")
                    else:
                        dmg_dice_val = int(chosen_spell[2][2:])
                        num_dice = int(chosen_spell[2][0])
                        old_h = hero_name.health
                        hero_name.take_damage(num_dice, dmg_dice_val, int(chosen_spell[3]))
                        print(
                            f"\nYou take {old_h - hero_name.health} damage as the bomb rolls back at you! You now have {hero_name.health} health.")
                    break
            else:
                pass

        if response == 1:

            chosen_attack = hero_name.choose_attack()
            if not chosen_attack:
                continue  # Skip turn if no valid attack is chosen

            print("Here's Your value\n\n\n\n\n")
            print(chosen_attack)
            print(selection(chosen_attack[1]))
            input()
            dice_result = roll(20)
            if dice_result != 20:
                print(f"You rolled a {dice_result} (+{chosen_attack[3]}) to hit!")
                crit = False
            else:
                print(f"\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "
                      f"\n* * YOU ROLLED A NATURAL {dice_result}! THAT'S A CRITICAL HIT!! * *"
                      f"\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
                crit = True
                dice_result += 900
            input("\n")

            if dice_result + chosen_attack[3] >= enemy_name.armour_class:
                # print(chosen_attack) DEBUG
                dmg_dice_val = int(chosen_attack[2][2:])
                num_dice = int(chosen_attack[2][0])
                old_h = enemy_name.health
                if crit:
                    enemy_name.take_damage((num_dice * 2), dmg_dice_val, int(chosen_attack[3]))
                else:
                    enemy_name.take_damage(num_dice, dmg_dice_val, int(chosen_attack[3]))
                print(
                    f"\n{enemy_name.name} takes {old_h - enemy_name.health} damage! The {enemy_name.name} now has {enemy_name.health} health.")
            else:
                print(f"\n You missed the {enemy_name.name} due to its AC of {enemy_name.armour_class}!")

            input("\n\n- - // - -")

    if enemy_name.is_defeated():
        print(f"The {enemy_name.name} has been defeated!")

    elif hero_name.is_defeated():
        print(f"The {hero_name.name} has been defeated!")




# Example Usage
# if __name__ == "__main__":
#     # Create a player with stats
#     hero = Player(
#         name="Hero",
#         health=75,
#         dmg_mod=10,
#         armour_class=12,
#         strength=15,
#         constitution=15,
#         dexterity=18,
#         intelligence=10,
#         wisdom=8,
#         charisma=13,
#         weapons=[[1, "Adventurers sword", "2d8", "Strength"],
#                [1, "Punch", "1d4", "Strength"],
#                [0, "Bow", "3d6", "Dexterity"],
#                [0, "Firebolt", "2d20", "Intelligence"]],
#                 # Amount, name, dmg, ability mod
#
#         items=[[1, "Bomb", "2d12", "Dexterity"],
#                [1, "Cure Wounds", "1d20", "Wisdom"],
#                [1, "Health Potion", "3d12", "Constitution"],
#                [1, "Arrow", "1d6", "Dexterity"],
#                [1, "Teleportation Staff", "1d100", "Intelligence"]],
#                 # Amount, name, numeric, ability mod
#         dodge = 1
#
#     )
#
#     # Create an enemy (the dragon)
#     dragon = Entity(
#         name="Red Dragon",
#         health=100,
#         damage=35,
#         dmg_mod=7,
#         attack_dialogues=[
#             ["The dragon breathes fire!", 6, 12, 8],
#             ["The dragon swipes its claws!", 4, 6, 8],
#             ["The dragon roars, shaking the ground!", 6, 6, 6],
#             ["The dragon swipes with its tail!", 3, 8, 8]
#         ],
#         armour_class=18,
#         dodge=1
#     )

    # Calculate adjusted player damage and health


    # Simulate a battle

    # combat(dragon, hero)



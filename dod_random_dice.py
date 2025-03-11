import random

# Generate a random number between 1 and 20

def roll(dice_type):
    return random.randint(1, dice_type)

def advantage(dice_type):
    roll_1 = random.randint(1, dice_type)
    roll_2 = random.randint(1, dice_type)
    # print(f"{roll_1} and {roll_2}")
    if roll_1 >= roll_2:
        return roll_1
    else:
        return roll_2

def disadvantage(dice_type):
    roll_1 = random.randint(1, dice_type)
    roll_2 = random.randint(1, dice_type)
    # print(f"{roll_1} and {roll_2}")
    if roll_1 < roll_2:
        return roll_1
    else:
        return roll_2

def main():
    print(roll(20))
    print(advantage(20))
    print(disadvantage(20))


if __name__ == "__main__":
    main()
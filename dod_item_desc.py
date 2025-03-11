import random

items = {

    "Item": [
        "You’ve chosen the mighty power of the item. Let’s see how it fares!",
        "A wise choice! The item will surely make a difference!",
        "Prepare yourself! The item is about to change the tide of battle!"
    ],

    "Health Potion": [
            "Drinking the potion provides a burst of renewed energy.",
            "The potion restores some of your lost health, making you feel revitalized.",
            "The healing potion works quickly, filling you with strength once more."
    ],

    "Bomb": [
            "A deafening explosion erupts from the thrown bomb.",
            "The bomb detonates, sending debris flying in all directions.",
            "A massive blast shakes the ground and creates a fiery shockwave."
    ],

    "Arrow": [
          "You stab it in the face . . . with an arrow? Try firing it from a *bow* next time"
    ],


    # WEAPON DESCRIPTIONS


    "Sword": [
        "A swift and clean slash with the adventurer's trusty sword.",
        "A powerful strike that cleaves through the enemy's defenses.",
        "A precise jab aimed straight at the heart."
    ],
    "Punch": [
        "A solid punch lands with a satisfying thud.",
        "A quick jab hits the enemy square in the chest.",
        "A devastating uppercut sends the enemy stumbling back."
    ],
    "Bow": [
        "An arrow flies through the air, seeking its target.",
        "A rapid shot hits its mark with pinpoint accuracy.",
        "A long-range shot pierces the air with deadly precision."
    ],

    "Morning Star": [
        "Attack 1",
        "Attack 2",
        "Attack 3"
    ],
    "Spear": [
        "Attack 1",
        "Attack 2",
        "Attack 3"
    ],
    "PlaceHolderWeapon": [
        "Attack 1",
        "Attack 2",
        "Attack 3"
    ],


    # SPELL DESCRIPTIONS


    "Firebolt": [
        "A blazing ball of fire streaks toward the enemy.",
        "A fiery explosion erupts from your hands, engulfing your target.",
        "A scorching fireball hurls through the air, incinerating anything in its path."
    ],
    "Cure Wounds": [
        "A soft glow restores vitality to the wounded.",
        "Healing energy flows through you, mending your injuries.",
        "A wave of calming energy heals the most grievous wounds."
    ]

}

def selection(item_name):
    if len(item_name) > 1:
        for item in item_name.split():
            if item in items:
                selected_item_key = item
    else:
        selected_item_key = item_name

    description = random.choice(items[selected_item_key])
    return f"{description}"
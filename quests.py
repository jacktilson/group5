# Setting the default quest
current_quest = 1

# Dictionaries containing all of the quest data

quest_1 = {
    "id": "1",

    "name": "The Departure",

    "description": "Help MJ and Simon move offices.",

    "criteria": 
    
    """
    (item_laptop in rooms["Parking"]["items"]) and (item_pen in rooms["Parking"]["items"]) and (item_biscuits in rooms["Parking"]["items"])    
    """,

    }

quest_2 = {
    "id": "2",

    "name": "The Handbook",

    "description": "Its time for you to drop off the handbook at the office",

    "criteria": 
    
    """
    (item_handbook in rooms["Office"]["items"]
    """,

    }




quest_numbers = {
    1: quest_1,
    2: quest_2,
}
from map import rooms
from player import *
from items import *
from gameparser import *
import string

# Setting the default quest, i.e. that at the start of play
current_quest = 1

# Dictionaries containing all of the quest data.



# Details for the first quest
quest_1 = {
    "id": "1",

    "name": "The Departure",

    "description": "Help MJ and Simon move offices. Its really important",

    "criteria": """(item_laptop in rooms["Kirill"]["items"])""",

    "name_art": 
    
"""
.___________. __    __   _______     _______   _______ .______      ___      .______     .___________. __    __  .______       _______ 
|           ||  |  |  | |   ____|   |       \ |   ____||   _  \    /   \     |   _  \    |           ||  |  |  | |   _  \     |   ____|
`---|  |----`|  |__|  | |  |__      |  .--.  ||  |__   |  |_)  |  /  ^  \    |  |_)  |   `---|  |----`|  |  |  | |  |_)  |    |  |__   
    |  |     |   __   | |   __|     |  |  |  ||   __|  |   ___/  /  /_\  \   |      /        |  |     |  |  |  | |      /     |   __|  
    |  |     |  |  |  | |  |____    |  '--'  ||  |____ |  |     /  _____  \  |  |\  \----.   |  |     |  `--'  | |  |\  \----.|  |____ 
    |__|     |__|  |__| |_______|   |_______/ |_______|| _|    /__/     \__\ | _| `._____|   |__|      \______/  | _| `._____||_______|
"""

    }

# Details for the second quest
quest_2 = {
    "id": "2",

    "name": "The Handbook",

    "description": "Its time for you to drop off the handbook at the office",

    "criteria": """(item_handbook in rooms["Outside"]["items"])""",

    "name_art":

    """
  _____ _            _   _                 _ _                 _    
 |_   _| |__   ___  | | | | __ _ _ __   __| | |__   ___   ___ | | __
   | | | '_ \ / _ \ | |_| |/ _` | '_ \ / _` | '_ \ / _ \ / _ \| |/ /
   | | | | | |  __/ |  _  | (_| | | | | (_| | |_) | (_) | (_) |   < 
   |_| |_| |_|\___| |_| |_|\__,_|_| |_|\__,_|_.__/ \___/ \___/|_|\_\
                                                                    
    """


    }


# Dictionary of quest IDs referred to in game.py
quest_numbers = {
    1: quest_1,
    2: quest_2,
}
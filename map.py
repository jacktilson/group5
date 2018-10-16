from items import *

"""This file is referred to by various functions in game.py to ascertain where different exits lead to
and to enable the efficient reporting of different room names, which items are in them and the movement
of items from those rooms into the inventory of the player in player.py"""

room_reception = {
    "name": "Reception",

    "description":
    """You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""",

    "exits": {"south": "Admins", "east": "Tutor", "west": "Parking"},

    "items": [item_biscuits, item_handbook],

    "entry_art":
    """
    
  _____           _                   _                     ____                                 _     _                             
 | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _    |  _ \    ___    ___    ___   _ __   | |_  (_)   ___    _ __              
 |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   | |_) |  / _ \  / __|  / _ \ | '_ \  | __| | |  / _ \  | '_ \             
 | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |   |  _ <  |  __/ | (__  |  __/ | |_) | | |_  | | | (_) | | | | |  _   _   _ 
 |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |   |_| \_\  \___|  \___|  \___| | .__/   \__| |_|  \___/  |_| |_| (_) (_) (_)
                                                  |___/                                 |_|                                          
    """
}

room_admins = {
    "name": "MJ and Simon's room",

    "description":
    """You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""",

    "exits":  {"north": "Reception"},

    "items": [],

    "entry_art": 
    """
    
  _____           _                   _                        _          _               _                           
 | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _       / \      __| |  _ __ ___   (_)  _ __    ___             
 |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |     / _ \    / _` | | '_ ` _ \  | | | '_ \  / __|            
 | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |    / ___ \  | (_| | | | | | | | | | | | | | \__ \  _   _   _ 
 |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |   /_/   \_\  \__,_| |_| |_| |_| |_| |_| |_| |___/ (_) (_) (_)
                                                  |___/                                                               
    """
}

room_tutor = {
    "name": "your personal tutor's office",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    "exits": {"west": "Reception"},

    "items": [],

    "entry_art": 
    """
    
  _____           _                   _                     _____           _                              
 | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _    |_   _|  _   _  | |_    ___    _ __             
 |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |     | |   | | | | | __|  / _ \  | '__|            
 | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |     | |   | |_| | | |_  | (_) | | |     _   _   _ 
 |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |     |_|    \__,_|  \__|  \___/  |_|    (_) (_) (_)
                                                  |___/                                                    
    """
}

room_parking = {
    "name": "the parking lot",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    "exits": {"east": "Office", "south": "Reception"},

    "items": [],

    "entry_art":
    """
    
  _____           _                   _                     ____                   _      _                             
 | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _    |  _ \    __ _   _ __  | | __ (_)  _ __     __ _             
 |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   | |_) |  / _` | | '__| | |/ / | | | '_ \   / _` |            
 | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |   |  __/  | (_| | | |    |   <  | | | | | | | (_| |  _   _   _ 
 |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |   |_|      \__,_| |_|    |_|\_\ |_| |_| |_|  \__, | (_) (_) (_)
                                                  |___/                                               |___/             
    """
}

room_office = {
    "name": "the general office",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"west": "Parking"},

    "items": [item_pen],

    "entry_art":
    """
    
  _____           _                   _                      ___     __    __   _                           
 | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _     / _ \   / _|  / _| (_)   ___    ___             
 |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   | | | | | |_  | |_  | |  / __|  / _ \            
 | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |   | |_| | |  _| |  _| | | | (__  |  __/  _   _   _ 
 |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |    \___/  |_|   |_|   |_|  \___|  \___| (_) (_) (_)
                                                  |___/                                                     
    """
}



rooms = {
    "Reception": room_reception,
    "Admins": room_admins,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office
}

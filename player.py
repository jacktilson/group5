from items import *
from map import rooms

# Declare what the player is holding at outset
inventory = [item_id, item_laptop, item_money]

# How many kilograms can the player carry?
max_weight_allowed = 3

# Start game at the reception
current_room = rooms["Reception"]

# Description of what we need to do to win.
victory_req = """TBC"""
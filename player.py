from items import *
from map import rooms

# Hold the name of the player, blank by default:
global player_name
player_name = ""

# Declare what the player is holding at outset
inventory = [item_phone, item_wallet]

# How many kilograms can the player carry?
max_weight_allowed = 3

# Start game at the reception
current_room = rooms["Outside"]

from items import *
from map import rooms

# Declare what the player is holding at outset
inventory = []

# How many kilograms can the player carry?
max_weight_allowed = 3

# Start game at the reception
current_room = rooms["Kitchen"]

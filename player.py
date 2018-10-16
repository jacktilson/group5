from items import *
from map import rooms

# Declare what the player is holding at outset
inventory = [item_id, item_laptop, item_money]

# How many kilograms can the player carry?
max_weight_allowed = 3.0

# Start game at the reception
current_room = rooms["Reception"]

# Description of what we need to do to win.
victory_req = """Quest: MJ and Simon are moving offices, and they need your help! \n
              They have loaded most of their things into the van but as you are carrying \n
              Simon's laptop to the car park, you notice his biscuits on the ground in Reception. \n
             Go and grab them before somebody stomps on them!!! MJ left his diamond \n
             encrusted pen in the main office too. Somebody is bound to steal it so... \n
             ... Grab that too :) \n \n """
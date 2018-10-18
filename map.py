from items import *

"""This file is referred to by various functions in game.py to ascertain where different exits lead to
and to enable the efficient reporting of different room names, which items are in them and the movement
of items from those rooms into the inventory of the player in player.py"""


room_outside = {
    "name": "Outside",

    "description":
    """It's your first day. Lighten up... Please don't tell me I have to
teach you how to open a door... Please.""",

    "exits": {"north": "Main"},

    "items": [item_rock],

    "song": "outside.mp3",

    "entry_art":
"\n" \
"\n" \
"  _____           _                   _                      ___            _           _       _                     \n" \
" | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _     / _ \   _   _  | |_   ___  (_)   __| |   ___              \n" \
" |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   | | | | | | | | | __| / __| | |  / _` |  / _ \             \n" \
" | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |   | |_| | | |_| | | |_  \__ \ | | | (_| | |  __/  _   _   _  \n" \
" |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |    \___/   \__,_|  \__| |___/ |_|  \__,_|  \___| (_) (_) (_) \n" \
"                                                  |___/                                                               \n" \
"\n",

    "required_items": [],

    "required_current_quest_min": 1
}


room_main = {
    "name": "The Main Office",

    "description":
    """You see an abundance of smartly dressed
people at their desks. They're speaking but the telephone rings make it difficult
to hear them... One guy seems to be eating a turkey sandwich... Maybe its chicken...
Same thing... Right?""",

    "exits": {"south": "Outside", "east": "Security", "west": "Spoons", "north": "Kitchen"},

    "items": [item_newspaper, item_tea],

    "song": "main.mp3",

    "entry_art":
"\n" \
"\n" \
"  _____           _                   _                     __  __           _              ___     __    __   _                            \n" \
" | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _    |  \/  |   __ _  (_)  _ __      / _ \   / _|  / _| (_)   ___    ___              \n" \
" |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   | |\/| |  / _` | | | | '_ \    | | | | | |_  | |_  | |  / __|  / _ \             \n" \
" | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |   | |  | | | (_| | | | | | | |   | |_| | |  _| |  _| | | | (__  |  __/  _   _   _  \n" \
" |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |   |_|  |_|  \__,_| |_| |_| |_|    \___/  |_|   |_|   |_|  \___|  \___| (_) (_) (_) \n" \
"                                                  |___/                                                                                     \n" \
"\n",

    "required_items": [],

    "required_current_quest_min": 1
}

room_kitchen = {
    "name": "The Kitchen",

    "description":
    """There seems to be an awful song from the seventies playing here... Kirill
must be around here somewhere... surely. Anyway, at least now you can make
the tea...""",

    "exits":  {"south": "Main"},

    "items": [item_kettle, item_milk, item_sugar],

    "song": "kitchen.mp3",

    "entry_art": 
"\n" \
"\n" \
"  _____           _                   _                     _  __  _   _            _                                 \n" \
" | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _    | |/ / (_) | |_    ___  | |__     ___   _ __               \n" \
" |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   | ' /  | | | __|  / __| | '_ \   / _ \ | '_ \              \n" \
" | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |   | . \  | | | |_  | (__  | | | | |  __/ | | | |  _   _   _  \n" \
" |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |   |_|\_\ |_|  \__|  \___| |_| |_|  \___| |_| |_| (_) (_) (_) \n" \
"                                                  |___/                                                               \n" \
"\n",

    "required_items": [],

    "required_current_quest_min": 2
}

room_security = {
    "name": "The Security Suite",

    "description":
    """There is a guy who seems to be half asleep in the corner.
There's also a giant hammer in the corner. It looks pretty heavy.
Perhaps you might need that for something... someday.""",

    "exits": {"west": "Main", "south": "Kirill"},

    "items": [item_id, item_hammer],

    "song": "security.mp3",

    "entry_art": 
"\n" \
"\n" \
"  _____           _                   _                     ____                                 _   _               ____            _   _                       \n" \
" | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _    / ___|    ___    ___   _   _   _ __  (_) | |_   _   _    / ___|   _   _  (_) | |_    ___              \n" \
" |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   \___ \   / _ \  / __| | | | | | '__| | | | __| | | | |   \___ \  | | | | | | | __|  / _ \             \n" \
" | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |    ___) | |  __/ | (__  | |_| | | |    | | | |_  | |_| |    ___) | | |_| | | | | |_  |  __/  _   _   _  \n" \
" |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |   |____/   \___|  \___|  \__,_| |_|    |_|  \__|  \__, |   |____/   \__,_| |_|  \__|  \___| (_) (_) (_) \n" \
"                                                  |___/                                                    |___/                                                 \n" \
"\n",

    "required_items": [],

    "required_current_quest_min": 1
}

room_spoons = {
    "name": "Spoons",

    "description":
    """You've just walked in and can see Jing, that other lecturer, sat down near
the window. She says that Kirill had started taking up singing lessons down in
the Opera House... Perhaps we should check there. She asks you to buy her a drink.
You refuse... Because there is much more important business at hand.""",

    "exits": {"east": "Main", "south": "Opera"},

    "items": [item_beer, item_jager, item_vodka],

    "song": "spoons.mp3",

    "entry_art":
"\n" \
"\n" \
"  _____           _                   _                     ____                                               __   \n" \
" | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _    / ___|   _ __     ___     ___    _ __    ___     _  \ \  \n" \
" |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   \___ \  | '_ \   / _ \   / _ \  | '_ \  / __|   (_)  | | \n" \
" | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |    ___) | | |_) | | (_) | | (_) | | | | | \__ \    _   | | \n" \
" |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |   |____/  | .__/   \___/   \___/  |_| |_| |___/   ( )  | | \n" \
"                                                  |___/            |_|                                     |/  /_/  \n" \
"\n",

    "required_items": [],

    "required_current_quest_min": 3
}

room_opera = {
    "name": "The Opera House",

    "description":
    """Hmm... It seems like those singing lessons that Jing was talking
about are paying off. This is music to your ears, you think to yourself.
You take a closer look, but clearly this isn't the guy you're looking for.
What you do notice, however, is a mysterious door with "Pandora's Box" 
written on it. Perhaps it's important?""",

    "exits": {"north": "Spoons", "south": "Pandora"},

    "items": [],

    "song": "opera.mp3",

    "entry_art":
"\n" \
"\n" \
"  _____           _                   _                      ___                                    _   _                                           \n" \
" | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _     / _ \   _ __     ___   _ __    __ _    | | | |   ___    _   _   ___    ___              \n" \
" |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   | | | | | '_ \   / _ \ | '__|  / _` |   | |_| |  / _ \  | | | | / __|  / _ \             \n" \
" | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |   | |_| | | |_) | |  __/ | |    | (_| |   |  _  | | (_) | | |_| | \__ \ |  __/  _   _   _  \n" \
" |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |    \___/  | .__/   \___| |_|     \__,_|   |_| |_|  \___/   \__,_| |___/  \___| (_) (_) (_) \n" \
"                                                  |___/            |_|                                                                              \n" \
"\n",

    "required_items": [],

    "required_current_quest_min": 3
}

room_pandora = {
    "name": "Pandora's Box",

    "description":
    """You enter a dark room. You hear a roaring sound coming from the far
corner of the room, followed by a mighty grunt. Suddenly, the light comes
on. It's Kirill! He's fighting a grizzly bear and seems to be winning!""",

    "exits": {"south": "Spoons", "east": "Kitchen"},

    "items": [],

    "song": "pandora.mp3",

    "entry_art":
"\n" \
"\n" \
"███████╗███╗   ██╗████████╗███████╗██████╗ ██╗███╗   ██╗ ██████╗     ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ██████╗  █████╗ ███████╗    ██████╗  ██████╗ ██╗  ██╗ \n" \
"██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██║████╗  ██║██╔════╝     ██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗╚██╗██╔╝ \n" \
"█████╗  ██╔██╗ ██║   ██║   █████╗  ██████╔╝██║██╔██╗ ██║██║  ███╗    ██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██████╔╝███████║███████╗    ██████╔╝██║   ██║ ╚███╔╝  \n" \
"██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██║██║╚██╗██║██║   ██║    ██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██║   ██║██╔══██╗██╔══██║╚════██║    ██╔══██╗██║   ██║ ██╔██╗  \n" \
"███████╗██║ ╚████║   ██║   ███████╗██║  ██║██║██║ ╚████║╚██████╔╝    ██║     ██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║  ██║██║  ██║███████║    ██████╔╝╚██████╔╝██╔╝ ██╗ \n" \
"╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ \n" \
"\n",

    "required_items": [item_hammer],

    "required_current_quest_min": 5
}

room_kirill = {
    "name": "Kirill's Office",

    "description":
    """This must be where Kirill spends his working day... Right?
Perhaps you're missing something, because the only thing that's here
to drink the tea you just made is the model Linux penguin in the corner.""",

    "exits": {"north": "Security"},

    "items": [item_penguin, item_putin, item_cash],

    "song": "kirill.mp3",

    "entry_art":
"\n" \
"\n" \
"  _____           _                   _                     _  __  _          _   _   _   _            ___     __    __   _                            \n" \
" | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _    | |/ / (_)  _ __  (_) | | | | ( )  ___     / _ \   / _|  / _| (_)   ___    ___              \n" \
" |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   | ' /  | | | '__| | | | | | | |/  / __|   | | | | | |_  | |_  | |  / __|  / _ \             \n" \
" | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |   | . \  | | | |    | | | | | |     \__ \   | |_| | |  _| |  _| | | | (__  |  __/  _   _   _  \n" \
" |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |   |_|\_\ |_| |_|    |_| |_| |_|     |___/    \___/  |_|   |_|   |_|  \___|  \___| (_) (_) (_) \n" \
"                                                  |___/                                                                                                \n" \
"\n",

    "required_items": [item_id, item_tea],

    "required_current_quest_min": 2
}



rooms = {
    "Outside": room_outside,
    "Main": room_main,
    "Kitchen": room_kitchen,
    "Security": room_security,
    "Spoons": room_spoons,
    "Opera": room_opera,
    "Pandora": room_pandora,
    "Kirill": room_kirill
}

#!/usr/bin/python3
# coding=utf-8

from map import rooms
from player import *
from items import *
from gameparser import *
from quests import *
import string
import music
import pyttsx3
import time
import pygame

def opening():
    """This function is called prior to the game loop, as such it shows its contents
    prior to the game actually starting"""
    
    # Clear screen
    print("\n" * 500)
    # Start playing initial soundtrack
    global set_song
    set_song(current_room["song"])
    # ASCII art to promt user to use speakers
    print(
"\n" \
"\n" \
"████████╗██╗   ██╗██████╗ ███╗   ██╗     ██████╗ ███╗   ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗██████╗     ███████╗██████╗ ███████╗ █████╗ ██╗  ██╗███████╗██████╗ ███████╗██╗ \n" \
"╚══██╔══╝██║   ██║██╔══██╗████╗  ██║    ██╔═══██╗████╗  ██║    ╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗    ██╔════╝██╔══██╗██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗██╔════╝██║ \n" \
"   ██║   ██║   ██║██████╔╝██╔██╗ ██║    ██║   ██║██╔██╗ ██║     ╚████╔╝ ██║   ██║██║   ██║██████╔╝    ███████╗██████╔╝█████╗  ███████║█████╔╝ █████╗  ██████╔╝███████╗██║ \n" \
"   ██║   ██║   ██║██╔══██╗██║╚██╗██║    ██║   ██║██║╚██╗██║      ╚██╔╝  ██║   ██║██║   ██║██╔══██╗    ╚════██║██╔═══╝ ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗╚════██║╚═╝ \n" \
"   ██║   ╚██████╔╝██║  ██║██║ ╚████║    ╚██████╔╝██║ ╚████║       ██║   ╚██████╔╝╚██████╔╝██║  ██║    ███████║██║     ███████╗██║  ██║██║  ██╗███████╗██║  ██║███████║██╗ \n" \
"   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═══╝       ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝ \n" \
"\n" \
"\n"
)
    # Hold script for 5 seconds
    time.sleep(5)
    # Clear screen
    print("\n" * 300)
    # Hold script for 2 seconds
    time.sleep(2)
    # Tron welcomes player
    text_to_speech("Welcome!")
    # Tron ASCII introduction
    print(
# Double backslash must be properly escaped in TRON 5000's nose
"\n" \
"████████╗██████╗  ██████╗ ███╗   ██╗    ███████╗ ██████╗  ██████╗  ██████╗  \n" \
"╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║    ██╔════╝██╔═████╗██╔═████╗██╔═████╗ \n" \
"   ██║   ██████╔╝██║   ██║██╔██╗ ██║    ███████╗██║██╔██║██║██╔██║██║██╔██║ \n" \
"   ██║   ██╔══██╗██║   ██║██║╚██╗██║    ╚════██║████╔╝██║████╔╝██║████╔╝██║ \n" \
"   ██║   ██║  ██║╚██████╔╝██║ ╚████║    ███████║╚██████╔╝╚██████╔╝╚██████╔╝ \n" \
"   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝  \n" \
"\n" \
"                __________                 \n" \
"         ______/ ________ \______          \n" \
"       _/      ____________      \_        \n" \
"     _/____________    ____________\_      \n" \
"    /  ___________ \  / ___________  \     \n" \
"   /  /           \ \/ /           \  \    \n" \
"  /  /            /    \            \  \   \n" \
"  |  \           / _  _ \           /  |   \n" \
"__|\_____   ___   //  \\\\   ___   _____/|__ \n" \
"[_       \     \  X    X  /     /       _] \n" \
"__|     \ \                    / /     |__ \n" \
"[____  \ \ \   ____________   / / /  ____] \n" \
"     \  \ \ \/||.||.||.||.||\/ / /  /      \n" \
"      \_ \ \  ||.||.||.||.||  / / _/       \n" \
"        \ \   ||.||.||.||.||   / /         \n" \
"         \_   ||_||_||_||_||   _/          \n" \
"           \     ........     /            \n" \
"            \________________/             \n" \
"\n" \
"\n" \
"\n" \
"██╗   ██╗ ██████╗ ██╗   ██╗██████╗      ██████╗ ██╗      █████╗ ███╗   ███╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗███████╗     █████╗ ███████╗███████╗██╗███████╗████████╗ █████╗ ███╗   ██╗████████╗ \n" \
"╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗    ██╔════╝ ██║     ██╔══██╗████╗ ████║██╔═══██╗██╔══██╗██╔═══██╗██║   ██║██╔════╝    ██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║╚══██╔══╝ \n" \
" ╚████╔╝ ██║   ██║██║   ██║██████╔╝    ██║  ███╗██║     ███████║██╔████╔██║██║   ██║██████╔╝██║   ██║██║   ██║███████╗    ███████║███████╗███████╗██║███████╗   ██║   ███████║██╔██╗ ██║   ██║    \n" \
"  ╚██╔╝  ██║   ██║██║   ██║██╔══██╗    ██║   ██║██║     ██╔══██║██║╚██╔╝██║██║   ██║██╔══██╗██║   ██║██║   ██║╚════██║    ██╔══██║╚════██║╚════██║██║╚════██║   ██║   ██╔══██║██║╚██╗██║   ██║    \n" \
"   ██║   ╚██████╔╝╚██████╔╝██║  ██║    ╚██████╔╝███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝███████║    ██║  ██║███████║███████║██║███████║   ██║   ██║  ██║██║ ╚████║   ██║    \n" \
"   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    \n" \
"\n" \
"\n" \
"\n" \
"\n"
)
    # Hold script for 1 second.
    time.sleep(1)
    # Tron 500 introduces itself.
    text_to_speech("My name is Tron Five Thousand. I will be your guide.")
    # Hold script for 2 seconds.
    time.sleep(2)
    # Tron hopes the player is ready for the ride of their life.
    text_to_speech("I hope you're ready for the ride of your life...")
    # Hold script for 0.5 seconds
    time.sleep(0.5)
    # Clear screen
    print("\n" * 300)
    # ASCII art of "This"
    print(
"\n" \
"\n" \
" ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  \n" \
"▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ \n" \
" ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  \n" \
"     ▐░▌     ▐░▌       ▐░▌     ▐░▌     ▐░▌           \n" \
"     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄  \n" \
"     ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌ \n" \
"     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌ \n" \
"     ▐░▌     ▐░▌       ▐░▌     ▐░▌               ▐░▌ \n" \
"     ▐░▌     ▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌ \n" \
"     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ \n" \
"      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  \n" \
"\n"
)
    # Tron says "this"
    text_to_speech("This")
    # Create a little room below
    print("\n" * 5)
    # Hold the script for 0.5 seconds.
    time.sleep(0.5)
    # ASCII art of "Is"
    print(
"\n" \
"\n" \
" ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  \n" \
"▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ \n" \
" ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  \n" \
"     ▐░▌     ▐░▌           \n" \
"     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄  \n" \
"     ▐░▌     ▐░░░░░░░░░░░▌ \n" \
"     ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌ \n" \
"     ▐░▌               ▐░▌ \n" \
" ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌ \n" \
"▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ \n" \
" ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  \n" \
"\n"
)
    # Tron says "is"
    text_to_speech("Iz")
    # Clear screen
    print("\n" * 300)
    # Hold the script for 0.5 seconds
    time.sleep(0.5)
    # Print Tea Boy ASCII art
    print(
"\n" \
"\n" \
"\n" \
"\n" \
"\n" \
" .----------------.  .----------------.  .----------------.           .----------------.  .----------------.  .----------------.  \n" \
"| .--------------. || .--------------. || .--------------. |         | .--------------. || .--------------. || .--------------. | \n" \
"| |  _________   | || |  _________   | || |      __      | |         | |   ______     | || |     ____     | || |  ____  ____  | | \n" \
"| | |  _   _  |  | || | |_   ___  |  | || |     /  \     | |         | |  |_   _ \    | || |   .'    `.   | || | |_  _||_  _| | | \n" \
"| | |_/ | | \_|  | || |   | |_  \_|  | || |    / /\ \    | |         | |    | |_) |   | || |  /  .--.  \  | || |   \ \  / /   | | \n" \
"| |     | |      | || |   |  _|  _   | || |   / ____ \   | |         | |    |  __'.   | || |  | |    | |  | || |    \ \/ /    | | \n" \
"| |    _| |_     | || |  _| |___/ |  | || | _/ /    \ \_ | |         | |   _| |__) |  | || |  \  `--'  /  | || |    _|  |_    | | \n" \
"| |   |_____|    | || | |_________|  | || ||____|  |____|| |         | |  |_______/   | || |   `.____.'   | || |   |______|   | | \n" \
"| |              | || |              | || |              | |         | |              | || |              | || |              | | \n" \
"| '--------------' || '--------------' || '--------------' |         | '--------------' || '--------------' || '--------------' | \n" \
" '----------------'  '----------------'  '----------------'           '----------------'  '----------------'  '----------------'  \n" \
"\n" \
"\n" \
"\n" \
"\n" \
"\n" 
)
    # Tron says "Tea Boy"
    text_to_speech("Tea Boy")
    # Hold the script for 2 seconds
    time.sleep(2)
    # Clear screen
    print("\n" * 300)
    # Reprint Tea Boy ASCII art
    print(
"\n" \
"\n" \
"\n" \
"\n" \
"\n" \
" .----------------.  .----------------.  .----------------.           .----------------.  .----------------.  .----------------.  \n" \
"| .--------------. || .--------------. || .--------------. |         | .--------------. || .--------------. || .--------------. | \n" \
"| |  _________   | || |  _________   | || |      __      | |         | |   ______     | || |     ____     | || |  ____  ____  | | \n" \
"| | |  _   _  |  | || | |_   ___  |  | || |     /  \     | |         | |  |_   _ \    | || |   .'    `.   | || | |_  _||_  _| | | \n" \
"| | |_/ | | \_|  | || |   | |_  \_|  | || |    / /\ \    | |         | |    | |_) |   | || |  /  .--.  \  | || |   \ \  / /   | | \n" \
"| |     | |      | || |   |  _|  _   | || |   / ____ \   | |         | |    |  __'.   | || |  | |    | |  | || |    \ \/ /    | | \n" \
"| |    _| |_     | || |  _| |___/ |  | || | _/ /    \ \_ | |         | |   _| |__) |  | || |  \  `--'  /  | || |    _|  |_    | | \n" \
"| |   |_____|    | || | |_________|  | || ||____|  |____|| |         | |  |_______/   | || |   `.____.'   | || |   |______|   | | \n" \
"| |              | || |              | || |              | |         | |              | || |              | || |              | | \n" \
"| '--------------' || '--------------' || '--------------' |         | '--------------' || '--------------' || '--------------' | \n" \
" '----------------'  '----------------'  '----------------'           '----------------'  '----------------'  '----------------'  \n" \
"\n" \
"\n" \
"\n" \
"\n" \
"\n" 
)
    # Supplement the above with a Loading Game art whilst Tron talks.
    print(
"\n" \
"\n" \
"\n" \
" ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄           \n" \
"▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌          \n" \
"▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀           \n" \
"▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌    ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌               ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌                    \n" \
"▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌    ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░▌ ▄▄▄▄▄▄▄▄      ▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄           \n" \
"▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌    ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░▌▐░░░░░░░░▌     ▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌          \n" \
"▐░▌          ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌    ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░▌ ▀▀▀▀▀▀█░▌     ▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀           \n" \
"▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌    ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌                    \n" \
"▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄  ▄  ▄  ▄  \n" \
"▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌▐░▌▐░▌ \n" \
" ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀  ▀  ▀  \n" \
"\n" \
"\n" \
"\n" 
)
    # Hold the script for 1 second
    time.sleep(1)
    # Tron warns this ain't no game
    text_to_speech("This ain't no game. This is reality for apprentices... up and down the country... You're lucky you came to University.")
    # Hold script for 2 seconds
    time.sleep(2)
    # Tron details the first quest
    text_to_speech("Its time for your very first quest... It's called... " + str(quest_numbers[current_quest]["name"]) + "... To complete this quest you must... " + str(quest_numbers[current_quest]["description"]) + "... ")
    # Hold the script for 1 second
    time.sleep(1)
    # Give name and description of current room
    text_to_speech("You're entering " + current_room["name"] + ". " + current_room["description"].replace("\n"," "))
    # Hold the script for 1 second
    time.sleep(1)
    # Tron tells apprentice to get going
    text_to_speech("Now off you go, apprentice.")
    # Clear screen
    print("\n" * 300)

    return


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    holding_array = []
    number_of_items = len(holding_array)

    for thing in items:
        holding_array.append(thing["name"])

    return ", ".join([str(name) for name in holding_array])


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if len(room["items"]) > 0:
        print("There is " + list_of_items(room["items"]) + " here." + "\n")
        return
    else:
        # Do nothing.
        pass

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    print("You have " + list_of_items(inventory) + "." + "\n")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(
"""
      _,--',   _._.--._____
 .--.--';_'-.', ";_      _.,-'
.'--'.  _.'    {`'-;_ .-.>.'
      '-:_      )  / `' '=.
        ) >     {_/,     /~)
        |/               `^ .'


""")
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    # Print the items in the room
    print_room_items(room)
    return

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for something in room_items:
        print("TAKE " + something["id"].upper() + " to take " + something["name"])

    for anotherthing in inv_items:
        print("DROP " + anotherthing["id"].upper() + " to drop your " + anotherthing["id"])

    
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    if chosen_exit in exits:
        return True
    else:
        return False


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    if is_valid_exit(current_room["exits"], direction) == True:
        destination_room = move(current_room["exits"], direction)
        if current_quest >= destination_room["required_current_quest_min"]:
            # Check through all required items - if we're missing one, we can't enter.
            for required_item in destination_room["required_items"]:
                if required_item not in inventory:
                    print("You need to bring something else to enter " + destination_room["name"] + ".")
                    text_to_speech("You're not carrying the right thing to access " + destination_room["name"] + ". Go get it!")
                    return
            current_room = destination_room
            print(current_room["entry_art"])
            # Set current song playing according to room
            set_song(current_room["song"])
            text_to_speech("You're entering " + current_room["name"] + ". " + current_room["description"].replace("\n"," "))
        else:
            print("You need to complete a quest to enter " + destination_room["name"] + ".")
            text_to_speech("Let's not get ahead of ourselves here... You need to complete a quest to access " + destination_room["name"] + ".")
    else:
        print("You cannot go there.")
        text_to_speech("Sorry, but you can't go there.")

def execute_take(item_ref):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints "You cannot take that." 
    Furthermore, it will also enforce a rule such that the player cannot carry more 
    than max_weight_allowed KG in their inventory at any given time. 
    The max_weight_allowed variable can be altered in player.py.
    """

    # Obtain the initial weight being carried, based on whats in inventory.
    global inventory
    weight_carried = 0
    for item in inventory:
        weight_carried = weight_carried + item["mass"]

    # Checking that what the player is already carrying plus what they're about to pick
    # up would not lead to them holding more than the maximum allowed mass, max_weight_allowed.

    if weight_carried + eval("item_" + item_ref)["mass"] <= max_weight_allowed:
        
        # If the item is indeed in the current room, make the move.

        for c in current_room["items"]:
            if item_ref == c["id"]:
                inventory.append(c)
                current_room["items"].remove(c)

                # Add in the additional weight that the player is now carrying.
                weight_carried = weight_carried + eval("item_" + item_ref)["mass"]
                text_to_speech("You've picked up " + eval("item_" + item_ref)["name"] + " ." + eval("item_" + item_ref)["description"])
                return

        # If that item actually is not in the current room, advise player.
        print("You cannot take that.")
        text_to_speech("Sorry, but you can't take that.")



    # If the player is carrying too much, or will be after they pick up their chosen object, advise.
    else:
        print ("You're carrying too much stuff! You've got to drop something...")
        text_to_speech("Sorry; you're not quite strong enough to lift that... You need to drop something.")



def execute_drop(item_ref):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """

    # Obtain the initial weight being carried, based on whats in inventory.

    weight_carried = 0
    for item in inventory:
        weight_carried = weight_carried + item["mass"]

    # If the item is indeed in the inventory, make the drop.

    for i in inventory:
        if item_ref in i["id"]:
            current_room["items"].append(i)
            inventory.remove(i)

            # Take off the additional weight that the player just dropped.

            weight_carried = weight_carried - eval("item_" + item_ref)["mass"]

            # Narrate what just happened
            text_to_speech("You've just dropped " + eval("item_" + item_ref)["name"] + " .")
            
            return

    # If that item actually is not in the inventory, advise player.

    print("You cannot drop that.")



 



    

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]

def text_to_speech(msg):
    """This function takes an argument, msg, and speaks what it says"""
    # Reduce volume of music
    pygame.mixer.music.set_volume(0.33)
    engine = pyttsx3.init()
    engine.setProperty('rate',180)  #180 words per minute
    engine.setProperty('volume',0.9) 
    engine.say(str(msg))
    engine.runAndWait()
    # Return volume of music to default
    pygame.mixer.music.set_volume(1)

def set_song(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()

def quest_completed(quest):
    """ This function will take the quest the player is on, obtain its
    criteria and check to see whether the player has met it. If they have,
    it will return a value to tell main game loop to move to the next quest
    """

    if eval(quest_numbers[quest]["criteria"]):
        print("Well Done! You've completed " + str(quest_numbers[quest]["name"]) + "! \n")
        text_to_speech("Well Done! You've completed " + str(quest_numbers[quest]["name"]) + "!")
        time.sleep(3)
        global current_quest
        current_quest = current_quest + 1
        return True
    else:
        return False

def game_won():
    """ This function simply declares what to do when the player does what
    is necessary to win the game ie current_quest = 6"""

    print (" You Win !!!" * 1000)


# This is the entry point of our program
def main():
    # Before we jump into the main loop, we need to introduce the player.
    opening()

    # Main game loop
    while True:

        global current_quest
        print("Your current quest is:")
        print("\n" + str(quest_numbers[current_quest]["name_art"]) + "\n")
        print(str(quest_numbers[current_quest]["description"]) + "\n")
        print("REMEMBER: You're only strong enough to carry " + str(max_weight_allowed) + " kilograms! \n")
        print("This game is best played in full screen! \n")

        # Display game status (room description, inventory etc.) and narrate the name and description
        print_room(current_room)
        print_inventory_items(inventory)

        # Narration prompt for the user to select a choice
        text_to_speech("What would you like to do next?")

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

        # Check to see if player has done all requisite things to complete current quest
        if quest_completed(current_quest) == True:
            text_to_speech("Now its time for your next quest. It's called... " + str(quest_numbers[current_quest]["name"]) + "... To complete this quest you must... " + str(quest_numbers[current_quest]["description"]) + "... ")

        
        # If there is more to do, just continue with the loop

        # Clearing contents of screen
        print("\n" * 300)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()


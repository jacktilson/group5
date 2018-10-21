#!/usr/bin/python3
# coding=utf-8

import time
import base64
import sys

import anim_bear

# Border characters - TL, T, TR, R, BR, B, BL, L
anim_border = "╔═╗║╝═╚║"
    
def print_animation_frame(frame):
    """This function takes a frame (a list of strings) and prints them in a
    rectangular frame."""

    global anim_border

    # Compute the frame width
    anim_width = 0
    for row in frame:
        if len(row) > anim_width:
            anim_width = len(row)

    # Clear the screen
    frame_text = "\n" * 50
    # Add the top border
    frame_text += anim_border[0] + (anim_border[1] * anim_width) + anim_border[2] + "\n"
    
    # Add each row with side borders
    for row in frame:
        frame_text += anim_border[7]
        frame_text += row
        if len(row) < anim_width:
            frame_text += " " * (anim_width - len(row))
        frame_text += anim_border[3] + "\n"

    # Add the bottom border
    frame_text += anim_border[6] + (anim_border[5] * anim_width) + anim_border[4] + "\n"

    # Print everything at once.
    # Using stdout doesn't add a newline afterwards, preventing jitter.
    sys.stdout.write(frame_text)

def print_animation(anim):
    """This function takes an animation object and prints its frames in a
    rectangular frame at a given frame rate (frames per second)"""

    # Predelay of half a second
    time.sleep(0.5)
    
    # Compute delay time
    rate = anim["rate"]
    if rate < 0.2:
       rate = 0.2
    anim_delay = 1.0/rate

    # Print each frame at the specified rate (approximate)
    for loop_number in range(0,anim["repeat"]):
        for frame_number in anim["order"]:
            print_animation_frame(anim["frames"][frame_number])
            time.sleep(anim_delay)

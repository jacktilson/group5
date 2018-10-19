#!/usr/bin/python3
# coding=utf-8

import time
import base64
import sys

# Border characters - TL, T, TR, R, BR, B, BL, L
anim_border = "╔═╗║╝═╚║"

def decode_row(row, width):
    decoded = base64.decodebytes(row.encode("ascii"))
    print(decoded.decode("ascii"))
    
def print_animation_frame(frame, width, invert):
    """This function takes a frame (a list of strings containing base64 encoded
    brightness values) and prints them in a rectangular frame. Optionally invert
    for light-themed terminals such as IDLE."""

    global anim_border

    # Clear the screen
    frame_text = "\n" * 500
    # Add the top border
    frame_text += anim_border[0] + (anim_border[1] * width) + anim_border[2] + "\n"
    
    # Add each row with side borders
    for row in frame:
        frame_text += anim_border[7]
        frame_text += row
        if len(row) < width:
            frame_text += " " * (width - len(row))
        frame_text += anim_border[3] + "\n"

    # Add the bottom border
    frame_text += anim_border[6] + (anim_border[5] * width) + anim_border[4]

    # Print everything at once
    print(frame_text)

def print_animation(frames, width, rate):
    """This function takes a list of frames (see above) and prints
    them in a rectangular frame at a given frame rate (frames per second)"""
    # Compute delay time
    if rate < 0.2:
       rate = 0.2
    anim_delay = 1.0/rate

    # Print each frame at the specified rate (approximate)
    for frame in frames:
        print_animation_frame(frame, width)
        time.sleep(anim_delay)

testanim = [
	[
		"Hello Hello",
		"lo Hello Hello Hello Hel",
		"Hello Hello Hello Hello ",
		"lo Hello Hello Hello Hel",
		"Hello Hello Hello Hello ",
		"lo Hello Hello Hello Hel"
	],[
		"World World World World ",
		"ld World World World Wor",
		"World World World World ",
		"ld World World World Wor",
		"World World World World ",
		"ld World World World Wor"
	]
]

print_animation(testanim, 24, 2.5)


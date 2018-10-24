#!/usr/bin/python3
# coding=utf-8

import time
import base64
import sys
import anim_bear
import anim_door

# Border characters - TL, T, TR, R, BR, B, BL, L
anim_border = "╔═╗║╝═╚║"
    
def print_animation_frame(frame, border):
    """This function takes a frame (a list of strings) and prints them in a
    rectangular frame."""

    global anim_border

    # Compute the frame width as the maximum width of all the lines
    width = 0
    for row in frame:
        if len(row) > width:
            width = len(row)

    # Clear the screen
    frame_text = "\n" * 300

    # Add the top border
    if border:
        frame_text += " " + anim_border[0] + (anim_border[1] * width) + anim_border[2] + "\n"
    
    # Add each row
    for row in frame:
        # Add a small gap
        frame_text += " "

        # Add left border
        if border:
            frame_text += anim_border[7]

        # Add row, padded to correct width
        frame_text += row
        if len(row) < width:
            frame_text += " " * (width - len(row))

        # Add right border
        if border:
            frame_text += anim_border[3]

        # Add a line break
        frame_text += "\n"

    # Add the bottom border
    if border:
        frame_text += " " + anim_border[6] + (anim_border[5] * width) + anim_border[4] + "\n"

    # Print everything at once.
    # Using stdout doesn't add a newline afterwards, preventing jitter.
    sys.stdout.write(frame_text)

def print_animation(anim, border):
    """This function takes an animation object and prints its frames in a
    rectangular frame at a given frame rate (frames per second)"""

    # Predelay of half a second
    time.sleep(0.5)
    
    # Calculate delay time
    rate = anim["rate"]
    if rate < 0.2:
       rate = 0.2
    delay = 1.0/rate

    # Get how many times to play
    repeat = anim["repeat"]
    if repeat < 1:
        repeat = 1
    
    # Print each frame at the specified rate (approximate)
    for loop_number in range(0, repeat):
        for frame_number in anim["order"]:
            print_animation_frame(anim["frames"][frame_number], border)
            time.sleep(delay)

def print_credits_scroll_left(lines):
    """This function takes a list of strings and prints them to the screen,
    then scrolls them off to the left."""

    # How much extra space to leave on the left of the credits
    margin = 8

    # Compute the width of the whole credits list
    credits_width = 0
    for line in lines:
        if len(line) > credits_width:
            credits_width = len(line)

    # Pad each line to align it centered within the whole credits area
    lines_padded = []
    for line in lines:
        line_offset = (credits_width - len(line)) // 2
        lines_padded.append(" " * line_offset + line)

    # Wait a bit before starting
    time.sleep(1)

    # Add one line at a time, re-printing the entire screen each time
    for frame in range(0, len(lines)+1):
        # Clear screen
        credits_text = "\n" * 300
        
        # Go through the lines by number
        for linenum in range(0, len(lines)):
            if linenum >= frame:
                # Add the line
                credits_text += "\n"
            else:
                # Hide the line
                credits_text += " " * margin + lines_padded[linenum] + "\n"

            # Leave an extra blank line after each printed line
            credits_text += "\n"
            
        # Add some space at the bottom of the screen
        credits_text += "\n\n"
        
        # Print everything at once.
        # Using stdout doesn't add a newline afterwards, preventing jitter.
        sys.stdout.write(credits_text)

        # Wait 0.25 seconds between lines
        time.sleep(0.25)
    
    # Wait 1.5 seconds per line to allow reading time
    time.sleep(len(lines) * 1.5)

    # Scroll off one character at a time
    for frame in range(0, credits_width + margin + 1):
        # Clear screen
        credits_text = "\n" * 300

        # Go through the lines by number
        for linenum in range(0, len(lines)):
            if len(lines_padded[linenum]) + margin - frame <= 0:
                # Line is already off screen, print a blank line
                credits_text += "\n"
            else:
                # Trim characters off the start to scroll left
                credits_text += (" " * margin + lines_padded[linenum])[frame:] + "\n"

            # Leave an extra blank line after each printed line
            credits_text += "\n"

        # Add some space at the bottom of the screen
        credits_text += "\n\n"
        
        # Print everything at once.
        # Using stdout doesn't add a newline afterwards, preventing jitter.
        sys.stdout.write(credits_text)

        # Wait 0.05 seconds between characters scrolled
        time.sleep(0.05)

    # Wait a bit before finishing
    time.sleep(1)

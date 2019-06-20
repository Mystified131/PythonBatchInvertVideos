from moviepy.editor import *
import os
import random

def color_shift(clip):
    """ Returns the color-inversed clip.

    The values of all pixels are replaced with (255-v) or (1-v) for masks 
    Black becomes white, green becomes purple, etc.
    """
    hue = random.randrange(255)

    maxi = (1.0 if clip.ismask else hue)
    return clip.fl_image(lambda f : maxi - f)

directr = "Input"

content = []

for subdir, dirs, files in os.walk(directr):

    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".mp4"):
            bline = str(filepath)
            content.append(bline)

print(content)

ctr = len(content)

for x in range(ctr):

    elem = content[x]

    clip = VideoFileClip(elem)

    new_clip = color_shift(clip)

    outstr = "Output\\" + str(x) + "c" + ".mp4"

    new_clip.write_videofile(outstr)
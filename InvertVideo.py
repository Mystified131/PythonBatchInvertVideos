from moviepy.editor import *
import os

def invert_colors(clip):
    """ Returns the color-inversed clip.

    The values of all pixels are replaced with (255-v) or (1-v) for masks 
    Black becomes white, green becomes purple, etc.
    """
    maxi = (1.0 if clip.ismask else 255)
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

    new_clip = invert_colors(clip)

    outstr = "Output\\" + str(x) + "i" + ".mp4"

    new_clip.write_videofile(outstr)
from moviepy.editor import *
import os
import random

def trim_randomly(clip):

    st = random.randrange(20)
    ln = random.randrange(15)

    new_clip = clip.set_start(t=st).set_end(t=(st + ln))
    
    return new_clip

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

    new_clip = trim_randomly(clip)

    outstr = "Output\\" + str(x) + "t" + ".mp4"

    new_clip.write_videofile(outstr)
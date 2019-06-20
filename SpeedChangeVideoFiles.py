from moviepy.editor import *
import moviepy.audio.fx.all as afx
import os
import random

def random_speed(clip):

    #sp = speed, dr = duration of clip

    rannm = random.randrange(5)

    if rannm < 6:
        vala = random.randrange(2,9)
        sp = vala / 10

    if rannm > 5:
        sp = random.randrange(2, 5)
    
    dr = 41

    new_clip = clip.fl_time(lambda t: sp*t).set_end(dr)
    
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

    new_clip = random_speed(clip)

    outstr = "Output\\" + str(x) + "s" + ".mp4"

    new_clip.write_videofile(outstr)
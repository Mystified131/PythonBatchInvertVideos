from moviepy.editor import *
import os
import random

def trim_randomly(clip):

    totlen = int(clip.duration)
    blen = clip.duration - 4

    newlen = random.randrange(blen)
    newlenb = newlen + 4
    
    st = totlen - newlenb
    ln = newlen

    try:
        new_clip = clip.set_start(t=st).set_end(t=(st + ln))
        return new_clip
    except:
        return clip

directr = "Input"

content = []

for subdir, dirs, files in os.walk(directr):

    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".mp4"):
            bline = str(filepath)
            content.append(bline)

print(content)

elem = content[0]

clip = VideoFileClip(elem)

new_clip = trim_randomly(clip)

outstr = "Output\\" + "t" + ".mp4"

new_clip.write_videofile(outstr)
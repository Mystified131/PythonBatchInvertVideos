from moviepy.editor import *
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import random

def trim_randomly(clip):

    st = random.randrange(20)
    ln = random.randrange(15)

    new_clip = clip.set_start(t=st).set_end(t=(st + ln))
    
    return new_clip

def color_shift(clip):
    """ Returns the color-inversed clip.

    The values of all pixels are replaced with (255-v) or (1-v) for masks 
    Black becomes white, green becomes purple, etc.
    """
    hue = random.randrange(35, 225)

    maxi = (1.0 if clip.ismask else hue)
    return clip.fl_image(lambda f : maxi - f)


def reverse(clip):
    
    # here we set the clip.duration. It must be shorter than the duration of the video or it will throw an error
    clip.duration = 40

    new_clip = clip.fl_time(lambda t: clip.duration - t, keep_duration=True)

    return new_clip

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

def sequence(clip1, clip2, clip3, clip4):
    
    # here we set the clip.duration. It must be shorter than the duration of the video or it will throw an error

    final_clip = concatenate_videoclips([clip1,clip2,clip3, clip4])

    return final_clip

directr = "Input"

content = []

for subdir, dirs, files in os.walk(directr):

    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".mp4"):
            bline = str(filepath)
            content.append(bline)

print(content)

outnum = int(input("How many output files would you like to create?: "))

for mainlp in range(outnum):
    ctr = len(content)
    num1 = random.randrange(ctr)
    vidstr = content[num1]
    clipa = VideoFileClip(vidstr)

    dic1 = random.randrange(10)
    if dic1 < 6:
        clipb = trim_randomly(clipa)
    if dic1 > 5:
        clipb = clipa

    clipc = color_shift(clipb)

    dic3 = random.randrange(10)
    if dic3 < 6:
        clipd = reverse(clipc)
    if dic3 > 5:
        clipd = clipa

    dic4 = random.randrange(10)
    if dic4 < 6:
        clipe = color_shift(clipd)
    if dic4 > 5:
        clipe = clipd

    outstr = "Output\\" + str(mainlp) + "processed" + ".mp4"

    clipe.write_videofile(outstr)

Conc = input("Would you like to randomly concatenate? (y/n): ")

if Conc == "y":

    directr = "Output"

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
        vidnum = random.randrange(ctr)
        file1 = content[vidnum]
        clip1 = VideoFileClip(file1)
        vidnum = random.randrange(ctr)
        file2 = content[vidnum]
        clip2 = VideoFileClip(file2)
        vidnum = random.randrange(ctr)
        file3 = content[vidnum]
        clip3 = VideoFileClip(file3)
        vidnum = random.randrange(ctr)
        file4 = content[vidnum]
        clip4 = VideoFileClip(file4)


        new_clip = sequence(clip1, clip2, clip3, clip4)

        arg = str(ctr)

        outstr = "Output\\" + str(x) + "prosseq" + arg + ".mp4"

        new_clip.write_videofile(outstr)
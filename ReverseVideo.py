from moviepy.editor import *
import os

def reverse(clip):
    
    # here we set the clip.duration. It must be shorter than the duration of the video or it will throw an error
    clip.duration = 40

    new_clip = clip.fl_time(lambda t: clip.duration - t, keep_duration=True)

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

    new_clip = reverse(clip)

    outstr = "Output\\" + str(x) + "r" + ".mp4"

    new_clip.write_videofile(outstr)
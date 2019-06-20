from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import random

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

    outstr = "Output\\" + str(x) + "seq" + arg + ".mp4"

    new_clip.write_videofile(outstr)
from moviepy.editor import VideoFileClip, clips_array
import os

def stack(clip):
    
    # here we set the clip.duration. It must be shorter than the duration of the video or it will throw an error
    final_clip = clips_array([[clip, clip],
                          [clip, clip]])

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

    elem = content[x]

    clip = VideoFileClip(elem)

    new_clip = stack(clip)

    outstr = "Output\\" + str(x) + "4" + ".mp4"

    new_clip.write_videofile(outstr)
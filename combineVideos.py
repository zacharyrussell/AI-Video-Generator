# Import everything needed to edit video clips
from moviepy.editor import *
def combineVideos(videoArray, selectedGenre, artStyle):
    # loading video dsa gfg intro video
    # clip = VideoFileClip("dsa_geek.webm")
    
    # # getting subclip as video is large
    # clip1 = clip.subclip(0, 5)
    
    # # getting subclip as video is large
    # clip2 = clip.subclip(60, 65)
    # concatenating both the clips
    final = concatenate_videoclips(videoArray)
    #writing the video into a file / saving the combined video
    final.write_videofile(f"./final/vid{selectedGenre}-{artStyle}.mp4", 
                     codec='libx264', 
                     audio_codec='aac', 
                     temp_audiofile='temp-audio.m4a', 
                     remove_temp=True
                     )
    
    # showing final clip
    final.ipython_display(width = 480)
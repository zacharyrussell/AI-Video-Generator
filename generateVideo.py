from moviepy.editor import AudioFileClip, ImageClip




# def add_background_audio(videoPath, audioPath):
#     # import moviepy.editor as mpe
#     # import moviepy.audio.fx.all as afx
    
#     my_clip = mpe.VideoFileClip(videoPath)
#     audio_background = mpe.AudioFileClip(audioPath).subclip(0,my_clip.duration)
#     afx.multiply_volume()
#     audio_background
#     final_audio = mpe.CompositeAudioClip([my_clip.audio, audio_background])
#     final_clip = my_clip.set_audio(final_audio)
#     final_clip.write_videofile("combined.mp4", 
#                      codec='libx264', 
#                      audio_codec='aac', 
#                      temp_audiofile='temp-audio.m4a', 
#                      remove_temp=True
#                      )
#     return final_clip

# add_background_audio("/Users/zach/Desktop/chatgpt/final/vidFantasy-3d render.mp4", "/Users/zach/Desktop/chatgpt/background/Full VHS Sound.mp3")

def makeQuiet(audioPath):
    from pydub import AudioSegment
    from pydub.playback import play

    song = AudioSegment.from_mp3(audioPath)

    # boost volume by 6dB
    # louder_song = song + 6
    # reduce volume by 3dB
    quieter_song = song - 3
    #Play song
    # play(quieter_song)

    #save louder song 
    quieter_song.export("newAudio2.mp3", format='mp3')

# makeQuiet("/Users/zach/Desktop/chatgpt/background/Full VHS Sound.mp3")
def add_static_image_to_audio(image_path, audio_path, output_path):
    """Create and save a video file to `output_path` after 
    combining a static image that is located in `image_path` 
    with an audio file in `audio_path`"""
    # create the audio clip object
    audio_clip = AudioFileClip(audio_path)
    # create the image clip object
    image_clip = ImageClip(image_path)
    # use set_audio method from image clip to combine the audio with the image
    video_clip = image_clip.set_audio(audio_clip)

    # specify the duration of the new clip to be the duration of the audio clip
    video_clip.duration = audio_clip.duration
    print(video_clip.duration)
    # set the FPS to 1
    video_clip.fps = 1
    # write the resuling video clip
    video_clip.write_videofile(output_path, 
                     codec='libx264', 
                     audio_codec='aac', 
                     temp_audiofile='temp-audio.m4a', 
                     remove_temp=True
                     )
    return video_clip
    # video_clip.write_videofile(output_path)
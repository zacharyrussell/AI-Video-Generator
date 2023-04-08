from instapy_cli import client
import ssl

from TikTokAutoUploader.TiktokAutoUploader.TiktokBot import TiktokBot, Upload


youtubeAPIKey = "AIzaSyBXMfr3wkIG66SdIhNY4NKySa6aPpOd0QE"
ssl._create_default_https_context = ssl._create_unverified_context


username = 'ai.powered.dreams'
password = 'password'

import os
if os.path.isfile("./config/ai.powered.dreams_uuid_and_cookie.json"):
    os.remove("./config/ai.powered.dreams_uuid_and_cookie.json")

from instabot import Bot
from datetime import datetime

def instaUpload(videoPath, title):
    video = videoPath
    text = title + '\r\n' + '#dalle2 #chatgpt #openai #aipowereddreams'
    import instabot
    bot = Bot()
    
    bot.login(username = username,
            password = password)
    
    bot.upload_video(videoPath,
                 caption =text)



def youtubeUpload(path, title):
    cmd = f'''python3 youtube_upload.py --file="{path}" --title="{title}" --description="100% AI Generated using chatGPT and Dalle2 \n Join our discord:\t https://discord.gg/5X3ts3rM" --keywords="dalle2, chatGPT, openAI, automation, ai, dalle, aipowereddreams" --category="22" --privacyStatus="public"'''
    os.system(cmd)


def tikTokUpload(path, title):
    # Example Usage

    tiktok_bot = TiktokBot()

    # Use a video from your directory.

    # tiktok_bot.upload.uploadVideo(path, "a", 1, 45)

    # Or use youtube url as video source. [Simpsons Meme 1:16 - 1:32 Example]
    tiktok_bot.upload.directUpload(path, title)

    # tiktok_bot.upload.uploadVideo("https://www.youtube.com/watch?v=OGEouryaQ3g", "TextOverlay", startTime=76, endTime=92, private=False)

def uploadAll(path, title):
    youtubeUpload(path, title)
    instaUpload(path, title)
    tikTokUpload(path, title)
        
# path = "./final/vidDrama-Watercolour painting.mp4"
# tikTokUpload(path, "The Canyon")
# youtubeUpload(path, "The Canyon")
path = "/Users/zach/Desktop/chatgpt/final/vidDrama-Watercolour painting.mp4"
# instaUpload(path, "The Canyon")

tikTokUpload(path, "The Canyon")

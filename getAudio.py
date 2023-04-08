from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os


# def test(name):
#     import pyttsx3
#     engine = pyttsx3.init()
#     engine.say("I will speak this text")
#     engine.runAndWait()

# test("testing")

def getWhiteNoise():
    from scipy.io import wavfile
    from scipy import stats
    import numpy as np

    sample_rate = 44100
    length_in_seconds = 3
    amplitude = 11
    noise = stats.truncnorm(-1, 1, scale=min(2**16, 2**amplitude)).rvs(sample_rate * length_in_seconds)
    wavfile.write('noise.wav', sample_rate, noise.astype(np.int16))

def getTone():
    from pysinewave import SineWave
    import time

    sinewave = SineWave(pitch = -30)
    sinewave.play()
    time.sleep(1)
    sinewave.stop()

apikey = "0a38e2fb974e44d6a89052fb3d170a51"


def getVoice(text, name):
    import requests

    url = "https://voicerss-text-to-speech.p.rapidapi.com/"

    querystring = {"key":apikey}

    payload = "src=Hello%2C%20world!&hl=en-us&r=0&c=mp3&f=8khz_8bit_mono"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": apikey,
        "X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)


# getVoice("a", "a")
# getTone()
# getWhiteNoise()
def getAudio(text, name):
    # The text that you want to convert to audio
    
    # Language in which you want to convert
    language = 'en'
    
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=text, lang=language, slow=False)
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save(f"./audio/{name}.mp3")
    return f"./audio/{name}.mp3"

# getAudio("Hello this is a test", "testAudio")


URL = "https://chat.openai.com/chat"

import random
import os
from time import sleep
import openai
import json
from getAudio import getAudio
from getImage import getImage
from getText import getText
from generateVideo import add_static_image_to_audio
from combineVideos import combineVideos


# Load your API key from an environment variable or secret management service
tokens = 1000


artStyles = ["Photorealism", "Digital art", "3d render", "Postmodernist art", "Abstract art", "Oil painting", "Stained glass", "Acrylic Painting", "Surrealist art", "Minimalist art", "Dadaist art", "Gothic art", "Cubist art", "Expressionist art", "Mannerist", "Rococo art", "Trailcam footage", "Horror", "Macabre art", "Watercolour painting", "Crayon drawing", "Kids drawing", "Spray Paint", "Pop art", "Comic book", "Rough sketch", "Blueprint", "VHS tape", "Light painting", "Sumi Painting", "Anime", "Ice sculpture", "Film photography", "Pixel art"]


artStyle = artStyles[random.randint(0, len(artStyles)-1)]
genres = ["Romance", "Mystery", "Fantasy", "Science-Fiction", "Horror", "Historical-Fiction", "Thriller", "Comedy", "Crime", "Drama", "Space-travel"]


selectedGenre = genres[random.randint(0, len(genres)-1)]

selectedGenre = "Drama"
artStyle = "Watercolour painting"

metaPrompt = f"generate a {selectedGenre} story prompt"

numPeople = random.randint(1,3)
numPlaces = random.randint(1,2)
people = getText(f"Generate {numPeople} names", 100)
places = getText(f"Generate {numPlaces} place", 100)
actions = getText("Generate 3 verbs", 100)

generatedPrompt = f"write a {selectedGenre} story about: {people}, {places}, {actions}"
title = getText(f"Generate a short title for a story about: {people}, {places}, {actions}", tokens)
rand = random.randint(0,11)
rand = 6
if(rand % 4 == 0):
    generatedPrompt += " with a tragic ending"
elif(rand % 4 == 1):
    generatedPrompt += " with a bad ending but then it turns good"
elif(rand % 4 == 2):
    generatedPrompt += " with a good ending but then it turns into a bad ending"


if(selectedGenre == 'Comedy'):
    generatedPrompt += " with lots of funny jokes"
# get our story text 
textResponse = getText(f"write a {selectedGenre} story about: " + generatedPrompt, tokens)

import nltk

sentences = nltk.tokenize.sent_tokenize(textResponse)
# print("TITLE:   " + title)
# print(metaPrompt)
# print(generatedPrompt)
# print(textResponse)
# print(sentences)
# print(selectedGenre)
# print(artStyle)

# sleep(10)
# textResponse = sentences[0]

count = 1
videoArray = []


for s in sentences:
    sentence = s
    print(sentence)
    audioPath = getAudio(sentence, f"audio{count}")
    imagePath = None
    # imagePath = getImage(sentence + " " + artStyle, f"frame{count}")
    while imagePath == None:
        try:
            imagePath = getImage(sentence + " " + artStyle, f"frame{count}")
        except:
            fixedSentence = getText(f"Make the sentence {sentence} safe for work", tokens)
            sentence = fixedSentence
            print("FAILED, trying new sentence")
            # imagePath = getImage(fixedSentence + artStyle, f"frame{count}")
    video_clip = add_static_image_to_audio(imagePath, audioPath, f"./videos/sent{count}.mp4")
    count += 1
    videoArray.append(video_clip)
    

combineVideos(videoArray, selectedGenre, artStyle)








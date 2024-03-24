from gtts import gTTS
from playsound import playsound
import string
import random
import os



def randomFileName(numberRange):
  return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(numberRange))  + '.mp3'

def cria_audio(audio):
 tts = gTTS(audio,lang='pt-br')
 fileName = randomFileName(6)
 tts.save('audios/' + fileName)
 playsound('audios/' + fileName)

def removeAudios():
  origfolder = "audios/"
  audioFiles = os.listdir(origfolder)
  for item in audioFiles:
   if item.endswith(".mp3"):
    os.remove(os.path.join(origfolder, item))


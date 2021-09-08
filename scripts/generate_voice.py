#otras opciones: https://pythonprogramminglanguage.com/text-to-speech/
from gtts import gTTS
import os

if __name__ == '__main__':
    language = 'es'

    mytext = 'Que tenga un buen día.'
  

    myobj = gTTS(text=mytext, lang=language, slow=False)

    myobj.save("tenga_buen_dia.mp3")

    os.system("mpg321 tenga_buen_dia.mp3")
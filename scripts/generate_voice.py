'''
    This code was used to convert text to speech. Audios of robot's
    artificial voice were generated with this code.

    Carlos Mario Bielma Avendano        A01730645  
    Nashely Martinez Chan               A01329786
    Jonatan Emanuel Salinas Avila       A01731815
    Ximena Aaroni Salinas Molar         A01551723
    Martin Octavio Garcia Garcia        A01328971

    Courses:
        Robotics Project
        Embedded Systems laboratory
    
    November, 2021
'''
#otras opciones: https://pythonprogramminglanguage.com/text-to-speech/
from gtts import gTTS
import os

if __name__ == '__main__':
    language = 'es'

    mytext = 'Que tenga un buen día.'
  
    myobj = gTTS(text=mytext, lang=language, slow=False)

    myobj.save("tenga_buen_dia.mp3")

    os.system("mpg321 tenga_buen_dia.mp3")
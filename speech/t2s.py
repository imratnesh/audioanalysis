# -*- coding: utf-8 -*-
from ibm_watson import TextToSpeechV1
import datetime as dt
import os
text_to_speech = TextToSpeechV1(
    iam_apikey='f5pBxf4Nr78rNYajvkCe8oIqgh_MnyIWgWzXMtqSAyZJ',
    url='https://gateway-lon.watsonplatform.net/text-to-speech/api'
)

#with open('hello_world.wav', 'wb') as audio_file:
#    audio_file.write(
#        text_to_speech.synthesize(
#            'Hello, I am Ratnesh',
#            voice='en-US_AllisonVoice',
#            accept='audio/wav'        
#        ).get_result().content)

def convertText(text, filename):
    try:
#        os.remove("../static/result.wav")
#        open(f'../static/result3.wav','w+')
        with open(f'./static/{filename}', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    text,
                    voice='en-US_AllisonVoice',
                    accept='audio/wav'        
                ).get_result().content)
    except Exception as e:
        print(e.with_traceback)
        return False
    return True

#print(convertText("I am Sumeet I live in sehore"))

from ibm_watson import SpeechToTextV1
from os.path import join, dirname
import json
from ibm_watson.websocket import RecognizeCallback, AudioSource

speech_to_text = SpeechToTextV1(
    iam_apikey='GFT9-N0g7zSU9FIM1YLNL7ZyzLdIJ1s_EkluUjYK8B1s',
    url='https://gateway-lon.watsonplatform.net/speech-to-text/api'
)

#with open(join(dirname(__file__), './.', 'audio1.wav'),
#               'rb') as audio_file:
#    speech_to_text.add_audio(
#        '{customization_id}',
#        'audio1',
#        audio_file,
#        content_type='audio/wav'
#    )
# Poll for audio status.

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        print(json.dumps(data['results'][0]['alternatives'][0]['transcript'], indent=2))

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

myRecognizeCallback = MyRecognizeCallback()

with open(join(dirname(__file__), 'audio-file.flac'), 'rb') as audio_file:
    audio_source = AudioSource(audio_file)
    speech_to_text.recognize_using_websocket(
        audio=audio_source,
        content_type='audio/flac',
        recognize_callback=myRecognizeCallback,
        model='en-US_BroadbandModel',
        keywords=['colorado', 'tornado', 'tornadoes'],
        keywords_threshold=0.5,
        max_alternatives=3)
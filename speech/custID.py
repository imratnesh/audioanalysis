# -*- coding: utf-8 -*-

from ibm_watson import SpeechToTextV1
import json

speech_to_text = SpeechToTextV1(
    iam_apikey='GFT9-N0g7zSU9FIM1YLNL7ZyzLdIJ1s_EkluUjYK8B1s',
    url='https://gateway-lon.watsonplatform.net/speech-to-text/api'
)

#language_model = speech_to_text.create_language_model(
#    'First example language model',
#    'en-US_BroadbandModel',
#    description='First custom language model example'
#).get_result()
#print(json.dumps(language_model, indent=2))

speech_model = speech_to_text.get_model('en-US_BroadbandModel').get_result()

print(json.dumps(speech_model, indent=2))
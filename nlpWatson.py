# -*- coding: utf-8 -*-

import json
from ibm_watson import NaturalLanguageUnderstandingV1, NaturalLanguageClassifierV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, EntitiesOptions,  EmotionOptions


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='be_bMNgvPhFVa7K2oE6FdBRBRVPPhEkPzBOjMzwOPX7U',
    url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api'
)


def n(site='www.wsj.com/news/markets'):
    response = natural_language_understanding.analyze(
        url=site,
        features=Features(sentiment=SentimentOptions(targets=['stocks']))).get_result()
    return response
#print(json.dumps(response, indent=2))
#
#response = natural_language_understanding.analyze(
#    html="<html><head><title>Emporphis</title></head><body><h1>IoT a Revolution for Retail Stores</h1><p>Internet of Things (IoT) is driving revolution and new opportunities by bringing every consumer, object, and activity into the digital realm. At the same time, leading businesses are making many changes within their organisations and enterprises by digitizing their employees, services, process, and product.</p></body></html>",
#    features=Features(emotion=EmotionOptions(targets=['iot','organisations']))).get_result()
#
#print(json.dumps(response, indent=2))


response = natural_language_understanding.analyze(
    url='www.impetus.com',
    features=Features(entities=EntitiesOptions(sentiment=True,limit=1))).get_result()


def nlpResponse(sitename):
    try:
        response = natural_language_understanding.analyze(
                url=sitename,
                features=Features(entities=EntitiesOptions(sentiment=True,limit=1))).get_result()
        return response['entities']
    except:
        return f"Something went wrong. Please try with https:// or http://"
    
#import datetime as dt
#print(dt.datetime.now())
#print(n("www.yahoo.in"))

#print(nlpResponse("www.impetus.com"))
#print(json.dumps(response, indent=2))

#{
#  "usage": {
#    "text_units": 1,
#    "text_characters": 754,
#    "features": 1
#  },
#  "retrieved_url": "http://www.impetus.com/",
#  "language": "en",
#  "entities": [
#    {
#      "type": "Company",
#      "text": "Teradata",
#      "sentiment": {
#        "score": 0.219044,
#        "label": "positive"
#      },
#      "relevance": 0.95883,
#      "disambiguation": {
#        "subtype": [],
#        "name": "Teradata",
#        "dbpedia_resource": "http://dbpedia.org/resource/Teradata"
#      },
#      "count": 3
#    }
#  ]
#}

#{
#  "usage": {
#    "text_units": 1,
#    "text_characters": 1361,
#    "features": 1
#  },
#  "retrieved_url": "https://www.emorphis.com/",
#  "language": "en",
#  "entities": [
#    {
#      "type": "JobTitle",
#      "text": "Services Product Development",
#      "sentiment": {
#        "score": 0.0,
#        "label": "neutral"
#      },"I am Sumeet I live in sehore"
#      "relevance": 0.973519,
#      "count": 4
#    }
#  ]
#}


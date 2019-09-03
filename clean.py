# -*- coding: utf-8 -*-
import re
from nltk.corpus import stopwords
sentence = []
#
#l = '/home/ubuntu/nltk_data/corpora/stopwords/english'
#a = []
#with open(l,'r') as f:
#    a.append(f.read())
#k = a[0].split('\n')
#print(True if 'are' in k else '')

stpwrds = stopwords.words("english")
def getSentence():
    with open('file.txt', 'r') as file:
        for s in file.readlines():
            
            s = re.sub("[@\"#!$?\-,.]",'', s)
            s = re.sub("[\d]",'', s)
            
            s = ' '.join([w for w in s.lower().split() if w not in stpwrds])  
            
#            print(s.split())
            sentence.append(s.split())
    return sentence

getSentence()
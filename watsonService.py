# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, render_template
from nlpWatson import nlpResponse
from speech.t2s import convertText
import json
import datetime as dt
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def wavio():
    result = nlpResponse(request.args.get('sitename'))
    print(result[0])
    return render_template("index.html", result=json.dumps(result))

@app.route('/s2t', methods=['GET', 'POST'])
def s2t():
    filepath = ''
    saveAudio('d')
    text = analyze(filepath)
    return render_template("s2t.html", result=text)

@app.route('/t2s', methods=['GET', 'POST'])
def t2s():
    result = ''
    filename = 'result'+str(dt.datetime.now())+'.wav' 
    if request.method == 'POST':
        text = request.form['text']
        print('text = ', text, 'writing file', filename)
        res = convertText(str(text), filename)
        if res:
            result = 'Play audio file to listen text'
        else:
            result = 'Try again. Something goes wrong'
            
    return render_template("t2s.html", result = result, filename=filename)

if __name__ == "__main__":
    app.run()
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishtofrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    print("{} is in French".format(textToTranslate))
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenctoenglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    print("{} is in English".format(textToTranslate))
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

from PIL import Image
from flask import Flask, send_file, jsonify, request
from flask_cors import CORS
from app.templates.drawTemplateFunctions import drawTemplateFunctions
from app.templatesList import templatesList
import io

app = Flask(__name__)
CORS(app)

#GET TEMPLATES
@app.route('/templates')
def index():
    return jsonify(templates = templatesList)

#GENERATE MEME
@app.route('/generate', methods=['POST'])
def generate():
    try:
        requestBody = request.json
        fileName = ""
        if requestBody['template'] == "templateOne":
            fileName = drawTemplateFunctions['templateOne'](requestBody['firstText'], requestBody['secondText'])
        elif requestBody['template'] == "templateTwo":
            fileName = drawTemplateFunctions['templateTwo'](requestBody['firstWord'], requestBody['secondWord'])
        elif requestBody['template'] == "templateThree":
            fileName = drawTemplateFunctions['templateThree'](requestBody['firstText'], requestBody['secondText'], requestBody['thirdText'])
        elif requestBody['template'] == "templateFour":
            fileName = drawTemplateFunctions['templateFour'](requestBody['firstText'], requestBody['secondText'], requestBody['thirdText'])
        elif requestBody['template'] == "templateFive":
            fileName = drawTemplateFunctions['templateFive'](requestBody['firstText'], requestBody['secondText'])
        else:
            raise Exception("Please add a valid template name")
        return jsonify(status = True, fileName = fileName)
    except:
        return jsonify(status = False, msg = "Error occurred, please make sure every required field is included")

#GET TEMPLATE
@app.route('/images/assets/<string:name>')
def getAsset(name):
    try:
        img = Image.open('assets/' + name)
        file_object = io.BytesIO()
        img.save(file_object, 'PNG')
        file_object.seek(0)
        return send_file(file_object, mimetype='image/PNG')
    except:
        return jsonify(status = False, msg = "Error occurred, please make sure your template name is correct")

#GET MEME
@app.route('/images/memes/<string:name>')
def getMeme(name):
    try:
        img = Image.open('temp/' + name)
        file_object = io.BytesIO()
        img.save(file_object, 'PNG')
        file_object.seek(0)
        return send_file(file_object, mimetype='image/PNG')
    except:
        return jsonify(status = False, msg = "Error occurred, please make sure your meme id is correct")

#GET MEME EXAMPLE
@app.route('/images/example/<string:name>')
def getExample(name):
    try:
        img = Image.open('examples/' + name)
        file_object = io.BytesIO()
        img.save(file_object, 'PNG')
        file_object.seek(0)
        return send_file(file_object, mimetype='image/PNG')
    except:
        return jsonify(status = False, msg = "Error occurred, please make sure your example name is correct")
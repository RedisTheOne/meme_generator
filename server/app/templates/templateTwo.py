# {
#    "template": "templateTwo" ,
#    "firstWord": "SAMPLE",
#    "secondWord": "SAMPLE"
# }

from PIL import Image, ImageDraw, ImageFont
import uuid
from app.templates.inc import checkIfTempFolderExists

def drawTemplateTwo(firstWord, secondWord):
    #CHECK IF TEMPLATE FOLDER IS CREATED
    checkIfTempFolderExists()
    
    #LOAD THE IMAGE, AND GET THE DIMENSIONS
    img = Image.open('assets/template2.jpg')
    imgWidth, imgHeight = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font_family.ttf", 30)

    #DRAW THE FIRST WORD
    firstWordWidth, _ = draw.textsize(firstWord, font=font)
    draw.text((((imgWidth + 20) / 4) - (firstWordWidth / 2), 120), firstWord, fill="black", font=font)

    #DRAW THE SECOND WORD
    secondWordWidth, _ = draw.textsize(secondWord, font=font)
    draw.text((((imgWidth / 2) + 53) - (secondWordWidth / 2), 78), secondWord, fill="black", font=font)

    #SAVE THE IMAGE
    randomName = str(uuid.uuid4())
    img.save(f"temp/{randomName}.png", "PNG")
    return randomName + ".png"
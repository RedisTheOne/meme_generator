# {
#    "template": "templateOne" ,
#    "firstText": "Sample Text",
#    "secondText": "Sample Text"
# }

from PIL import Image, ImageDraw, ImageFont
import uuid
from app.templates.inc import checkIfTempFolderExists

def drawTemplateOne(firstText, secondText):
    #CHECK IF TEMPLATE FOLDER IS CREATED
    checkIfTempFolderExists()

    #LOAD THE IMAGE, AND GET THE DIMENSIONS
    img = Image.open('assets/template1.png')
    imgWidth, imgHeight = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font_family.ttf", 40)
    
    #DRAW THE FIRST TEXT
    firstTextWidth, firstTextHeight = draw.textsize(firstText, font=font)
    isValid = firstTextWidth < imgWidth / 2
    index = 2
    while isValid == False:
        splitedFirstText = firstText.split()
        middle = len(splitedFirstText) // index
        secondIndex = 0
        firstText = ""
        for piece in splitedFirstText:
            if middle == secondIndex:
                firstText += piece + '\n'
                secondIndex = 0
            else:
                firstText += piece + ' '   
                secondIndex += 1 
        index += 1  
        firstTextWidth, firstTextHeight = draw.textsize(firstText, font=font)
        isValid = firstTextWidth < imgWidth / 2
    draw.text(((imgWidth / 2), ((imgHeight / 4)) - (firstTextHeight / 2)), firstText, fill="black", font=font)

    #DRAW THE SECOND TEXT
    secondTextWidth, secondTextHeight = draw.textsize(secondText, font=font)
    isValid = secondTextWidth < imgWidth / 2
    index = 2
    while isValid == False:
        splitedSecondText = secondText.split()
        middle = len(splitedSecondText) // index
        secondIndex = 0
        secondText = ""
        for piece in splitedSecondText:
            if middle == secondIndex:
                secondText += piece + '\n'
                secondIndex = 0
            else:
                secondText += piece + ' '   
                secondIndex += 1 
        index += 1  
        secondTextWidth, secondTextHeight = draw.textsize(secondText, font=font)
        isValid = secondTextWidth < imgWidth / 2
    draw.text(((imgWidth / 2), ((imgHeight / 1.35)) - (secondTextHeight / 2)), secondText, fill="black", font=font)

    #SAVE THE IMAGE
    randomName = str(uuid.uuid4())
    img.save(f"temp/{randomName}.png", "PNG")
    return randomName + ".png"
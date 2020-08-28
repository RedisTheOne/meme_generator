# {
#    "template": "templateThree" ,
#    "firstText": "Sample Text",
#    "secondText": "Sample Text",
#    "thirdText": "SamplteText"
# }

from PIL import Image, ImageDraw, ImageFont
import uuid
from app.templates.inc import checkIfTempFolderExists

def drawTemplateThree(firstText, secondText, thirdText):
    #CHECK IF TEMPLATE FOLDER IS CREATED
    checkIfTempFolderExists()

    #LOAD THE IMAGE, AND GET THE DIMENSIONS
    img = Image.open('assets/template3.jpg')
    imgWidth, imgHeight = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font_family.ttf", 40)
    
    #DRAW THE FIRST TEXT
    firstTextWidth, firstTextHeight = draw.textsize(firstText, font=font)
    isValid = firstTextWidth < (imgWidth / 2 - 40)
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
        isValid = firstTextWidth < (imgWidth / 2 - 40)
    draw.text(((imgWidth / 2 + 20), ((imgHeight / 6)) - (firstTextHeight / 2)), firstText, fill="black", font=font)

    #DRAW THE SECOND TEXT
    secondTextWidth, secondTextHeight = draw.textsize(secondText, font=font)
    isValid = secondTextWidth < (imgWidth / 2 - 40)
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
        isValid = secondTextWidth < (imgWidth / 2 - 40)
    draw.text(((imgWidth / 2 + 20), ((imgHeight / 2)) - (secondTextHeight / 2)), secondText, fill="black", font=font)

    #DRAW THE THIRD TEXT
    thirdTextWidth, thirdTextHeight = draw.textsize(thirdText, font=font)
    isValid = thirdTextWidth < (imgWidth / 2 - 40)
    index = 2
    while isValid == False:
        splitedThirdText = thirdText.split()
        middle = len(splitedThirdText) // index
        secondIndex = 0
        thirdText = ""
        for piece in splitedThirdText:
            if middle == secondIndex:
                thirdText += piece + '\n'
                secondIndex = 0
            else:
                thirdText += piece + ' '   
                secondIndex += 1 
        index += 1  
        thirdTextWidth, thirdTextHeight = draw.textsize(thirdText, font=font)
        isValid = thirdTextWidth < (imgWidth / 2 - 40)
    draw.text(((imgWidth / 2 + 20), ((imgHeight / 1.2)) - (thirdTextHeight / 2)), thirdText, fill="black", font=font)

    #SAVE THE IMAGE
    randomName = str(uuid.uuid4())
    img.save(f"temp/{randomName}.png", "PNG")
    return randomName + ".png"
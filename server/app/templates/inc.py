import os

destinationFolder = "./temp"

def checkIfTempFolderExists():
    if os.path.exists(destinationFolder) == False:
        os.makedirs(destinationFolder)
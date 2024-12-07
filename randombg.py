#!/usr/bin/python3

import os
import re
import random
import fileinput

# Configure these:
IMAGES_DIRECTORY_PATH: str = "/home/ethan/backgrounds"
HYPRPAPER_PATH: str = "/home/ethan/.config/hypr/hyprpaper.conf"
VALID_FILE_FORMATS = ["png", "jpeg", "gif", "webp", "jpg"]

# takes in a list of file names
# returns one with the valid file formats
def filterImages(files: [str]) -> [str]:
    breakAtDot = lambda file: file.split(".")
    extentionSeperatedFiles: [[str]] = map(breakAtDot, files)
    
    getLastExtention = lambda extentionSeperatedFile: extentionSeperatedFile[-1]
    fileExtentions: [str] = map(getLastExtention, extentionSeperatedFiles)

    isImg = lambda fileExtention: fileExtention in VALID_FILE_FORMATS
    areImages: [bool] = list(map(isImg, fileExtentions))
    
    validFiles: [str] = []
    for i in range(len(files)):
        if areImages[i]:
            validFiles.append(files[i])

    return validFiles

# takes in a str with the path
# returns a str the absolute path of a random 
# image in the directory 
def getRandomBackground(directory: str) -> str:
    dirListing: [str] = os.listdir(directory)
    validBackgrounds: [str] = filterImages(dirListing)
    chosenPicture: int = random.choice(validBackgrounds)
    absolutePathOfChosenPicture = IMAGES_DIRECTORY_PATH + "/" + chosenPicture
    return absolutePathOfChosenPicture

def setConfig(backgroundImagePath: str):
    preload: str = "preload = " + backgroundImagePath
    wallpaper: str = "wallpaper = monitor, " + backgroundImagePath
    newConfig: str = "\n".join([preload, wallpaper])
    
    with open(HYPRPAPER_PATH, "w") as hyperpaperConfig:
        hyperpaperConfig.write(newConfig)

setConfig(getRandomBackground(IMAGES_DIRECTORY_PATH))



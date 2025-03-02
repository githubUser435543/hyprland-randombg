#!/usr/bin/python3

from collections.abc import Callable
import os
import random

# Configure these:
IMAGES_DIRECTORY_PATH: str = "/home/ethan/backgrounds"
HYPRPAPER_PATH: str = "/home/ethan/.config/hypr/hyprpaper.conf"
VALID_FILE_FORMATS = ["png", "jpeg", "gif", "webp", "jpg"]

# takes in a list of file names
# returns one with the valid file formats
def filterImages(files: list[str]) -> list[str]:
    breakAtDot = lambda file: file.split(".")
    extentionSeperatedFiles: map[Callable] = map(breakAtDot, files)
    
    getLastExtention = lambda extentionSeperatedFile: extentionSeperatedFile[-1]
    fileExtentions: map[str] = map(getLastExtention, extentionSeperatedFiles)

    isImg = lambda fileExtention: fileExtention in VALID_FILE_FORMATS
    areImages: list[bool] = list(map(isImg, fileExtentions))
    
    validFiles: list[str] = []
    for i in range(len(files)):
        if areImages[i]:
            validFiles.append(files[i])

    return validFiles

# takes in a str with the path
# returns a str the absolute path of a random 
# image in the directory 
def getRandomBackground(directory: str) -> str:
    dirListing: list[str] = os.listdir(directory)
    validBackgrounds: list[str] = filterImages(dirListing)
    chosenPicture: str = random.choice(validBackgrounds)
    absolutePathOfChosenPicture: str = IMAGES_DIRECTORY_PATH + "/" + chosenPicture
    return absolutePathOfChosenPicture

def setConfig(backgroundImagePath: str):
    preload: str = "preload = " + backgroundImagePath
    wallpaper: str = "wallpaper = monitor, " + backgroundImagePath
    newConfig: str = "\n".join([preload, wallpaper])
    print(newConfig)
    #with open(HYPRPAPER_PATH, "w") as hyperpaperConfig:
    #    hyperpaperConfig.write(newConfig)

setConfig(getRandomBackground(IMAGES_DIRECTORY_PATH))



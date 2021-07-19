import termcolor
import colorama
import os
import platform
from PIL import Image
from sys import argv

colorama.init() # windows compatibility for cprint

# code functions
def addToCurrentCell():
    global register, cellPointer
    register[cellPointer] += 1

def subFromCurrentCell():
    global register, cellPointer
    register[cellPointer] -= 1

def goToNextCell():
    global register, cellPointer
    try:
        cellPointer += 1
        register[cellPointer]
    except:
        register.append(0)

def goToPreviousCell():
    global register, cellPointer
    if cellPointer == 0: return
    cellPointer -= 1

def startLoop():
    global char, cellPointer, loopStart, inLoop
    inLoop = True
    loopStart = char

def endLoop():
    global register, cellPointer, loopStart, inLoop, line, char
    if inLoop:
        if register[cellPointer] == 0:
            inLoop = False
            char += 1
            return
        else:
            char = loopStart
            return
        

def printCurrentCell():
    global register, cellPointer
    print(chr(register[cellPointer]), end='')

def inputIntoCurrentCell():
    global register, cellPointer
    thing = input()
    if type(thing) == int:
        register[cellPointer] = thing
    elif type(thing) == str:
        register[cellPointer] = ord(thing[0])

# brainfuck vars
register = [0]
cellPointer = 0
loopStart = 0
inLoop = False

# brainloller vars
running = True

# other vars
line = 0
char = 0

if len(argv) == 1 or not argv[1] in ["lol", "run"]:
    termcolor.cprint("Please provide a valid mode! Usage: bfpy (run|lol) (file)", 'red')
elif argv[1] == "run":
    # open and read file
    file = open(argv[2], 'r')
    code = file.readlines()

    # loop through code
    for line in code:
        while char < len(line):
            # run code
            if line[char] == "+":
                addToCurrentCell()
            elif line[char] == "-":
                subFromCurrentCell()
            elif line[char] == ">":
                goToNextCell()
            elif line[char] == "<":
                goToPreviousCell()
            elif line[char] == "[":
                startLoop()
            elif line[char] == "]":
                endLoop()
            elif line[char] == ".":
                printCurrentCell()
            elif line[char] == ",":
                inputIntoCurrentCell()
            char += 1
elif argv[1] == "lol":
    img = Image.open(argv[2])
    pix = img.load()
    width, height = img.size
    x = 0
    y = 0
    
    while running:
        rgb = (pix[x, y][0], pix[x, y][1], pix[x, y][2])

        if rgb == (0,255,0):
            addToCurrentCell()
        elif rgb == (0,128,0):
            subFromCurrentCell()
        elif rgb == (255,0,0):
            goToNextCell()
        elif rgb == (128,0,0):
            goToPreviousCell()
        elif rgb == (255,255,0):
            pass # todo
        elif rgb == (128,128,0):
            pass # todo
        elif rgb == (0,0,255):
            printCurrentCell()
        elif rgb == (0,0,128):
            inputIntoCurrentCell()
        elif rgb == (0,255,255):
            pass # todo
        elif rgb == (0,128,128):
            pass # todo

        x += 1
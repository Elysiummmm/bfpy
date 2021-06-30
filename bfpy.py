import termcolor
import colorama
import os
import platform
from sys import argv

colorama.init() # windows compatibility for cprint

# helper functions
def throwError(error):
    termcolor.cprint("Error: " + error, 'red')
    exit(1)

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
    if cellPointer == 0: throwError("tried to move past first cell")
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

# other vars
line = 0
char = 0

if len(argv) == 1 or not argv[1] in ["build", "run"]:
    termcolor.cprint("Please provide a valid mode! Usage: bfpy (run|build) (file)", 'red')
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
import os 
from time import sleep
from multiprocessing import Process
from pynput.keyboard import Key, Controller

def getListOfFiles(directoryPath):
    command = "ls -1 {}".format(directoryPath)
    listOfFiles = os.popen(command).read().split("\n")
    if(listOfFiles[ len(listOfFiles)  - 1] == "" ):
	    del listOfFiles[len(listOfFiles) - 1]  
    for i in range(len(listOfFiles)):
        if(listOfFiles[i] == "pic"): 
            del listOfFiles[i]
    return listOfFiles

def printInformationAboutFilesToConvert(listOfFiles):
    print("Files to convert:")
    for file in listOfFiles:
	    print("-> {}".format(file))	
    print("Amount of file {}".format(len(listOfFiles)))

def runFlashApp(fileToOpen):
    command = "flashplayer {} 2> /dev/null".format(fileToOpen)
    
    def FlashApp():
        os.system(command)
        
    process = Process(target=FlashApp)
    process.start()
    sleep(0.5)
    process.kill()

def makeFlashAppFullScreen():
    # press clt + f to fullscreen
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press('f')
    # print('pressed')
    keyboard.release(Key.ctrl)
    sleep(0.25)
    keyboard.release('f')

def closeFlashApp():
    os.system("killall flashplayer")

def mkDirForScreenshots(folder):
    os.system("mkdir -p {}pic".format(folder))

def takeScreenshot(fileToSaveSceenshot):
    os.system("gnome-screenshot -w -f {} 2> /dev/null "
        .format(fileToSaveSceenshot))

def chengeFileFromSwfToPng(file):
    newFile = file.split(".")
    out = ""
    if(newFile[len(newFile) -1 ] == "swf"):
        newFile[len(newFile) -1 ] = "png"
        file = ""
        count = 0
        for string in newFile:
            if( len(newFile)-1 != count):
                file += string + "."
            else:
                file += string
            count += 1
        out = file
    return out
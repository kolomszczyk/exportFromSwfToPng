import os
import subprocess
from multiprocessing import Process
from time import sleep
import swfTools

# Start 

# root directory is directory 
# that hold all swf files 
rootDir = "/home/nefex/exportswf/swfFiles/"
swfTools.mkDirForScreenshots(rootDir)

# get list of apps 	
listOfFiles = swfTools.getListOfFiles(rootDir)

swfTools.printInformationAboutFilesToConvert(listOfFiles)

# for every file 
# 	open flashplayer 

for file in listOfFiles:	
	swfTools.runFlashApp(rootDir + "/" + file)

	swfTools.runFlashApp(rootDir + file)
	sleep(1)

	# focus on the Flash 
	# and make window big 

	swfTools.makeFlashAppFullScreen()
	sleep(0.5)

	# 	take screenshot and save 
	newFile = swfTools.chengeFileFromSwfToPng(file)

	swfTools.takeScreenshot(rootDir + "pic/" + newFile)

	# 	close flashplayer 
	swfTools.closeFlashApp()



'''
def open_flash(filePath):	
	command = "flashplayer /home/nefex/exportswf/JNiemieckiTrends1PdPilot_1.swf"
	x = os.popen(command)
	sleep(1)
	x.close()
	# os.system('flashplayer /home/nefex/exportswf/JNiemieckiTrends1PdPilot_1.swf ')

process = Process(target=open_flash, args=(["arg"]))
process.start()
sleep(5)
killFlashPlayerCommand = "killall flashplayer"
os.system(killFlashPlayerCommand)



#processes = [Process(target=rand_num, args=([4])) for x in range(4)]
# process = Process(target=rand_num, args=(["wtf"]))
'''
'''
process.start()
sleep(1)
process.kill()

type(process)
'''

'''
exit()

print(type([]))

for p in processes:
	p.start()

for p in processes:
	p.join()


exit()
print("hello")

os.system('flashplayer /home/nefex/exportswf/JNiemieckiTrends1PdPilot_1.swf &')

print('xd')
'''
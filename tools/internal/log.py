import os
from time import strftime
import time
from math import floor
from sys import platform

global lastLog
lastLog = None
global newLog
newLog = None

class log():

    def __init__(self, calledFrom="Nowhere", customName=0, logPath="./"):
        try:
            fileSystemChecks().makeDirectory(logPath + "logs/")
        except IOError:
            pass
        if (lastLog is None or not fileSystemChecks().FileExistsCheck(logPath + "logs/" + lastLog)) or newLog:
            self.currentLogName = timeStamp().logName()
        else:
            self.currentLogName = lastLog
        if customName != 0:
            self.currentLogName = customName
        self.file = open(logPath + "logs/" + self.currentLogName + ".log", "a+")
        self.file.write(timeStamp().timeStampGen() + " " + "Hello From " + calledFrom + "\n")


    def __str__(self):
        self.__init__()
        return 1

    def WriteLog(self, input):
        self.file.write(timeStamp().timeStampGen() + " " + input + "\n")
        return 1
    def CloseLog(self, options=0):
        self.WriteLog("Exiting. Goodbye.")

        self.file.close()
        if options == 1:
            newLog = True
            return 1
        else:
            return 1




class timeStamp():
    def __init__(self):
        pass

    def __str__(self):
        self.__init__()
        return 1

    def logName(self):
        filenametime = strftime("%d.%m.%Y-%H.%M.%S", time.localtime(floor(time.time())))
        return filenametime

    def timeStampGen(self):
        readabletime = strftime("%H:%M:%S", time.localtime(floor(time.time())))
        return "[" + readabletime + "]"


class fileSystemChecks():
    def __init__(self):
        pass

    def __str__(self):
        self.__init__()
        return 1

    def FileExistsCheck(self, filename):
        if os.path.exists(filename):
            return True
        return False

    def FileCorrectCheck(self, filename):

        if platform == "linux":
            arr = filename.split("/")
        else:
            arr = filename.split("\\")
        for i in arr:
            if ".py" in i:
                return True
            else:
                return False

    def makeDirectory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
            return 1
        else:
            raise IOError("Folder Already Exists")

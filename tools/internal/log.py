import inspect
import os.path
import time
from os import mkdir, scandir, stat, listdir
from loguru import logger as log
from utils import getFileCalledFrom, getAbsPath

def init(path, file):
    removeOldLogs(path)
    filePath = path + file
    if not os.path.isdir(path + "oldlogs"):
        mkdir(path + "oldlogs")
    if os.path.exists(filePath):
        try:
            os.rename(filePath, path + "oldlogs/" + time.strftime("%Y.%m.%d-%H.%M.%S") + ".log")
        except PermissionError:
            pass
        open(filePath, "w").close()
    logid = log.add(filePath, format="[{time:DD-MM-YYYY HH:mm:ss}][{level}][line {line}][{file}]{message}", level="TRACE")
    return logid

def CloseLog(logid: int):
    log.remove(logid)


def removeOldLogs(path):
    while len(listdir(path + "oldlogs")) >= 3: # REMEMBER GO ONE ABOVE DESIRED LOG OUTPUT OTHERWISE IT WILL GO ONE UNDER
        oldest = 0
        oldestName = ""
        for file in scandir(path + "oldlogs"):
            if time.time() - file.stat().st_mtime > oldest:
                oldest = time.time() - file.stat().st_mtime
                oldestName = file.path
        os.remove(oldestName)



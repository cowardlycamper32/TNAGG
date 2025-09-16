import inspect
import os.path
import time
from os import mkdir, scandir, stat, listdir
from loguru import logger as log
from tools.internal.utils import getFileCalledFrom, getAbsPath

def init(path: str, file: str) -> int:
    """
    initialise the log and remove old logs
    :param path: path to logs folder
    :param file: name of log file
    :return: log ID
    :rtype: int
    """
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

def CloseLog(logid: int) -> None:
    """
    closes the log specified by the id
    :param int logid: the numerical id of the log created from logger.add()
    :return: None
    """
    log.remove(logid)


def removeOldLogs(path):
    """
    removes old logs
    :param path: log folder path
    :return: None
    """
    while len(listdir(path + "oldlogs")) >= 3: # REMEMBER GO ONE ABOVE DESIRED LOG OUTPUT OTHERWISE IT WILL GO ONE UNDER
        oldest = 0
        oldestName = ""
        for file in scandir(path + "oldlogs"):
            if time.time() - file.stat().st_mtime > oldest:
                oldest = time.time() - file.stat().st_mtime
                oldestName = file.path
        os.remove(oldestName)



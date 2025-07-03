import inspect
import os.path
import time
from os import mkdir
from loguru import logger as log
from utils import getFileCalledFrom, getAbsPath

def init(path, file):
    filePath = path + file
    if not os.path.isdir(path + "oldlogs"):
        mkdir(path + "oldlogs")
    if os.path.exists(filePath):
        try:
            os.rename(filePath, path + "oldlogs/" + time.strftime("%Y.%m.%d-%H.%M.%S") + ".log")
        except PermissionError:
            pass
        open(filePath, "w").close()
    logid = log.add(filePath, format="[{time:DD-MM-YYYY HH:mm:ss}][{level}][line {line}]{message}", level="TRACE")
    WriteLog("Log Initialised in '" + getFile() + "'", "success")
    return logid

def WriteLog(message, type):
    match type.lower():
        case "info":
            log.info("[" + getFile() + "] " + message)
        case "debug":
            log.debug("[" + getFile() + "] " + message)
        case "warn":
            log.warning("[" + getFile() + "] " + message)
        case "warning":
            log.warning("[" + getFile() + "] " + message)
        case "error":
            log.error("[" + getFile() + "] " + message)
        case "err":
            log.error("[" + getFile() + "] " + message)
        case "except":
            log.exception("[" + getFile() + "] " + message)
        case "success":
            log.success("[" + getFile() + "] " + message)
        case "critical":
            log.critical("[" + getFile() + "] " + message)
        case "crit":
            log.critical("[" + getFile() + "] " + message)
        case _:
            WriteLog("Erroneous log type, quiting.", "critical")
            exit(1024)


def getFile():
    return inspect.currentframe().f_back.f_code.co_filename.split("\\")[-1]

def CloseLog(logid: int):
    log.remove(logid)

from os import walk
import inspect
def getWP():
    for root, dirs, files in walk("..\\..\\"):
       if "content" in dirs and "tools" in dirs:
           return root


def getFileCalledFrom():
    try:
        return inspect.currentframe().f_back.f_back.f_code.co_filename.split("\\")[-1]
    except AttributeError:
        return inspect.currentframe().f_back.f_code.co_filename.split("\\")[-1]

def getAbsPath(depth: int=1):
    temp = inspect.currentframe().f_back.f_code.co_filename.split("\\")
    for i in range(depth):
        temp.pop(-1)
    return joinPath(temp)
def joinPath(arr):
    out = ""
    for i in arr:
        out += i + "/"
    return out


def safeExit():
    try:
        exit()
    except PermissionError:
        pass
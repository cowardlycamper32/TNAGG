from os import walk
import inspect
def getWP() -> str:
    """
    Get working Path
    :return: the root directory
    :rtype: str
    """
    for root, dirs, files in walk("..\\..\\"):
       if "content" in dirs and "tools" in dirs:
           return root


def getFileCalledFrom():
    """
    Get the file called from
    :return: the file this function was called from
    :rtype: str
    """
    try:
        return inspect.currentframe().f_back.f_back.f_code.co_filename.split("\\")[-1]
    except AttributeError:
        return inspect.currentframe().f_back.f_code.co_filename.split("\\")[-1]

def getAbsPath(depth: int=1) -> str:
    """

    :param int depth: how many directories back, 1 being current directory
    :return: the absuloute path
    :rtype: str
    """
    temp = inspect.currentframe().f_back.f_code.co_filename.split("\\")
    for i in range(depth):
        temp.pop(-1)
    return joinPath(temp)
def joinPath(arr) -> str:
    """
    joins an array of directories
    :param list arr: array of directory names to be joined
    :return: a path made from the array of directories in order from left to right
    :rtype: str
    """
    out = ""
    for i in arr:
        out += i + "/"
    return out

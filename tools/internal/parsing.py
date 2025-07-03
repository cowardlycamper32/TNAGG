import json

from jsonValidation import validator
from utils import getAbsPath, safeExit
import log as log




class Parser:
    def __init__(self, levelPath, entityPath, genericPaths: [str]):
        self.logid = log.init(getAbsPath(3) + "logs/", "main.log")
        validator(logid=self.logid)
        self.contentPath = "../../content/"
        self.levelPath = self.contentPath + levelPath + "/"
        self.entityPath = self.contentPath +  entityPath + "/"
        self.genericPaths = map(lambda genericPaths : self.contentPath + genericPaths, genericPaths)

    def grabLevel(self, levelName):
        temp = open(self.levelPath + levelName + ".json")
        js = json.load(temp)
        temp.close()

        return js

    def grabEntity(self, entityFileName):
        temp = open(self.entityPath + entityFileName + ".json")
        js = json.load(temp)
        temp.close()

        return js

    def ReadLevel(self, level):
        js = self.grabLevel(level)
        level = Level(js)



class Level:
    def __init__(self, js):
        rooms = []
        for room in js["level"]["rooms"]:
            try:
                temp = Room(room["ID"], room["exits"], room["entities"])
                rooms.append(temp)
            except (KeyError, IndexError):
                log.WriteLog("room " + room["ID"] + " has errors", "error")

class Room:
    def __init__(self, id, exits, entities):
        self.ID = id
        self.exits = exits,
        self.entities = entities

parser = Parser("levels/levels", "entities/entities", ["entities/generic", "levels/generic"])
parser.ReadLevel("level1")
log.CloseLog(parser.logid)
#safeExit()

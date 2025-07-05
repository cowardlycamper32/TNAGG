import json

from jsonValidation import validator
from utils import getAbsPath, safeExit
import log as log
from loguru import logger


_path = getAbsPath(3) + "content/"
#print(_path)
_entityPath = _path + "entities/"
#print(_entityPath)
_levelPath = _path + "levels/"
#print(_levelPath)


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
        level = Level(level, js)




class Level:
    def __init__(self, levelName, js):
        self.rooms = []
        for room in js["level"]["rooms"]:
            try:
                temp = Room(levelName, room["ID"], room["exits"], room["entities"])
                self.rooms.append(temp)
                #print(temp)
            except (KeyError, IndexError) as e:
                logger.warning("room " + room["ID"] + " has errors at index " + str(e))
                raise e
    def buildLevel(self):
        pass

class Room:
    def __init__(self, level, id, exits, entities):
        self.ID = id
        self.exits = exits,
        self.entities = entities
        self.actualEntities = {
            "north": [],
            "east": [],
            "south": [],
            "west": []
        }

        self.buildRoom(level)
        print(self.actualEntities)

    def buildRoom(self, level):
        file = open(_levelPath + "levels/" + level + ".json")
        js = json.load(file)
        file.close()
        file = open(_entityPath + "entities/" + level + ".json")
        entjs = json.load(file)
        file.close()
        for i in js["level"]["rooms"]:
            for entity in i["entities"]:
                for ent in entjs:
                    temp = entity.split("/")
                    if temp[-1] in ent.values():
                        if ent["type"] == "generic:spawnPoint":
                            pass
                        elif ent["location"] == "north" or ent["location"] == "n":
                            self.actualEntities["north"].append(ent)
                        elif ent["location"] == "east" or ent["location"] == "e":
                            self.actualEntities["east"].append(ent)
                        elif ent["location"] == "south" or ent["location"] == "s":
                            self.actualEntities["south"].append(ent)
                        elif ent["location"] == "west" or ent["location"] == "w":
                            self.actualEntities["west"].append(ent)




    def __str__(self):
        return f"{self.ID}, {self.exits}, {self.entities}"



class Entity:
    def __init__(self, ID, js):
        self.ID = ID
        try:
            if
            self.location = js["location"]
        except (KeyError, IndexError):

        print(f"{self.ID}, {self.location}")

parser = Parser("levels/levels", "entities/entities", ["entities/generic", "levels/generic"])
parser.ReadLevel("level1")
log.CloseLog(parser.logid)
#safeExit()

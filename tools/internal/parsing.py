import json

from tools.internal.jsonValidation import validator
from tools.internal.utils import getAbsPath
import tools.internal.log as log
from loguru import logger


_path = getAbsPath(3) + "content/"
#print(_path)
_entityPath = _path + "entities/"
#print(_entityPath)
_levelPath = _path + "levels/"
#print(_levelPath)


class Parser:
    def __init__(self, levelPath: str, entityPath: str, genericPaths: [str]):
        """
        create a Parser and initialise log
        :param str levelPath: the path all level JSONs are: 'levels/levels'
        :param entityPath: the path all entity JSONs are: 'entities/entities'
        :param genericPaths: list of all generic paths: ['entities/generic', 'levels/generic']
        """
        self.logid = log.init(getAbsPath(3) + "logs/", "main.log") #initialise the log
        validator(logid=self.logid) #validate the json and warn if errors
        self.contentPath = "../../content/"
        self.levelPath = self.contentPath + levelPath + "/"
        self.entityPath = self.contentPath +  entityPath + "/"
        self.genericPaths = map(lambda genericPaths : self.contentPath + genericPaths, genericPaths) #add absolute path to the start of each path

    def grabLevel(self, levelName) -> dict:
        """
        parse contents of level json file
        :param str levelName: the name of the level file without .json
        :return: the json file contents as a python dictionary
        :rtype: dict
        """
        temp = open(self.levelPath + levelName + ".json")
        js = json.load(temp)
        temp.close()

        return js

    def grabEntity(self, entityFileName) -> list:
        """
        parse contents of level json file
        :param entityFileName: the name of the level entity file without .json
        :return: the json file contents as a list
        :rtype: list
        """
        temp = open(self.entityPath + entityFileName + ".json")
        js = json.load(temp)
        temp.close()

        return js

    def ReadLevel(self, level):
        """
        parse the JSON file into a Level object
        :param level: the name of the level file without .json
        :return: the level object
        :rtype: Level
        """
        js = self.grabLevel(level)
        level = Level(level, js)
        return level




class Level:
    def __init__(self, levelName: str, js: dict):
        """
        create a new Level object and initiialise rooms.
        :param str levelName: name of the level file without .json
        :param dict js: dictionary of information about room
        """
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
        """
        Unused
        :return: None
        """
        pass

class Room:
    def __init__(self, level, id, exits, entities):
        """
        initialise the Room and entities
        :param level: name of the level file without .json
        :param id: level ID, got from the JSON, normally parsed in through Level
        :param exits: level exits, got from the JSON, normally parsed in through Level
        :param entities: level entities, got from the JSON, normally parsed in through Level
        """
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
        #print(self.actualEntities)

    def buildRoom(self, level) -> None:
        """

        :param level: name of the level file without .json
        :return: Nothing
        :rtype: None
        """
        file = open(_levelPath + "levels/" + level + ".json")
        js = json.load(file)
        file.close()
        file = open(_entityPath + "entities/" + level + ".json")
        entjs = json.load(file)
        file.close()
        entitySearchList = list(map(self.iterate, entjs, [self.ID.split(":")[-1]]*len(entjs)))

        for i in range(len(entitySearchList)):
            if entitySearchList[i]:
                match entjs[i]["location"]:
                    case "north":
                        self.actualEntities["north"].append(entjs[i])
                    case "n":
                        self.actualEntities["north"].append(entjs[i])
                    case "east":
                        self.actualEntities["east"].append(entjs[i])
                    case "e":
                        self.actualEntities["east"].append(entjs[i])
                    case "south":
                        self.actualEntities["south"].append(entjs[i])
                    case "s":
                        self.actualEntities["south"].append(entjs[i])
                    case "west":
                        self.actualEntities["west"].append(entjs[i])
                    case "w":
                        self.actualEntities["west"].append(entjs[i])

    def iterate(self, dict: dict, searchTerm: str):
        """
        check if item is in a dictionaries values
        :param list dict: list of entities
        :param str searchTerm: thing to find
        :return: True if item is found, otherwise returns None
        :rtype: Boolean or None
        """
        if searchTerm in dict.values():
            return True

    def __str__(self):
        return f"{self.ID}: {self.exits}, {self.actualEntities}"






class Entity:
    """
    CURRENTLY UNUSED
    """
    def __init__(self, ID, js):
        self.ID = ID
        try:
            self.location = js["location"]
        except (KeyError, IndexError):
            try:
                self.facing = js["facing"]
            except:
                logger.warning(f"error in entity file {js["intName"]} of type {js["type"]}")
        #print(f"{self.ID}, {self.location}")

parser = Parser("levels/levels", "entities/entities", ["entities/generic", "levels/generic"])
level = parser.ReadLevel("level1")
for i in level.rooms:
    print(i)
log.CloseLog(parser.logid)

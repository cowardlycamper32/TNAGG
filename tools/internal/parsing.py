import json

from jsonValidation import validator

validator()

_contentPath = "../../content/"
_entityPath = _contentPath + "entities/entities/"
_levelPath = _contentPath + "levels/levels/"


def grabLevel(levelName):
    temp = open(_levelPath + levelName + ".json")
    js = json.load(temp)
    temp.close()

    print(js)




grabLevel("level1")
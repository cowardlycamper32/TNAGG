import json

class Game:
    pass
class Room:
    def __init__(self):
        pass



class EntityManager:
    def __init__(self, entityFileName: str):
        self.filename = entityFileName
        entities = open("content/entities/levels/" + entityFileName, "r").read()
        self.entities = json.loads(entities)

    def createEntities(self):
        for entity in self.entities:
            try:
                print(entity["content"])
            except KeyError as e:
                exit("Format error in " + self.filename + " at entity \'" + entity["intName"] + "'")






class Entity:
    def __init__(self):
        pass




em = EntityManager("level1.json")
em.createEntities()


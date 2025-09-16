import json
from tools.internal.utils import search

file = open("content/levels/levels/level1.json")
level = json.load(file)
file.close()
file = open("content/entities/entities/level1.json")
entities = json.load(file)
file.close()

#print(level)
#print(entities)




entityList = search(entities, "00")
for i in range(len(entityList)):
    if entityList[i] == True:
        print(entities[i])

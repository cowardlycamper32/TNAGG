import json

file = open("content/levels/levels/level1.json")
level = json.load(file)
file.close()
file = open("content/entities/entities/level1.json")
entities = json.load(file)
file.close()

#print(level)
#print(entities)

def iterate(dict, searchTerm):
    print(dict.values())
    if searchTerm in dict.values():
        return True


entityList = list(map(iterate, entities, ["01"]*len(entities)))
for i in range(len(entityList)):
    if entityList[i] == True:
        print(entities[i])

import json
from jsonschema import validate
import jsonschema.exceptions
from os import scandir as sd
from sys import argv
from log import log as logger
def validator(tool: bool = False):
    log = logger("tools\\json-validation.py", logPath="../../")

    _contentPath = "../../content/"
    _entitiesPath = _contentPath + "entities/"
    _levelsPath = _contentPath + "levels/"

    entitiesGen = {}
    levelsGen = []


    for file in sd(_entitiesPath + "generic"):
        temp = open(file)
        js = json.load(temp)
        temp.close()

        entitiesGen["generic:" + file.name.split(".")[0]] = js
    log.WriteLog("Generic Entity Dictionary Generated")

    for file in sd(_levelsPath + "generic"):
        temp = open(file)
        js = json.load(temp)
        temp.close()

        levelsGen.append(js)
    log.WriteLog("Generic Level List Generated")

    for file in sd(_entitiesPath + "entities"):
        temp = open(file)
        js = json.load(temp)
        temp.close()

        for entity in js:
             for key in entitiesGen.keys():
                 if key == entity["type"]:
                    try:
                        validate(entity, entitiesGen[key])
                    except jsonschema.exceptions.ValidationError as e:
                        if tool:
                            if len(argv) != 2:
                                log.WriteLog("Validation Error in '" + file.path + "': " + e.message)
                                log.CloseLog()
                                exit(f"Validation Error in '{file.path}': {e.message}")
                            else:
                                if argv[1] == "-v" or argv[1] == "--verbose":
                                    log.WriteLog(jsonschema.exceptions.ValidationError(e.message, e.validator, e.path, e.cause, e.context, e.validator_value,
                                                                            e.instance, e.schema, e.schema_path, e.parent))
                                    log.CloseLog()
                                    raise jsonschema.exceptions.ValidationError(e.message, e.validator, e.path, e.cause, e.context, e.validator_value,
                                                                            e.instance, e.schema, e.schema_path, e.parent)
                                else:
                                    log.WriteLog("Validation Error in '" + file.path + "': " + e.message)
                                    log.CloseLog()
                                    exit(f"Validation Error in '{file.name}': {e.cause}")
                        else:
                            log.WriteLog("Validation Error in '" + file.path + "': " + e.message)


    for file in sd(_levelsPath + "levels"):
        temp = open(file)
        js = json.load(temp)
        temp.close()
        for i in range(len(levelsGen)):
            try:
                validate(js, levelsGen[i])
            except jsonschema.exceptions.ValidationError as e:
                if tool:
                    if len(argv) != 2:
                        log.WriteLog("Validation Error in '" + file.path + "': " + e.message)
                        log.CloseLog()
                        exit(f"Validation Error in '{file.path}': {e.message}")
                    else:
                        if argv[1] == "-v" or argv[1] == "--verbose":
                            log.WriteLog(
                                str(jsonschema.exceptions.ValidationError(e.message, e.validator, e.path, e.cause, e.context,
                                                                      e.validator_value,
                                                                      e.instance, e.schema, e.schema_path, e.parent)))
                            log.CloseLog()
                            raise jsonschema.exceptions.ValidationError(e.message, e.validator, e.path, e.cause, e.context,
                                                                    e.validator_value,
                                                                        e.instance, e.schema, e.schema_path, e.parent)
                        else:
                            log.WriteLog("Validation Error in '" + file.path + "': " + e.message)
                            log.CloseLog()
                            exit(f"Validation Error in '{file.name}': {e.cause}")
                else:
                    log.WriteLog("Validation Error in '" + file.path + "': " + e.message)

    log.CloseLog()
if __name__ == "__main__":
    validator(True)
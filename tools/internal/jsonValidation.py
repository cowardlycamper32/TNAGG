import json
from jsonschema import validate
import jsonschema.exceptions
from os import scandir as sd, walk, path
from sys import argv
import log as log
import inspect
import utils
from loguru import logger
def validator(tool: bool = False, logid = None):


    #print(joinPath(inspect.currentframe().f_back.f_code.co_filename.split("\\")[0:3]))

    _path = utils.getAbsPath(3)
    if tool:
        logid = log.init(_path + "logs/", "main.log")
    else:
        if logid is None:
            raise AttributeError("Invalid LogID")
    _contentPath = _path + "content/"
    _entitiesPath = _contentPath + "entities/"
    _levelsPath = _contentPath + "levels/"

    entitiesGen = {}
    levelsGen = []


    for file in sd(_entitiesPath + "generic/"):
        temp = open(file)
        js = json.load(temp)
        temp.close()

        entitiesGen["generic:" + file.name.split(".")[0]] = js
    logger.success("Generic Entity Dictionary Generated")

    for file in sd(_levelsPath + "generic/"):
        temp = open(file)
        js = json.load(temp)
        temp.close()

        levelsGen.append(js)
    logger.success("Generic Level List Generated")

    for file in sd(_entitiesPath + "entities/"):
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
                                logger.critical("Validation Error in '" + file.path + "': " + e.message)
                                log.CloseLog(logid)
                                exit(f"Validation Error in '{file.path}': {e.message}")
                            else:
                                if argv[1] == "-v" or argv[1] == "--verbose":
                                    logger.critical(jsonschema.exceptions.ValidationError(e.message, e.validator, e.path, e.cause, e.context, e.validator_value,
                                                                                       e.instance, e.schema, e.schema_path, e.parent))
                                    log.CloseLog(logid)
                                    raise jsonschema.exceptions.ValidationError(e.message, e.validator, e.path, e.cause, e.context, e.validator_value,
                                                                            e.instance, e.schema, e.schema_path, e.parent)
                                else:
                                    logger.critical("Validation Error in '" + file.path + "': " + e.message)
                                    log.CloseLog(logid)
                                    exit(f"Validation Error in '{file.name}': {e.cause}")
                        else:
                           logger.warning("Validation Error in '" + file.path + "': " + e.message)
    logger.success("All Entities Correct")

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
                        logger.critical("Validation Error in '" + file.path + "': " + e.message)
                        log.CloseLog(logid)
                        exit(f"Validation Error in '{file.path}': {e.message}")
                    else:
                        if argv[1] == "-v" or argv[1] == "--verbose":
                            logger.critical(
                                str(jsonschema.exceptions.ValidationError(e.message, e.validator, e.path, e.cause, e.context,
                                                                      e.validator_value,
                                                                      e.instance, e.schema, e.schema_path, e.parent)))
                            log.CloseLog(logid)
                            raise jsonschema.exceptions.ValidationError(e.message, e.validator, e.path, e.cause, e.context,
                                                                    e.validator_value,
                                                                        e.instance, e.schema, e.schema_path, e.parent)
                        else:
                            logger.critical("Validation Error in '" + file.path + "': " + e.message)
                            log.CloseLog(logid)
                            exit(f"Validation Error in '{file.name}': {e.cause}")
                else:
                    logger.warning("Validation Error in '" + file.path + "': " + e.message)
    logger.success("All levels correct")


if __name__ == "__main__":
    validator(True)

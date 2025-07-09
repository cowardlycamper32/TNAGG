room has level field containing an array of rooms which contains dictionaries containing the ID, exits and entities
structure is:  
level  
```json
{
  "level": {
    "rooms": [
      {
        "ID": "tutorial:01",
        "exits": [
          "tutorial:02"
        ],
        "entities": ["level1/00","level1/01"]
      },
      {
        "ID": "tutorial:02",
        "exits": [
          "tutorial:03", "tutorial:02"
        ],
        "entities": ["level1/02"]
      }
    ]
  }
}
```
- level reader should build the rooms with exits, infer entrances and create entities  
- entities should be got from the entities file of the same name as the room file  
- entities should have a facing or location attribute  
logic should be:  
1. level JSON opened, parsed, loaded and closed
2. entity JSON opened, parsed, loaded and closed
3. for each room, generate room
4. iterate through entity IDs in exits list
5. get entity definition from entity JSON
6. define entity using Entity class.
import json

jsonData1 = '{"a": "2", "b": {"c": "1"}}'
jsonData2 = '{"a": "2", "b": {"c": "5"}}'

jsonToPython1 = json.loads(jsonData1)
jsonToPython2 = json.loads(jsonData2)

for key in jsonToPython1:
    if jsonToPython1[key] != jsonToPython2[key]:
        print(key, " - ", jsonToPython1[key])
        print(key, " - ", jsonToPython2[key])
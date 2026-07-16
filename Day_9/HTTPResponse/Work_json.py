'''
json modules
json.dumps() - Python dict to json string
json.loads() - json string to python dict
'''

import json

user = {

    "id" : 101,
    "name" : "Mayur",
    "active" : True,
    "skills" : ["Python", "FastAPI"]

}


json_string = json.dumps(user)
print(json_string)

json_dict = json.loads(json_string)
print(json_dict)
print(type(json_dict))
print(json_dict["name"])
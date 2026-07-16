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
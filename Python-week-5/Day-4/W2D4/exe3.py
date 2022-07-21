import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

sampleJson = eval(sampleJson)
print(sampleJson['company']['employee']['name'])

with open('./result.json', mode='w') as jsonFile:
    json.dump(sampleJson, jsonFile)
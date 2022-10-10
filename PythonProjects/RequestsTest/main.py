import requests

response_add = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 668,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "test_doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print (response_add.text)

response_update = requests.put("https://petstore.swagger.io/v2/pet", json = {
  "id": 668,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response_update.text)

response_find = requests.get("https://petstore.swagger.io/v2/pet/668")
print(response_find.text)

import requests
import json

database_auth = ""
VariableID = ""
Value = ""
JSON = ""
def createVar(auth:database_auth, name:str, value:any) -> VariableID:
  """
  Creates a new variable and returns the Variable ID, which you can use to retrieve the value using the getValueFromID() Function. 
  
  **Example Script:**

  moneyID = createVar("myUniqueAuth", "money", "$1,291")
  value = getValueFromID(moneyID)    
  print(value)

  **Example Response:**
  
  >> $1, 291
  """
  
  url = "https://userinfo-70d4.restdb.io/rest/datastore"
  payload = json.dumps( {"auth":auth, "name":name, "value": value} )
  headers = {
    'content-type': "application/json",
    'x-apikey': "605d6dd602a77403cf46172b62132a7ebe0b3",
    'cache-control': "no-cache"
    }

  response = requests.request("POST", url, data=payload, 
  headers=headers)
  return response.json()["_id"]
  

def getValueFromID(ID:VariableID) -> Value:
  """
  Retrieve the value from the Variable ID. 
  
  **Example Script:**

  moneyID = createVar("myUniqueAuth", "money", "$1,291")
  value = getValueFromID(moneyID)    
  print(value)

  **Example Response:**
  
  >> $1, 291
  """
  url = "https://userinfo-70d4.restdb.io/rest/datastore/"+ID
  headers = {
    'content-type': "application/json",
    'x-apikey': "605d6dd602a77403cf46172b62132a7ebe0b3",
    'cache-control': "no-cache"
    }

  response = requests.request("GET", url, headers=headers)
  value = response.json()["value"]
  return value

def getJSONFromID(ID:VariableID) -> JSON:
  """
   Retrieve the JSON from the Variable ID.
   
   **Does not work for userGen() Variable IDs, use getUserJSON() instead...**
  
  **Example Script:**

  moneyID = createVar("myUniqueAuth", "money", "$1,291")
  json = getJSONFromID(moneyID)    
  print(json)

  **Example Response:**
  
  >> {'_id': '633cbfd65057d14f0004d011', 'name': 'Hi', 'auth': 'John', 'value': 15}
  """
  url = "https://userinfo-70d4.restdb.io/rest/datastore/"+ID

  headers = {
    'content-type': "application/json",
    'x-apikey': "605d6dd602a77403cf46172b62132a7ebe0b3",
    'cache-control': "no-cache"
    }

  response = requests.request("GET", url, headers=headers)
  value = response.json()
  return value

def userGen(amount_of_users: int, statusUpdate:bool = False) -> JSON:
  """
Generate completely random users with phone numbers, usernames, passwords, adresses, emails, and more.

------------------------------------

**Params** | 
>> amount_of_users: int -> How many users to generate. Must be an int such as 1, 219, or 173. | Generates a maximum of 999 users.
>> statusUpdate: bool -> Print updates on the user generation status. If True -> Will print update for each user created. If False -> Will not print update. | BETA MODE DO NOT RECOMEND!

**Example Script:**
  
ranUser = userGen(5, True)
print(ranUser[0])
print("\n"+ranUser[1]["name"])
print("\n"+str(ranUser[2]["age"]))
  
----------------------------------

**Example Response:**
  
User #1 Created!
User #2 Created!
User #3 Created!
User #4 Created!
User #5 Created!
{'_id': '633c78f45057d14f0004c7d4', 'pass': '9Clifford57', 
'name': 'Bobbie Towne', 'email': 
'Hortense.Mayert@yahoo.com', 'user': 'Carolina_Ruecker', 
'age': 89, 'phone': '040-533-6820', 'address': '6724 
Rodriguez Turnpike\nLake Edgardo, UT 84745', '_mock': True}
   
Chelsey Gusikowski

96

-------------------------------------------------------
_id and _mock are debug elements, ignore them
"""
  import requests as r
  import random as x
  if amount_of_users > 999:
    return "Unable to return that many users"
  else:
    global result
    dbUrl = "https://userinfo-70d4.restdb.io/rest/user-info"
    try:
      data = r.get(dbUrl, headers={"x-apikey":"605d6dd602a77403cf46172b62132a7ebe0b3"}).json()
    except: 
      return "Api is Down"
    #retreving from api
    indexLen = len(data)
    finalR = ""
    ranIndex = x.randint(0, indexLen)
    split1 = str(data).split("}")
    result = split1[ranIndex].split(", {")
    #getting randomResult
    if amount_of_users == 1:
      finalR = "{"+result[1]+"}"
      if statusUpdate:
        print("User #1 Created!")
      jsonFinal = eval(finalR)
      #ending if only 1 response needed
    else:
      finalR = "{"+result[1]+"}"   
      for i in range(amount_of_users):
        #making the users needed
        ranIndex = x.randint(0, indexLen)
        split1 = str(data).split("}")
        result = split1[ranIndex].split(", {")
        finalR = finalR +","+"{"+result[1]+"}"
        if statusUpdate:
          print(f"User #{i+1} Created!")
      jsonFinal = eval("["+finalR+"]")
    return jsonFinal

def getUserJSON(ID:VariableID) -> JSON:
  """
   Retrieve the User Info JSON from the Variable ID. Helpful if you want to keep the User Info for later. 
  
  **Example Script:**

  ranUser = userGen(1, False)
  userID = ranUser["_id"]
  json = getUserJSON(userID)    
  print(json)

  **Example Response:**
  
  >> {'_id': '633c78f45057d14f0004c85c', 'pass': '5Quentin39', 'name': 'Dameon Moen', 'email': 'Damion.DuBuque@yahoo.com', 'user': 'Lloyd.Bechtelar', 'age': 77, 'phone': '919-957-3368', 'address': '042 Charlene Manors Suite 189\nWest Weston, SD 85505-4141', '_mock': True}
  """
  url = "https://userinfo-70d4.restdb.io/rest/user-info/"+ID

  headers = {
    'content-type': "application/json",
    'x-apikey': "605d6dd602a77403cf46172b62132a7ebe0b3",
    'cache-control': "no-cache"
    }

  response = requests.request("GET", url, headers=headers)
  value = response.json()
  return value

def setVar(ID:VariableID, new_value:any) -> VariableID:
  """
  Updates an already created variable and returns the Variable ID, which you can use to retrieve the value using the getValueFromID() Function. 
  
  **Example Script:**

  moneyID = createVar("myUniqueAuth", "money", "$1,291")
  value = getValueFromID(moneyID)    
  print(value)
  updatedMoney = setVar(moneyID, "$1,801")
  updated_value = getValueFromID(moneyID)    
  print(updated_value)

  **Example Response:**
  
  >> $1, 291
  >> $1, 801
  """
  
  url = "https://userinfo-70d4.restdb.io/rest/datastore/"+ID

  payload = "{\"value\":\""+new_value+"\"}"
  headers = {
    'content-type': "application/json",
    'x-apikey': "605d6dd602a77403cf46172b62132a7ebe0b3",
    'cache-control': "no-cache"
    }

  response = requests.request("PUT", url, data=payload, headers=headers)
  return response.json()["_id"]

def removeVar(ID:VariableID) -> None:
  """
  Deletes an already created variable.
  
  **Example Script:**

  moneyID = createVar("myUniqueAuth", "money", "$1,291")
  value = getValueFromID(moneyID)    
  print(value)
  removeVar(moneyID)
  print(getJSONFromID(moneyID))
  print(getValueFromID(moneyID))
  

  **Example Response:**
  
  >> $1, 291
  >> []
  >> Traceback (most recent call last):
  File "main.py", line 262, in <module>
    print(getValueFromID(moneyID))
  File "main.py", line 58, in getValueFromID
    value = response.json()["value"]
TypeError: list indices must be integers or slices, not str
  """
  
  url = "https://userinfo-70d4.restdb.io/rest/datastore/"+ID

  headers = {
    'content-type': "application/json",
    'x-apikey': "605d6dd602a77403cf46172b62132a7ebe0b3",
    'cache-control': "no-cache"
    }

  response = requests.request("DELETE", url, headers=headers)

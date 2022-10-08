import json

class Config:

    def __init__(self, path=None, jsonText=None):

        if path != None:

            with open(path, "r") as f:

                self._json = json.loads(f.read())

        elif jsonText != None:

            self._json = json.loads(jsonText)

        else:

            self._json = {}

    def __getattr__(self, name):

        result = Config()

        if name == "__":

            return self._json

        elif type(self._json) is dict:

            if name not in self._json.keys():

                raise Exception("Key not found in configuration: " + name)

            result._json = self._json[name]
            return result

        elif type(self._json) is list:

            if not name[1:].isdecimal():

                raise Exception("Key does not describe an array index.")
                
            index = int(name[1:])

            if not 0 <= index < len(self._json):  
                
                raise Exception("Key not found in configuration.")

            result._json = self._json[index]
            return result


    def __getitem__(self, keyChain):

        if not self.defined(keyChain):

            raise Exception("The key chain could not be found in config.")

        keys = keyChain.split(".")

        currentLayer = self._json

        for key in keys:

            if type(currentLayer) is dict:

                currentLayer = currentLayer[key]

            elif type(currentLayer) is list:

                index = int(key)
                currentLayer = currentLayer[index]

        return currentLayer

    def defined(self, keyChain):

        keys = keyChain.split(".")

        currentLayer = self._json

        for key in keys:

            if type(currentLayer) is dict:

                if key not in currentLayer.keys():

                    return False

                currentLayer = currentLayer[key]

            elif type(currentLayer) is list:

                if not key.isdecimal():

                    return False
                
                index = int(key)

                if not 0 <= index < len(currentLayer):

                    return False
                
                currentLayer = currentLayer[index]

            else: 

                return False

        return True

    def __repr__(self):

        return self._json.__repr__()

if __name__ == "__main__":

    c = Config("example.json")

    keyChains = ["key1", "key2", "key3", "keyArray", "keyArray.none", 
    "keyArray.0", "keyArray.2", "keyArray.3.2",  "keyArray.3.3", "keyArray.4.keyObject.keyTest"]

    for chain in keyChains:
        print(chain, c.defined(chain), c[chain] if c.defined(chain) else "N/A")

    print(c.keyArray._4.keyObject)
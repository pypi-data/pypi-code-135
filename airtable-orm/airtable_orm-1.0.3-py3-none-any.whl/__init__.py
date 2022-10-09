from airtable_orm.airtable_session import AirtableSession

class AirtableORM:

    __instance = None

    @staticmethod
    def getInstance():
      """ Static access method. """
      if AirtableORM.__instance == None:
         AirtableORM()
      return AirtableORM.__instance


    def __init__(self, connection_string: str):
        is_first = True
        if AirtableORM.__instance != None:
            is_first = False
        else:
            AirtableORM.__instance = self
        self.connection_string = connection_string
        api_key = self.connection_string.split("airtable://:")[1].split("@")[0]
        app_key = self.connection_string.split("airtable://:")[1].split("@")[1]
        self.session = AirtableSession(
            api_key=api_key,
            app_key=app_key
        )
        
    def get_session(self):
        print("Initializing db...")
        return self.session


    
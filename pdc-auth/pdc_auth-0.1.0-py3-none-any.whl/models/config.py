from pydantic import BaseModel

class Lisensi(BaseModel):
    email: str
    pwd: str

class ConfigData(BaseModel):
    lisensi: Lisensi
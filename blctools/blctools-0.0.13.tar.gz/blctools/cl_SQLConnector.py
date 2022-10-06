from . import dirs
from . import fechas


from sqlalchemy import create_engine as ce
import numpy as np
import pandas as pd
import datetime as dt

__all__ = ['SQLConnector',]


class SQLConnector():
    
    def __init__(
        self,
        host= '10.230.1.152',
        port='3306',
        usr = 'driobo',
        pwd = 'd13g0',
        db = 'crom',
        db_type = 'mysql',
        db_dialect = 'pymysql',
        conectar=False
        ):
        
        self._host = None
        self._port = None
        self._usr = None
        self._pwd = None
        self._db = None
        self._db_type = None
        self._db_dialect = None
        self._conexion = None
        self._motor = None
        self._conectado = None

        self.host = host
        self.port = port
        self.usr = usr
        self.pwd = pwd
        self.db = db
        self.db_type = db_type
        self.db_dialect = db_dialect
        self.conectado = False
        self.motor = self.crear_motor()
        
        if conectar:
            self.conectar()
            
    @property
    def host(self):
        return self._host
    @host.setter
    def host(self,val):
        self._host = val

    @property
    def port(self):
        return self._port
    @port.setter
    def port(self,val):
        self._port = val
 
    @property
    def usr(self):
        return self._usr
    @usr.setter
    def usr(self,val):
        self._usr = val
        
    @property
    def pwd(self):
        return self._pwd
    @pwd.setter
    def pwd(self,val):
        self._pwd = val
        
    @property
    def db(self):
        return self._db
    @db.setter
    def db(self,val):
        self._db = val

    @property
    def db_type(self):
        return self._db_type
    @db_type.setter
    def db_type(self,val):
        self._db_type = val
        
    @property
    def db_dialect(self):
        return self._db_dialect
    @db_dialect.setter
    def db_dialect(self,val):
        self._db_dialect = val
        
    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self,val):
        self._motor = val
        
    @property
    def conexion(self):
        return self._conexion
    
    @conexion.setter
    def conexion(self,val):
        self._conexion = val
        if not val is None:
            self.conectado = 'actualizar_status'
    
    @property
    def conectado(self):
        return self._conectado
    
    @conectado.setter
    def conectado(self,val):
        '''Note that "val" is not used'''
        try:
            self._conectado = not self.conexion.closed
        except:
            self._conectado = val
        
    def crear_motor(self,
                       host = None, 
                       port = None,
                       usr = None, 
                       pwd = None,
                       db = None,
                       db_type = None,
                       db_dialect = None,
                       echo=False,
                       future=False
                       ):
        '''Crea un objeto "Engine" para interactuar con la base de datos.'''
        if host is None:
            host = self.host
            
        if port is None:
            port = self.port
              
        if usr is None:
            usr = self.usr
            
        if pwd is None:
            pwd = self.pwd
            
        if db is None:
            db = self.db
            
        if db_type is None:
            db_type = self.db_type
            
        if db_dialect is None:
            db_dialect = self.db_dialect
            
        if db_dialect:
            url = f"{db_type}+{db_dialect}://{usr}:{pwd}@{host}:{port}/{db}"
        else:
            url = f"{db_type}://{usr}:{pwd}@{host}:{port}/{db}"

        return ce(url,echo=echo,future=future)
    
    def conectar(self,mensajes=False):
        '''Intenta conectarse a la base de datos'''
        self.conexion = self.motor.connect()
        
        if mensajes:
            if self.conectado:
                print('Conexión exitosa')
            else:
                print("Imposible conectarse a la Base de Datos del CROM")
    
    def desconectar(self,mensajes=False):
        
        if self.conectado:
            self._conexion.close()
            self.conexion = self._conexion
        
        if mensajes:
            if not self.conectado :
                print('Desconexión exitosa')
            else:
                print("Error al desconectar.")

        
    def checkear_conexion(self,mensajes=False):
        
        if not self.conectado:
            try:
                self.conectar(mensajes=mensajes)
            except:
                pass
            
        return self.conectado
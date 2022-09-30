from configparser import ConfigParser
from pathlib import Path
import pandas as pd


class ClassAPI(object):
    """Base Class API"""

    def __init__(self, config_path='', config_file='', config_key='capstone'):
        config_path = config_path if config_path else str(Path(Path.home(), '.config', 'capstone_api'))
        config_file = config_file if config_file else 'capstone_api.ini'
        config_key = config_key if config_key else "discord"
        config_ini = Path(config_path, config_file)
        self.CAPSTONE_CONFIG = str(config_path)
        self.CAPSTONE_PATH = str(Path.cwd())
        if config_ini.exists():
            config = ConfigParser()
            config.read(config_ini)
            self.CAPSTONE_PATH = config[config_key].get('CAPSTONE_PATH')

    def loadStudents(self, capstone_folder='', csv_file='students.csv'):
        capstone_folder = capstone_folder if capstone_folder else self.CAPSTONE_PATH
        csv_file = str(Path(capstone_folder, csv_file))
        self.df_students = pd.read_csv(csv_file)
        return self.df_students

    def saveStudents(self, df_students='', capstone_folder='', config_folder='', csv_file='students.csv'):
        self.df_students = df_students if df_students else self.loadStudents()
        capstone_folder = capstone_folder if capstone_folder else self.CAPSTONE_PATH
        csv_file = str(Path(capstone_folder, csv_file))
        self.df_students.to_csv(csv_file, index=False)

        config_folder = config_folder if config_folder else self.CAPSTONE_CONFIG
        csv_file = str(Path(config_folder, csv_file))
        self.df_students.to_csv(csv_file, index=False)

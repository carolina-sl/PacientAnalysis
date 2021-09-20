
import configparser


class MySqlConfig:
    def __init__(self, configuration_section):
        config = configparser.ConfigParser()
        config.read('../config/db.config.ini')
        self.host = config[configuration_section]['host']
        self.database = config[configuration_section]['database']
        self.user = config[configuration_section]['user']
        self.password = config[configuration_section]['password']

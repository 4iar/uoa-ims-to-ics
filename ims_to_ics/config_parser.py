import configparser

class Config():

    def __init__(self, config_filename='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_filename)

    def getint(self, section, key):

        return self.config.getint(section, key)

    def get(self, section, key):

        return self.config.get(section, key)


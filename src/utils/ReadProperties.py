import configparser
import os

current_directory = os.getcwd() + "\configurations"

configpath = os.path.normpath(os.path.join(current_directory,"config.ini"))
config = configparser.RawConfigParser()
config.read(configpath)


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getHeadless() -> bool:
        headless = config.get('common info','headless')
        return headless

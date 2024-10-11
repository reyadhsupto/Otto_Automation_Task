from src.utils.ReadProperties import ReadConfig
from src.utils.CustomLogger import LogGen

class TestBase:
    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
import configparser

config=configparser.RawConfigParser()
config.read("./Configurations/loginDetails.ini")

class ReadLoginConfig():
    def getsauceDemoURL(self):
        return config.get("URLS","sauceDemoURL")

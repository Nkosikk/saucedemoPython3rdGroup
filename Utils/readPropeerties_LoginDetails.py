import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/loginDetails.ini")


class ReadLoginConfig():
    def getSauceDemoURL(self):
        return config.get("URLS", "sauceDemoURL")

    def getUserName(self):
        return config.get('Login Details', 'username')


    def getPassword(self):
        return config.get('Login Details',  'password')

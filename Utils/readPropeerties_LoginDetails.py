import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/loginDetails.ini")


class ReadLoginConfig():
    def getSauceDemoURL(self):
        return config.get("URLS", "sauceDemoURL")

    def getUserName(self):
        return config.get('Login Details', 'username')


    # TODO create function to read password = Motlatso

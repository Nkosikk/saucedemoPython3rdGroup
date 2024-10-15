import configparser

config=configparser.RawConfigParser()
config.read("./Configurations/loginDetails.ini")

class ReadLoginConfig():
    def getsauceDemoURL(self):
        return config.get("URLS","sauceDemoURL")




    #TODO create function to read username =  MoreBlessing
    #TODO create function to read password = Motlatso

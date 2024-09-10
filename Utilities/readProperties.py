import configparser

config = configparser.RawConfigParser()
config.read('.\\Configuration\\config.ini')

class ReadConfig():
    @staticmethod
    def getAppUrl():
        url = config.get('common Data','baseUrl')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common Data','userName')
        return username


    @staticmethod
    def getPassWord():
        password = config.get('common Data','passWord')
        return password

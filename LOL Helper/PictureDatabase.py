class DataBase(object):
    def __init__(self):
        self.settings = Settings()
        self.data = {"picturesDir": self.settings.getData("Picture")}

    def picture(self,variable, integer):
        return self.data["picturesDir"]+"/" + variable + integer + ".png"

class Settings(object):
    def __init__(self):
        pass
    def readline(self,lineNumber):
        try:
            file = open("Settings.ini")
            for i in range(lineNumber):
                line = file.readline()
            file.close()
            return line
        except:
            return False

    def getPictureLocation(self):
        return self.getData("PicturesLocation")

    def getData(self,variable):
        data = ""
        line = self.readline(2)
        if line:
            record = False
            for char in line:
                if record:
                    data += char
                if char == "=":
                    record = True
            data.replace(" ", "")
        return data






from Data import Data
from PictureDatabase import DataBase
import copy

class Monitor(object):
    def __init__(self,plClass):
        self.PictureDataBase = DataBase()
        self.pl = plClass

        self.infoBarBbox = ((2203,8),(2600,25))

        self.csbboxes = (((219,0),(231,17)),((230,0),(242,17)),)

    def _getPaths(self, variable, reset = False):
        paths = []
        for number in range(0,10):
            paths.append(self.PictureDataBase.picture(variable, str(number)))

        return paths

    def update(self, forctimeupdate = False):
        """

        :return: True if it found and updated all the data in the info box
        """
        f_properUpdate = (0,0,0)
        if forctimeupdate:
            #force updating of the time. Used during init so you can get starting time.
            pass
        #update cs
        cs = []
        ss = self.pl.ScreenShot(bbox = self.infoBarBbox)

        #find the fistnumber of CS
        ssCopy = copy.copy(ss)
        ssCopy.crop(self.csbboxes[0])

        i = 0
        for path in self._getPaths("cs1-"):

            if ssCopy.contains(self.pl.Picture(path), us_similarity=True):

                cs.append(i)
                f_properUpdate[0] = 1
                break
            i += 1
            if i == 9:
                return(f_properUpdate)

        #find the second number of CS
        ssCopy = copy.copy(ss)
        ssCopy.crop(self.csbboxes[1])

        i = 0
        for path in self._getPaths("cs2-"):
            if ssCopy.contains(self.pl.Picture(path), us_similarity=True):

                cs.append(i)
                f_properUpdate[1] = 1
                break
            i += 1
            if i == 9:
                return(f_properUpdate)

        return f_properUpdate





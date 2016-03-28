from PIL import Image,ImageGrab

class Picture(object):
    def __init__(self,file, xColors=[], bbox = None):
        self.name = file
        self.picture = Image.open(file).convert("RGB")
        self.data = self.picture.load()
        self.res = self.picture.size
        self.colors = {}
        if bbox == None:
            bbox = ((0,0),(self.res))
        self._createColorsData(xColors)
         
    def _createColorsData(self, xColors):
        """creates the dict colors. example{(255,255,255):((25,30),(0,0))}"""
        x = 0
        y = 0
        for l in range(self.res[0]):
            for h in range(self.res[1]):
                color = self.data[x,y]
                if color in self.colors:
                    self.colors[color].append((x,y))
                elif color not in self.colors and color not in xColors:
                    self.colors[color] = []
                    self.colors[color].append((x,y))
                elif color in xColors:
                    continue
                else:
                    print("error in Picture.creatColorList x,y,color: ",x,y,color)
                y += 1
            x+=1
            y = 0

    def _getColorLocations(self,color):
        """returns all pixel location for a color"""
        try:
            return self.colors[color]
        except:
            print(color, " Does not exist in: ", self.name)
            return False

    def _match(self, location, crop):
        """searches"""
        self_x = location[0] ; self_y = location[1]
        cropped_x = 0  ; cropped_y = 0

        for x in range(crop.res[0]):
            for y in range(crop.res[1]):
                self_color = self.getPixelColor((self_x,self_y))
                crop_color = crop.getPixelColor((cropped_x,cropped_y))

                if self_color != crop_color:
                    return False
                else:
                    self_y += 1
                    cropped_y += 1
            self_x += 1
            self_y = location[1]
            cropped_x += 1
            cropped_y = 0
        return True
                    
    def getColors(self):
        """returns list of all colors in the picture"""
        return self.colors
        
    def getPixelColor(self,location):
        """returns the color of the pixel in the given location"""
        return self.data[location[0],location[1]]
    
    def getFirstColor(self):
        """not used"""
        for color in self.colors.keys():
            return color

    def contains(self,crop):
        """test to see if the crop is in the image"""
        #search the image by color (R,G,B) values
        crop_color = crop.getPixelColor((0,0))

        #this will return all the locations that the crop_color exist in self or False if it does not exist
        self_color_locations = self._getColorLocations(crop_color)
        if self_color_locations:
            for location in self_color_locations:
                found = self._match(location,crop)
                if found == True:
                    end = location[0]+crop.res[0], location[1]+crop.res[1]
                    return(location, end)
        return False

class ScreenShot(Picture):
    def __init__(self,picture = None, xColors = [], bbox = None):
        if picture ==None:
            if bbox != None:
                self.picture = ImageGrab.grab(bbox)
            else:
                self.picture = ImageGrab.grab()
        else: self.picture = picture

        self.data = self.picture.load()
        self.res = self.picture.size
        self.colors = {}

        self._createColorsData(xColors)
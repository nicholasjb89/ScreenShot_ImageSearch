from PIL import Image,ImageGrab


class Picture(object):
    def __init__(self,file, xColors=[], bbox = None):
        self.picture = Image.open(file).convert("RGB")
        self.data = self.picture.load()
        self.res = self.picture.size

        if bbox == None:
            bbox = ((0,0),(self.res))
        self._createColorsData(xColors,bbox)
         
    def _createColorsData(self, xColors,bbox):
        """creates the dict colors. example{(255,255,255):((25,30),(0,0))}"""
        self.colors = {}
        length = bbox[1][0] - bbox[0][0]
        height = bbox[1][1] - bbox[0][1]
        x = bbox[0][0]
        y = bbox[0][1]
        for l in range(length):
            for h in range(height):
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
                    
    def getColors(self):
        """returns list of all colors in the picture"""
        #may be an error in this somewhere last color got fucked up
        return self.colors
    
    def getColorLocations(self,color):
        """returns all pixel location for a color"""
        try:
            return self.colors[color]
        except:
            print(color, " Does not exist in this SS")
            return False
        
    def getPixelColor(self,location):
        """returns the color of the pixel in the given location"""
        return self.data[location[0],location[1]]
    
    def getFirstColor(self):
        for color in self.colors.keys():
            return color
        
class Screen(Picture):
    def __init__(self,picture = None, xColors = [], bbox = None):
        if picture ==None: self.picture = ImageGrab.grab()
        else: self.picture = picture

        self.data = self.picture.load()
        self.res = self.picture.size
        
        if bbox == None:
            bbox = ((0,0),(self.res))
        self._createColorsData(xColors,bbox)

def searchByColor(picture,screen):
                
    pictureColor = picture.getPixelColor((0,0))
    screenLocations = screen.getColorLocations(pictureColor)
    if screenLocations:
        for location in screenLocations:
            found = search(location,picture,screen)
            if found == True:
                end = location[0]+picture.res[0], location[1]+picture.res[1]
                return location,end
    return False

def search(location,picture,screen):
    """if picture is found will return true"""
    sX = location[0] ; sY = location[1]
    pX = 0 ; pY = 0
    for x in range(picture.res[0]):
        for y in range(picture.res[1]):
            pColor = picture.getPixelColor((pX,pY))
            sColor = screen.getPixelColor((sX,sY))
            
            if pColor != sColor: return False
            pY += 1 ; sY +=1
        sX +=1 ; pX += 1
        pY = 0 ; sY = location[1]
    return True

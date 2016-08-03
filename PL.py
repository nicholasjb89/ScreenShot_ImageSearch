from PIL import Image,ImageGrab

class Picture(object):
    def __init__(self,file, xColors=[]):
        self.name = file
        self.picture = Image.open(file).convert("RGB")
        self.data = self.picture.load()
        self.res = self.picture.size
        self.colors = {}
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
            #print(color, " Does not exist in: ", self.name)
            return False

    def _match(self, location, crop, us_similarity = False, threshold = 20):
        """

        :param location: pixel location (x,y)
        :param crop: Picture Object
        :param us_similarity: Used for transparent crops
        :param threshold: how close should the pixel be to the sources pixel color
        :return: True or False if it is the same or close if that flag is set
        """
        self_x = location[0] ; self_y = location[1]
        cropped_x = 0  ; cropped_y = 0

        for x in range(crop.res[0]):
            for y in range(crop.res[1]):
                self_color = self.getPixelColor((self_x,self_y))
                crop_color = crop.getPixelColor((cropped_x,cropped_y))
                if self_color == False:
                    return False
                elif crop_color == False:
                    return False

                if us_similarity:
                    if not is_similar(self_color,crop_color,threshold):
                        return False
                else:
                    if self_color != crop_color:
                        return False
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
        try:
            return self.data[location[0],location[1]]
        except IndexError:
            return False
    
    def getFirstColor(self):
        """not used"""
        for color in self.colors.keys():
            return color

    def contains(self, crop, us_similarity = False, threshold = 50):
        if not us_similarity:
            #test to see if the crop is in the image This is an exact match
            #search the image by color (R,G,B) values
            crop_color = crop.getPixelColor((0,0))

            #this will return all the locations that the crop_color exist in self or False if it does not exist
            self_color_locations = self._getColorLocations(crop_color)
            if self_color_locations:
                for location in self_color_locations:
                    found = self._match(location,crop,us_similarity, threshold)
                    if found:
                        end = location[0]+crop.res[0], location[1]+crop.res[1]
                        return[location, end]
            return False
        else:
            #us_similarity = True
            for x in range(self.res[0]):
                for y in range(self.res[1]):
                    found = self._match((x,y),crop,us_similarity=True)
                    if found:
                        end = [x+crop.res[0], y+crop.res[1]]
                        return[[x,y], end]
            return False

    def crop(self, bbox):
        x1, y1, x2, y2 = bbox[0][0], bbox[0][1], bbox[1][0], bbox[1][1]
        self.picture = self.picture.crop((x1,y1,x2,y2))
        self.data = self.picture.load()
        self.res = self.picture.size
        self._createColorsData(xColors=[])

    def save(self,name):
        self.picture.save(name)

class ScreenShot(Picture):
    def __init__(self,picture = None, xColors = [], bbox = None):
        if picture ==None:
            if bbox != None:
                x1, y1, x2, y2 = bbox[0][0], bbox[0][1], bbox[1][0], bbox[1][1]
                self.picture = ImageGrab.grab(bbox=(x1,y1,x2,y2))
            else:
                self.picture = ImageGrab.grab()
        else: self.picture = picture

        self.name = "ScreenShot"
        self.data = self.picture.load()
        self.res = self.picture.size
        self.colors = {}

        self._createColorsData(xColors)

def luminance(pixel):
    return (0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])

def is_similar(pixel_a, pixel_b, threshold):
    return abs(luminance(pixel_a) - luminance(pixel_b)) < threshold
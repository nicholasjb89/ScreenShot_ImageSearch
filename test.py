import PL
from PIL import ImageGrab

def searchByColorTest():
    POINT1 = (0,0)
    POINT2 = (50,50)
    ImageGrab.grab((POINT1[0],POINT1[1],POINT2[0],POINT2[1])).convert("RGB").save("SS.bmp","BMP")
    image = PL.Picture("SS.bmp")
    screen = PL.Screen()
    return PL.searchByColor(image, screen)

print(searchByColorTest())
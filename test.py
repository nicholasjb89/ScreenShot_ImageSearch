import PL
from PIL import ImageGrab
import unittest

class SearchByColorTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_cropped_image_format_bmp(self):
        full_image = PL.Picture("RedFull.bmp")
        cropped = PL.Picture("RedCropped.bmp")
        self.assertNotEqual(PL.searchByColor(cropped,full_image),False)

    def test_cropped_image_format_png(self):
        full_image = PL.Picture("RedFull.png")
        cropped = PL.Picture("RedCropped.png")
        self.assertNotEqual(PL.searchByColor(cropped,full_image),False)

    def test_cropped_image_two_different_file_formats(self):
        full_image = PL.Picture("RedFull.jpg")
        cropped = PL.Picture("RedCropped.bmp")
        self.assertNotEqual(PL.searchByColor(cropped,full_image),False)

    def test_screenshot_image(self):
        POINT1 = (0,0)
        POINT2 = (50,50)
        ImageGrab.grab((POINT1[0],POINT1[1],POINT2[0],POINT2[1])).convert("RGB").save("SS.bmp","BMP")
        image = PL.Picture("SS.bmp")
        screen = PL.Screen()
        self.assertEqual(PL.searchByColor(image,screen), (POINT1,POINT2))


if __name__ == "__main__":
    unittest.main()


from PL import Picture,ScreenShot
from PIL import ImageGrab
import unittest

class Picture_contains_image_test(unittest.TestCase):

    def setUp(self):
        self.cropped_location = ((69,0),(230,156))

    def test_cropped_image_format_bmp(self):
        full_image = Picture("test/RedFull.bmp")
        cropped = Picture("test/RedCropped.bmp")
        self.assertEqual(full_image.contains(cropped),self.cropped_location)

    def test_correct_found_location(self):
        full_image = Picture("test/RedFull.bmp")
        cropped = Picture("test/RedCropped.bmp")
        self.assertEqual(full_image.contains(cropped),(self.cropped_location))

class ScreenShot_contains_image_test(unittest.TestCase):
    def setUp(self):
        self.cropped_location = (0,0,50,50)

    def test_cropped_image(self):
        screen_shot = ScreenShot()
        cropped = ScreenShot(bbox=self.cropped_location)
        correct = (self.cropped_location[0], self.cropped_location[1]),\
                  (self.cropped_location[2], self.cropped_location[3])
        self.assertEqual(screen_shot.contains(cropped),correct)

if __name__ == "__main__":
    unittest.main()


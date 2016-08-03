from PL import Picture,ScreenShot
import unittest

class Picture_contains_image_test(unittest.TestCase):

    def setUp(self):
        self.cropped_location = ((69,0),(230,156))

    def test_cropped_image_format_bmp(self):
        full_image = Picture("RedFull.bmp")
        cropped = Picture("RedCropped.bmp")
        self.assertEqual(full_image.contains(cropped),self.cropped_location)

    def test_correct_found_location(self):
        full_image = Picture("RedFull.bmp")
        cropped = Picture("RedCropped.bmp")
        self.assertEqual(full_image.contains(cropped),(self.cropped_location))

    def test_croped_image_similar_equale_format_png(self):
        full_image = Picture("TransparentNumbersSource.png")
        cropped = Picture("TransparentNumbersCropped.png")
        self.assertEqual(full_image.contains(cropped,us_similarity=True),((0,0),(51,14)))

    def test_croped_image_similar_notEquale_format_png(self):
        full_image = Picture("TransparentNumbersCroppedNotSimilar.png")
        cropped = Picture("TransparentNumbersCropped.png")
        self.assertNotEqual(full_image.contains(cropped,us_similarity=True),((0,0),(51,14)))

class ScreenShot_contains_image_test(unittest.TestCase):
    def setUp(self):
        self.cropped_location = (0,0,50,50)

    def test_cropped_image(self):
        # will not pass if the second screenshot and the first are to far apart and the screen has
        # changed even a pixel in the (0,0,50,50) bbox area.
        screen_shot = ScreenShot()
        cropped = ScreenShot(bbox=self.cropped_location)
        correct = (self.cropped_location[0], self.cropped_location[1]),\
                  (self.cropped_location[2], self.cropped_location[3])
        self.assertEqual(screen_shot.contains(cropped),correct)

    def test_cropped_image_similar(self):
        #this can only passs when a league game is running and the score is 0/0/0
        screen_shot = ScreenShot()
        cropped = Picture("TransparentNumbersCropped.png")
        contains = screen_shot.contains(cropped,us_similarity=True)
        print(contains)
        self.assertNotEqual(contains,False)

if __name__ == "__main__":
    unittest.main()
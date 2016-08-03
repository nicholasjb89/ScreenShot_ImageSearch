from Monitor import Monitor
from PictureDatabase import DataBase, Settings
import PL
import unittest
import time

class TestMonitor(unittest.TestCase):
    """
    def test_FindInfoBox(self):
        monitor = Monitor(PL)
        self.assertNotEqual(monitor.infoboxBbox, False)
        """

    def test_update(self):
        monitor = Monitor(PL)
        monitor.update()

    def test_update_infinit(self):
        #remove this for normal testing
        monitor = Monitor(PL)
        while True:
            time.sleep(.2)
            monitor.update()

class TestSettings(unittest.TestCase):
    def test_getPicturesLocation(self):
        settings = Settings()
        self.assertEqual(settings.getPictureLocation(), "Pictures")

class TestDataBase(unittest.TestCase):

    def test_picture(self):
        self.assertEqual(DataBase().picture("time","0"),"Pictures/time0.png")

if __name__ == "__main__":
    unittest.main()
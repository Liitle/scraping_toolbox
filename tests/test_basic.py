import scraping_toolbox
import unittest


class BasicTestCase(unittest.TestCase):
    """ Basic test cases """

    def test_basic(self):
        """ check True is True """
        self.assertTrue(True)

    def test_version(self):
        """ check scraping_toolbox exposes a version attribute """
        self.assertTrue(hasattr(scraping_toolbox, "__version__"))
        self.assertIsInstance(scraping_toolbox.__version__, str)


if __name__ == "__main__":
    unittest.main()

import sys

from selenium import webdriver


class Driver:
    _driver = None

    @staticmethod
    def get_driver():
        """
        Returns the webdriver with chromedriver or create if not exists.
        :return: The driver to navigate and get the html of the page
        """
        try:
            if len(sys.argv) > 1:
                if Driver._driver is None:
                    Driver._driver = webdriver.Chrome(executable_path=sys.argv[1])
                return Driver._driver
            else:
                raise Exception("Please provide a path to the chromedriver")
        except Exception:
            raise FileNotFoundError("Could not execute webdriver. Make sure you provided the correct path to the "
                                    "chromedriver")

    @staticmethod
    def init_driver(driver_path):
        """
        Initialize the webdriver with chromedriver.
        :param driver_path: Path of the driver
        :return: The driver to navigate and get the html of the page
        """
        try:
            if driver_path != "":
                Driver._driver = webdriver.Chrome(executable_path=driver_path)
            else:
                raise Exception("Please provide a path to the chromedriver")
        except Exception:
            raise FileNotFoundError("Could not execute webdriver. Make sure you provided the correct path to the "
                                    "chromedriver")

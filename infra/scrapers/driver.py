import sys

from selenium import webdriver


class Driver:
    _driver = None

    @staticmethod
    def get_driver():
        """
        Initialize the webdriver with chromedriver.
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

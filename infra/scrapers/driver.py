import sys
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig(filename='driver_log_file.log',
                    format='%(asctime)s-%(levelname)s-FILE:%(filename)s-FUNC:%(funcName)s-LINE:%(lineno)d-%(message)s',
                    level=logging.INFO)

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
                    logging.info(f"Driver loaded succesfully from {sys.argv[1]}")
                return Driver._driver
            else:
                logging.error(f"Driver cannot be found. User entered: {sys.argv[1]}")
                raise Exception("Please provide a path to the chromedriver")

        except Exception as e:
            logging.error(f"Driver cannot be found. User entered: {sys.argv[1]}")
            raise FileNotFoundError("Could not execute webdriver. Make sure you provided the correct path to the "
                                    "chromedriver",e )

    @staticmethod
    def init_driver(driver_path):
        """
        Initialize the webdriver with chromedriver.
        :param driver_path: Path of the driver
        :return: The driver to navigate and get the html of the page
        """
        try:
            if driver_path != "":
                chrome_options = Options()
                # chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                Driver._driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
            else:
                raise Exception("Please provide a path to the chromedriver")
        except Exception as e:
            logging.error(f"Driver cannot be found. Path entered: {driver_path}")
            raise FileNotFoundError("Could not execute webdriver. Make sure you provided the correct path to the "
                                    "chromedriver", e)
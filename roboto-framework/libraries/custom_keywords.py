"""Custom Python Keywords"""

import json
import os
import time
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


def get_current_url():
    """Get the current page URL"""
    selenium = BuiltIn().get_library_instance("SeleniumLibrary")
    return selenium.get_location()


def wait_and_log_until_url_contains(text, timeout=10):
    """Wait until URL contains specified text and log the process"""
    selenium = BuiltIn().get_library_instance("SeleniumLibrary")
    start_time = time.time()
    end_time = start_time + float(timeout)

    logger.info(f"Waiting for URL to contain text: '{text}'")

    while time.time() < end_time:
        current_url = selenium.get_location()
        if text in current_url:
            elapsed = time.time() - start_time
            logger.info(f"URL contains expected text, took {elapsed:.2f} seconds")
            return True
        time.sleep(0.1)

    logger.error(f"Timeout: URL did not contain text '{text}'")
    current_url = selenium.get_location()
    logger.error(f"Current URL: {current_url}")
    return False


def load_test_data_from_json(file_name="test_data.json"):
    """Load test data from a JSON file"""
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, "data", file_name)

        with open(file_path, "r") as file:
            data = json.load(file)

        logger.info(f"Successfully loaded test data: {file_path}")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {str(e)}")
        return {}


def take_numbered_screenshot(name="screenshot"):
    """Take a numbered screenshot"""
    selenium = BuiltIn().get_library_instance("SeleniumLibrary")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{name}_{timestamp}.png"
    selenium.capture_page_screenshot(filename)
    logger.info(f"Screenshot taken: {filename}")
    return filename

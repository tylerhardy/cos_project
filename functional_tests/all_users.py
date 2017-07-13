# -*- coding: utf-8 -*-                                         # Indicates the coding of the file.
from selenium import webdriver                                  # Imports 'selenium' and 'unittest', a Python library for testing.
import unittest

class NewVisitorTest(unittest.TestCase):                        # Creats a 'TestCase' class, named 'NewVisitorTest'.

    def setUp(self):                                            # A 'setUp' method that initializes the test.
        self.browser = webdriver.Chrome()                      # Opens the browser.
        self.browser.implicitly_wait(3)                         # Waits 3 seconds if needed (if the page is not loaded).

    def tearDown(self):                                         # A 'tearDown' method that runs after each test.
        self.browser.quit()                                     # Closes the browser.

                                                                # The 'setUp' and 'tearDown' methods run at the beginning and at the end of each 'test' method.

    def test_it_worked(self):                                   # A method that starts with 'test'.
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)  # Asserts that the title of the webpage has 'Welcome to Django' in it.

if __name__ == '__main__':                                      # Only if Python runs the file directly (not imported) it will execute the function 'unittest.main()'.  
                                                                # This function launches the 'unittest Test runner', that identifies the different tests defined by looking for methods that start with 'test'.
    unittest.main(warnings='ignore')                            # The 'unittest.main() function is called with the optional parameter "warnings='ignore'" to avoid a ResourceWarning message.
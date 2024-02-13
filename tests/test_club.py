"""..."""
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from app.models import Club


class Testclub(unittest.TestCase):
    """..."""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:8000/")
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_title_presence(self):
        """..."""
        title = self.driver.title
        self.assertEqual(title, "Hello Page")

    def test_hello_text_presence(self):
        """..."""
        hello_text = self.driver.find_element(By.CLASS_NAME, "display-1").text
        self.assertEqual(hello_text, "HELLO")

    def test_count(self):
        """..."""
        count_element = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div')
        count_text = count_element.text
        self.assertEqual(int(count_text), 117389)

    # def test_count_object(self):
    #     """..."""
    #     club_count = Club.objects.count()
    #     expected_count = 117389
    #     self.assertEqual(club_count, expected_count)

if __name__ == "__main__":
    unittest.main()

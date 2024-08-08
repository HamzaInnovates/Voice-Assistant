from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, TimeoutException
import time

class Info:
    def __init__(self, driver_path):
        options = Options()
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(service=Service(driver_path), options=options)

    def get_info(self, query):
        self.driver.get('https://www.wikipedia.org')
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()



class Music:
    def __init__(self, driver_path):
        options = Options()
        options.add_argument('--disable-gpu')
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(service=Service(driver_path), options=options)

    def play(self, query):
        self.driver.get(f'https://www.youtube.com/results?search_query={query}')
        
        try:
            # Wait for video elements to be clickable
            video = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@id='video-title']"))
            )
            video.click()
            
            # Wait for the video player to be ready
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "html5-video-player"))
            )
            while True:
                time.sleep(5)  
                self.driver.execute_script("document.querySelector('video').play()")
                self.driver.execute_script("document.dispatchEvent(new KeyboardEvent('keydown', {'key': 'k'}))")
      
                try:
                    play_button = WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@class='ytp-play-button ytp-button']"))
                    )
                    if play_button.get_attribute('aria-label') == 'Play (k)':
                        play_button.click()
                except TimeoutException:
                    continue 
            
        except (ElementClickInterceptedException, ElementNotInteractableException, TimeoutException) as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            self.driver.quit()



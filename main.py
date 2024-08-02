from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc

import requests
from fake_useragent import UserAgent
import pickle
import time

import json

class uraRuGrabber:
    def __init__(self):
        #init selenium
        self.url = 'https://ura.news/news/1052773324'
        self.options = webdriver.ChromeOptions()
        self.service = Service(executable_path = ChromeDriverManager().install())
        self.driver = uc.Chrome(options=self.options,service = self.service, version_main= 121)
        self.waiter = WebDriverWait(self.driver, 5)
        self.scroll_to_element = ActionChains(self.driver)
        with open('elementAttribute.json','r') as x:
            self.elementAttribute = json.load(x)
    
    
    def read_comments_text(self):
        text_comment = ''
        all_info_comment = self.waiter.until(EC.presence_of_element_located((By.CLASS_NAME, 'comment-container')))
        author_comment = all_info_comment.find_element(By.CLASS_NAME, ".comment-container:nth-child .ng-binding")
        print(author_comment.text)
        print(all_info_comment)
    def search_btn(self):
        try:
            showBtn = self.driver.find_element(By.CSS_SELECTOR, ".no-print:nth-child(11) .btn-comments-expand")
            self.scroll_to_element.move_to_element(showBtn).perform()
            closeHuita = self.waiter.until(EC.element_to_be_clickable((By.CLASS_NAME, 'bannerStickyClose'))).click()
            try:
                showBtn.click()
            except Exception:
                print('no click :(')
            print('yes btn :)')
        except Exception:
            print('no btn :(')
    def comment_input_wrapper(self):
        try:
            comment_wrapper = self.waiter.until(
                    EC.presence_of_element_located((By.CLASS_NAME, self.elementAttribute["commentWrapperClass"])))
            self.scroll_to_element.move_to_element(comment_wrapper).perform()
            self.search_btn()
        except Exception as ex: 
            print(f'ERROR in comment_input_wrapper {ex}')    
        
    def read_news_columns(self):
        #поиск информации о статье и текст самой статьи
        try:
            news_title = self.waiter.until(
                EC.presence_of_element_located((By.XPATH, self.elementAttribute["titleNews"])))
            
            author_news = self.waiter.until(
                EC.presence_of_element_located((By.CLASS_NAME, self.elementAttribute["authorNews"])))
            
            all_text_news = self.waiter.until(
                EC.presence_of_element_located((By.CLASS_NAME, self.elementAttribute["allTextNews"])))
            
            only_text_news = all_text_news.find_elements(By.TAG_NAME, self.elementAttribute["textNews"])

            date_news = self.waiter.until(
                EC.presence_of_element_located((By.CLASS_NAME, self.elementAttribute['dateNews'])))

        except Exception as ex:
            print(f'ERROR in read_news_columns {ex}')

    def setWebPage(self):
        
        try:
            self.driver.maximize_window()
            self.driver.get(url=self.url)
            self.read_comments_text()
        except Exception as ex:
            print(f'ERROR in set_web_page {ex}')
        

mururu = uraRuGrabber()
mururu.setWebPage()
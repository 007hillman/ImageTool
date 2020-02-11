import time
import configparser
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

class Crawler :
  def __init__(self, username, password,sent_url, image_path):
    
    options = Options()
    options.add_argument("--headless")
    #chrome_options = webdriver.ChromeOptions()  
    #chrome_options.add_argument("--headless")
    self.driver = webdriver.Firefox(firefox_options=options)
    self.image = image_path
    self.username = username
    self.password = password
  def loginface(self):
    print("Attempting to login to facebook...")
    self.driver.get('https://en-gb.facebook.com/login')
    usr_box = self.driver.find_element_by_id('email')
    usr_box.send_keys(self.username)
    pwd_box = self.driver.find_element_by_id('pass')
    pwd_box.send_keys(self.password)
    login_button = self.driver.find_element_by_id('loginbutton')
    login_button.submit()
    print("login successful, waiting for full page load. this might take a while (30s)...")
    self.driver.implicitly_wait(10)

  def post(self, text):
    #remove opaque screen 
    #self.driver.find_element_by_tag_name('body').click()
    #WALL
    give = self.driver.find_element_by_xpath("//*[@name='xhpc_message']")
    time.sleep(3)
    give.send_keys(text)
    time.sleep(5)
    #ATTACH MEDIA
    file = self.driver.find_element_by_name("composer_photo[]")
    # file = self.driver.find_element_by_xpath("//input[@data-testid='media-sprout']")
    self.driver.implicitly_wait(10)
        #sending media
    file.send_keys(self.image)
        #wait while it uploads
    time.sleep(10)

        #POST
    print("postind picture and comment...")
    post = self.driver.find_element_by_css_selector('button[data-testid="react-composer-post-button"]')
    post.click()
        #wait for post to be made
    time.sleep(10)
    self.driver.close()
    print("Image posted successfully...")
  def loginlink(self):
    print("Attempting to login to linkedln...")
    self.driver.get('https://www.linkedin.com/login')
    usr_box = self.driver.find_element_by_id('username')
    usr_box.send_keys(self.username)
    pwd_box = self.driver.find_element_by_id('password')
    pwd_box.send_keys(self.password)
    self.driver.find_element_by_xpath("//button[contains(text(),'Sign in')]").click()
    print("login successful, waiting for full page load...")
    time.sleep(10)
  def postlink(self, text):
    self.driver.find_element_by_class_name('sharing-create-share-view__create-content').click()
    time.sleep(3)
    self.driver.find_element_by_class_name('mentions-texteditor__contenteditable').send_keys(text)
    time.sleep(3)
    self.driver.find_elements_by_name("file")[0].send_keys(self.image)
    time.sleep(3)
    post_box = self.driver.find_element_by_class_name("//*[@data-control-name='share.post]")
    time.sleep(3)
    post_box.click()
    self.driver.close()

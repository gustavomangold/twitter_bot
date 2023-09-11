from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time, os

class Twitterbot:

	def __init__(self, email, password):

		self.email = email
		self.password = password
		# initializing chrome options
		# can be done with firefox
		chrome_options = Options()
		
		self.bot = webdriver.Chrome()

	def login(self):
		bot = self.bot
		bot.get('https://twitter.com/login')
		# sleep times can be adjusted according to internet speed
		time.sleep(3)
		
		email = bot.find_element(By.TAG_NAME,
			'input'
		)
		email.send_keys(self.email)
		# sends the password to the password input
		all_buttons = bot.find_elements(By.XPATH, "//div[@role = 'button']")
		all_buttons[-2].click()
		time.sleep(0.7)
		password = bot.find_element(By.XPATH, "//input[@type='password']")
		password.send_keys(self.password)

		password.send_keys(Keys.RETURN)

		time.sleep(2)

	def post_tweets(self,tweetBody):

		bot = self.bot  

		try:
		    bot.find_element(By.XPATH, "//a[@data-testid='SideNav_NewTweet_Button']").click()
		except:
		    time.sleep(3)
		    bot.find_element(By.XPATH, "//a[@data-testid='SideNav_NewTweet_Button']").click()

		time.sleep(4) 
		body = tweetBody

		try:
		    bot.find_element(By.XPATH, "//div[@role='textbox']").send_keys(body)
		except common.exceptions.NoSuchElementException:
		    time.sleep(3)
		    bot.find_element(By.XPATH, "//div[@role='textbox']").send_keys(body)

		time.sleep(2)
		bot.find_element(By.XPATH, "//div[@data-testid='tweetButton']").click()
		time.sleep(4) 


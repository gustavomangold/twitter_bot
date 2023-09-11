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
		# sends the email to the email input
		email.send_keys(self.email)
		# sends the password to the password input
		all_buttons = bot.find_elements(By.XPATH, "//div[@role = 'button']")
		all_buttons[-2].click()
		time.sleep(0.7)
		password = bot.find_element(By.XPATH, "//input[@type='password']")
		password.send_keys(self.password)
		# executes RETURN key action
		password.send_keys(Keys.RETURN)

		time.sleep(2)

	def like_retweet(self, hashtag):

		"""
		This function automatically retrieves
		the tweets and then likes and retweets them

		Arguments:
			hashtag {string} -- twitter hashtag
		"""

		bot = self.bot

		# fetches the latest tweets with the provided hashtag
		bot.get(
			'https://twitter.com / search?q =% 23' + \
			hashtag+'&src = typed_query&f = live'
		)

		time.sleep(3)

		# using set so that only unique links
		# are present and to avoid unnecessary repetition
		links = set()

		# obtaining the links of the tweets
		for _ in range(100):
			# executing javascript code
			# to scroll the webpage
			bot.execute_script(
				'window.scrollTo(0, document.body.scrollHeight)'
			)

			time.sleep(4)

			# using list comprehension
			# for adding all the tweets link to the set
			# this particular piece of code might
			# look very complicated but the only reason
			# I opted for list comprehension because is
			# lot faster than traditional loops
			[
				links.add(elem.get_attribute('href'))\
				for elem in bot.find_elements(By.XPATH, "//a[@dir ='auto']")
			]

		# traversing through the generated links
		for link in links:
			# opens individual links
			bot.get(link)
			time.sleep(4)

			try:
				# retweet button selector
				bot.find_element_by_css_selector(
					'.css-18t94o4[data-testid ="retweet"]'
				).click()
				# initializes action chain
				actions = ActionChains(bot)
				# sends RETURN key to retweet without comment
				actions.send_keys(Keys.RETURN).perform()

				# like button selector
				bot.find_element_by_css_selector(
					'.css-18t94o4[data-testid ="like"]'
				).click()
				# adding higher sleep time to avoid
				# getting detected as bot by twitter
				time.sleep(10)
			except:
				time.sleep(2)
				
	

		# fetches the main homepage
		bot.get('https://twitter.com/')
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


import twitterbot as tb
import secrets, sys

# the command must be called with python3 main_script.py 'tweet_to_be_posted'
# the argument is the tweet
# fetches the hashtag from command line argument
argument = sys.argv[1]

# initialize the bot with your username/email or password
bot = tb.Twitterbot('email_or_username-string', 'password-string')
bot.login()
# calling post_tweet function
bot.post_tweet(argument)


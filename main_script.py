import twitterbot as tb
import secrets, sys

# fetches the hashtag from command line argument
argument = sys.argv[1]
# fetches the credentials dictionary
# using get_credentials function
credentials = secrets.get_credentials()
# initialize the bot with your credentials
bot = tb.Twitterbot('ja_pode_almosar', 'senhaforte21')
# logging in
bot.login()
# calling like_retweet function
bot.post_tweets(argument)


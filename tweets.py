import tweepy
from colorama import init
from mystreamListener import MyStreamListener

# init colorama
init()


def print_tweets(status):
    print(status.user.screen_name + ' : ' + status.text)


consumer_key = 'Tf8WmaLCWFja3saFR3GgowaJX'
consumer_secret = 'E4D9H3rY6py3W1OUCmhEVP9erLym2KsprcoZhvsB3in8PnBAE1'
access_token = '149328992-e98pmhIcSBZLQSwcz3D05MDUh3p9x92Io6Ei88TI'
access_token_secret = 'vnJZCu65XqklBIqJnbWEItmuN14nxqAIE2iBVcLJnYSN8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

myStreamListener = MyStreamListener(print_tweets)

myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=['python'], async=True)

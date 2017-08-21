import tweepy

# override tweepy.StreamListener to add logic to on_status



class MyStreamListener(tweepy.StreamListener):

    def __init__(self, print_status):
        self.print_status = print_status
        super(MyStreamListener, self).__init__()

    def on_status(self, status):
        self.print_status(status)


    def on_error(self, status_code):
        if status_code == 420:        
            return False



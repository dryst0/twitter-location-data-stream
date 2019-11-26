
from tweepy import Stream, OAuthHandler

from .listeners import TweetListener


class TwitterClient():

    def __init__(self, aws_firehose_client, twitter_api_consumer_key, twitter_api_consumer_key_secret, twitter_api_access_token, twitter_api_access_token_secret):
        self._twitter_api_consumer_key = twitter_api_consumer_key
        self._twitter_api_consumer_key_secret = twitter_api_consumer_key_secret
        self._twitter_api_access_token = twitter_api_access_token
        self._twitter_api_access_token_secret = twitter_api_access_token_secret
        self._oauth = self._authenticate()
        self._tweet_listener = TweetListener(aws_firehose_client)
        self._tweet_stream = self._get_tweet_stream()

    def _authenticate(self):
        oauth = OAuthHandler(self._twitter_api_consumer_key, self._twitter_api_consumer_key_secret)
        oauth.set_access_token(self._twitter_api_access_token, self._twitter_api_access_token_secret)

        return oauth

    def _get_tweet_stream(self):
        return Stream(self._oauth, self._tweet_listener)

    def listen(self, location_bounding_box):
        self._tweet_stream.filter(locations=location_bounding_box)

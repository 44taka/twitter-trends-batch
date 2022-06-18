import tweepy
from core.settings import TwitterApiSettings


# 接続情報読み込み
twitter_api_settings = TwitterApiSettings()

# 認証
twitter_api_auth = tweepy.OAuthHandler(
    consumer_key=twitter_api_settings.api_key,
    consumer_secret=twitter_api_settings.api_secret_key
)
twitter_api_auth.set_access_token(
    key=twitter_api_settings.access_token,
    secret=twitter_api_settings.access_token_secret
)

# TwitterAPIセット
twitter_api = tweepy.API(twitter_api_auth)

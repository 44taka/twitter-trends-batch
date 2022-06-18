from loguru import logger
from tweepy.errors import TweepyException

from usecase.twitter.trends import TwitterTrendsUseCase


class TwitterTrendsCommand(object):
    
    def __init__(self, tuc: TwitterTrendsUseCase):
        self._tuc = tuc
    
    def run(self) -> int:
        try:
            trends = self._tuc.get(woeid=23424856)
            self._tuc.register(trends=trends)
            return 0
        except TweepyException as e:
            logger.exception(e)
            return 1
        except Exception as e:
            logger.exception(e)
            return 2

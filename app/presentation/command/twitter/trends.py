from tkinter import W
from loguru import logger
from tweepy.errors import TweepyException

from core.constants import Constants
from usecase.twitter.trends import TwitterTrendsUseCase


class TwitterTrendsCommand(object):
    
    def __init__(self, tuc: TwitterTrendsUseCase):
        self._tuc = tuc
    
    def run(self, woeid: int=None) -> int:
        try:
            if woeid is None:
                wid = Constants().WOEID_JAPAN
            else:
                wid = self._tuc.woeid_find_by_id(woeid=woeid).id
            trends = self._tuc.get(woeid=wid)
            self._tuc.register(trends=trends)
            return 0
        except TweepyException as e:
            logger.exception(e)
            return 1
        except Exception as e:
            logger.exception(e)
            return 2

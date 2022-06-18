from typing import List

from loguru import logger
from orator import DatabaseManager
import tweepy

from domain.model.twitter.trends import TwitterTrendsModel, TwitterTrendsApiModel
from domain.repository.twitter.trends import TwitterTrendsRepository


class TwitterTrendsPersistence(TwitterTrendsRepository):
    """Twitterトレンド永続化処理クラス"""
    
    def __init__(self, db: DatabaseManager, twitter_api: tweepy.API):
        self._db = db
        self._twitter_api = twitter_api

    def find(self, woeid: int) -> List[TwitterTrendsApiModel]:
        """TwitterトレンドAPI実行

        Args:
            woeid (int): 地域ID

        Returns:
            List[TwitterTrendsApiModel]: TwitterトレンドAPIモデルのリスト
        """
        try:
            result = self._twitter_api.get_place_trends(id=woeid)
            logger.debug(result)
            return list(map(
                TwitterTrendsApiModel.parse_obj, result[0]['trends']
            ))
        except:
            raise
    
    def insert(self, trends: List[TwitterTrendsApiModel]) -> None:
        """Twitterトレンド情報をDBに登録

        Args:
            trends (List[TwitterTrendsApiModel]): TwitterトレンドAPIモデルのリスト
        """
        # TODO:リファクタしたい
        try:
            data = []
            for index, trend in enumerate(trends):
                data.append(TwitterTrendsModel(
                    rank=index + 1,
                    name=trend.name,
                    url=trend.url,
                    tweet_volume=trend.tweet_volume,
                ).dict())
            query = self._db.table(TwitterTrendsModel.Config.table_name)
            result = query.insert(data)
            logger.debug(result)
        except:
            raise

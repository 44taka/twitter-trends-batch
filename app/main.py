import sys

from loguru import logger
import fire

from infrastructure.database import db
from infrastructure.twitter_api import twitter_api
from infrastructure.persistence.woeid import WoeIdPersistence
from infrastructure.persistence.twitter.trends import TwitterTrendsPersistence

from presentation.command.twitter.trends import TwitterTrendsCommand
from usecase.twitter.trends import TwitterTrendsUseCaseImpl


class Main(object):
    
    # TODO:Twitter関連のCLIはグループ化してまとめたい。APIのルーティングみたいな感じでやりたい。
    def twitter_trends(self, woeid: int=None):
        logger.info('Twitterトレンド取得 START')
        # DI注入
        wip = WoeIdPersistence(db=db)
        ttp = TwitterTrendsPersistence(db=db, twitter_api=twitter_api)
        tuc = TwitterTrendsUseCaseImpl(wip=wip, ttp=ttp)
        ttc = TwitterTrendsCommand(tuc=tuc)
        # 処理実行
        status = ttc.run(woeid=woeid)
        logger.debug('status = ' + str(status))
        logger.info('Twitterトレンド取得 END')
        sys.exit(status)


if __name__ == '__main__':
    fire.Fire(Main)

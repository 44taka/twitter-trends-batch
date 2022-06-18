from tweepy.errors import TweepyException
import pytest

from presentation.command.twitter.trends import TwitterTrendsCommand
from infrastructure.database import db
from infrastructure.twitter_api import twitter_api
from infrastructure.persistence.woeid import WoeIdPersistence
from infrastructure.persistence.twitter.trends import TwitterTrendsPersistence
from usecase.twitter.trends import TwitterTrendsUseCaseImpl


# フィクスチャ
@pytest.fixture
def ttc():
    wip = WoeIdPersistence(db=db)
    ttp = TwitterTrendsPersistence(db=db, twitter_api=twitter_api)
    tuc = TwitterTrendsUseCaseImpl(wip=wip, ttp=ttp)
    return TwitterTrendsCommand(tuc=tuc)


class TestTwitterTrendsCommand(object):
    
    def test_run(self, ttc: TwitterTrendsCommand):
        result = ttc.run()
        assert result == 0
    
    @pytest.mark.parametrize('exception, expected', [
        (TweepyException, 1),
        (Exception, 2),
    ])
    def test_exception_run(self, 
                           mocker, 
                           exception: Exception, 
                           expected: int, 
                           ttc: TwitterTrendsCommand):
        # モックを使って例外発生させる
        mock = mocker.MagicMock()
        mock.get = mocker.Mock(side_effect=exception)
        mocker.patch.object(ttc, "_tuc", mock)
        result = ttc.run()
        assert result == expected
